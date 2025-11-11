# 🖥️ System Health Monitor

A lightweight, real-time system monitoring application built with Python. Monitor your CPU, memory, disk, network, and running processes in a beautiful dark-themed interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

## 📥 Direct Download

### 🚀 Ready-to-Use Executable
[**Download SystemHealthMonitor.exe**](https://github.com/uzman2406/SysPulse_-System-health-monitor-/blob/master/dist/SystemHealthMonitor.exe) - Just download and run!
##download it as a raw file from download file option even if nothing is shown in exe file file because that's how it an exe file is shown in github but it is safe to download this exe file as ra and then run it.

> ⚠️ **Note**: Some antivirus software may flag the EXE as suspicious because it's not digitally signed. This is a false positive - you can safely run it or build from source.

## ✨ Features

- **Real-time CPU Monitoring**: Usage percentage, cores, frequency
- **Memory Tracking**: RAM usage, total/used/free memory
- **Disk Monitoring**: Storage usage across drives
- **Network Statistics**: Data sent/received
- **Process Management**: Top 5 resource-consuming processes
- **Live Charts**: Historical usage graphs
- **Beautiful Dark UI**: Modern CustomTkinter interface
- **Lightweight**: Low resource consumption
- **Portable**: No installation required

## 🖼️ Application Preview

![System Health Monitor](docs/preview.png)

*Three-tab interface showing Overview, Processes, and Charts*

## 🛠️ For Developers

### Prerequisites
- Python 3.8+
- pip package manager

### Installation & Running from Source

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/system-health-monitor.git
   cd system-health-monitor

2.Install dependencies

pip install -r requirements.txt

3.Run the application
python src/main.py


To build your own executable:

pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico --name "SystemHealthMonitor" src/main.py


Project Structure:

system-health-monitor/

├── src/                 # Source code

   │   ├── main.py         # Application entry point

   │   ├── monitor.py      # System monitoring logic

   │   ├── dashboard.py    # GUI interface

   │   └── config.py       # Configuration settings


├── dist/               # Built executables (download here!)

├── docs/               # Documentation

   ├── .gitignore          # Git ignore rules

   ├── requirements.txt    # Python dependencies

   ├── build.spec          # PyInstaller build configuration

   ├── icon.ico           # Application icon

   └── README.md          # This file





