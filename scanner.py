import asyncio
import argparse
from datetime import datetime
from typing import List, Dict
import os

# Semaphore to limit concurrent tasks
semaphore = asyncio.Semaphore(100)

async def scan_port(target: str, port: int, timeout: float = 2.0) -> Dict:
    async with semaphore:
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(target, port),
                timeout=timeout
            )
            writer.close()
            await writer.wait_closed()
            return {"port": port, "state": "open"}
        except (asyncio.TimeoutError, ConnectionRefusedError):
            return {"port": port, "state": "closed"}
        except Exception as e:
            return {"port": port, "state": f"error: {str(e)}"}

async def scan_ports(target: str, start_port: int, end_port: int) -> List[Dict]:
    tasks = [scan_port(target, port) for port in range(start_port, end_port + 1)]
    return await asyncio.gather(*tasks)

def save_results(results: List[Dict], output_file: str):
    with open(output_file, 'w') as f:
        for result in results:
            if result['state'] == 'open':
                f.write(f"Port {result['port']}: {result['state']}\n")
    print(f"\nResults saved to {output_file}")

async def main():
    parser = argparse.ArgumentParser(description="Asynchronous Port Scanner using asyncio")
    parser.add_argument("target", help="Target IP address or domain")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--timeout", type=float, default=2.0, help="Timeout in seconds per port (default: 2.0)")
    parser.add_argument("--output", help="Output file to save open ports", default="open_ports.txt")

    args = parser.parse_args()

    print(f"Starting async port scan on {args.target} from port {args.start} to {args.end}\n")
    start_time = datetime.now()

    results = await scan_ports(args.target, args.start, args.end)
    duration = datetime.now() - start_time

    open_ports = [r for r in results if r['state'] == 'open']

    if open_ports:
        print("\nOpen ports:")
        for result in open_ports:
            print(f"Port {result['port']}: {result['state']}")
    else:
        print("\nNo open ports found.")

    save_results(open_ports, args.output)
    print(f"\nScan completed in {duration}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")
