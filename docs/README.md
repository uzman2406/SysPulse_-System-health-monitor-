# 🖥️ System Health Monitor

A lightweight, real-time system monitoring application built with Python. Monitor your CPU, memory, disk, network, and running processes in a beautiful dark-themed interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

##Screenshots

<img width="1187" height="936" alt="image" src="https://github.com/user-attachments/assets/06bb5067-6b1a-4986-bdbb-340f52da2b4c" />

<img width="1190" height="928" alt="image" src="https://github.com/user-attachments/assets/70f5e353-6f08-4c04-9e68-8e99c8ff2c11" />

<img width="1191" height="928" alt="image" src="https://github.com/user-attachments/assets/12972004-089f-4576-a478-d9846aff8b3e" />


##  Direct Download

###  Ready-to-Use Executable
[**Download SystemHealthMonitor.exe**](https://github.com/uzman2406/SysPulse_-System-health-monitor-/blob/master/dist/SystemHealthMonitor.exe) - Just download and run!
##download it as a raw file from download file option even if nothing is shown in exe file file because that's how  an exe file is shown in github but it is safe to download this exe file as raw and then run it.

>  **Note**: Some antivirus software may flag the EXE as suspicious because it's not digitally signed. This is a false positive - you can safely run it or build from source.

##  Features

- **Real-time CPU Monitoring**: Usage percentage, cores, frequency
- **Memory Tracking**: RAM usage, total/used/free memory
- **Disk Monitoring**: Storage usage across drives
- **Network Statistics**: Data sent/received
- **Process Management**: Top 5 resource-consuming processes
- **Live Charts**: Historical usage graphs
- **Beautiful Dark UI**: Modern CustomTkinter interface
- **Lightweight**: Low resource consumption
- **Portable**: No installation required



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








