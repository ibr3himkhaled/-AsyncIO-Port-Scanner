⚡ AsyncIO Port Scanner

**AsyncIO Port Scanner** is a fast, lightweight, and fully asynchronous port scanning tool written in Python using the `asyncio` library. It’s built for developers, network administrators, and ethical hackers who need to scan ports quickly and efficiently without overloading their systems.

🚀 Features

- 🔄 **Asynchronous scanning** using `asyncio.Semaphore` for safe and controlled concurrency
- 🎯 Scan **custom port ranges** (from any start to any end port)
- ⏱️ Adjustable **timeout settings** to skip unresponsive ports
- 📂 **Save open ports** to a file with `--output`
- 📉 **Execution time reporting** after each scan
- 💻 **CLI-based tool** (no GUI, pure terminal)

🧠 How It Works

The tool uses Python’s asyncio to launch multiple simultaneous connection attempts to the target host’s TCP ports within the specified range. It applies a semaphore to limit concurrent scans to a safe number (default 100) to avoid overwhelming system resources or the target network.

Each connection attempt has a configurable timeout. If the connection succeeds, the port is marked open; if it times out or is refused, it is considered closed or filtered.

The asynchronous approach ensures fast scanning speeds compared to sequential scans.

📦 Requirements

- Python 3.7+
- No third-party libraries needed (standard library only)

📥 Installation

Just clone this repo — no installation or pip requirements:

Command:

git clone https://github.com/yourusername/asyncio-port-scanner.git

cd asyncio-port-scanner

▶️ Usage

python3 scanner.py <target> [--start START_PORT] [--end END_PORT] [--timeout TIMEOUT] [--output FILE]

🧪 Example

python3 scanner.py 192.168.1.100 --start 20 --end 1000 --timeout 1.5 --output results.txt

⚠️ Disclaimer
This tool is intended for authorized use only. Scanning devices or networks without explicit permission is illegal. Use responsibly and only on systems you own or have permission to test.
