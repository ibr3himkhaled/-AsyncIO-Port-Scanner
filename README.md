# ⚡ AsyncIO Port Scanner

**AsyncIO Port Scanner** is a fast, lightweight, and fully asynchronous port scanning tool written in Python using the `asyncio` library. It’s built for developers, network administrators, and ethical hackers who need to scan ports quickly and efficiently without overloading their systems.

---

## 🚀 Features

- 🔄 **Asynchronous scanning** using `asyncio.Semaphore` for safe and controlled concurrency
- 🎯 Scan **custom port ranges** (from any start to any end port)
- ⏱️ Adjustable **timeout settings** to skip unresponsive ports
- 📂 **Save open ports** to a file with `--output`
- 📉 **Execution time reporting** after each scan
- 💻 **CLI-based tool** (no GUI, pure terminal)

---

## 🧠 How It Works

The scanner uses Python’s `asyncio` to open TCP connections to a target host across a specified port range. Ports that respond within the timeout are marked as **open**, while others are considered **closed** or **filtered**.

To prevent overwhelming your network or system, the tool uses a **semaphore** to limit the number of concurrent tasks (default: 100).

---

## 📦 Requirements

- **Python 3.7+**
- No third-party libraries needed (standard library only)

---

## 📥 Installation

Just clone this repo — no installation or pip requirements:

```bash
git clone https://github.com/yourusername/asyncio-port-scanner.git
cd asyncio-port-scanner
