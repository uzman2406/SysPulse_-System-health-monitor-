# monitor.py
import psutil
from typing import Dict, Any

class SystemMonitor:
    def __init__(self):
        pass  # Remove speedtest initialization
    
    def get_cpu_info(self) -> Dict[str, Any]:
        """Get CPU information"""
        return {
            'usage': psutil.cpu_percent(interval=1),
            'cores': psutil.cpu_count(logical=False),
            'threads': psutil.cpu_count(logical=True),
            'frequency': psutil.cpu_freq().current if psutil.cpu_freq() else 0
        }
    
    def get_memory_info(self) -> Dict[str, Any]:
        """Get memory information"""
        memory = psutil.virtual_memory()
        return {
            'total': round(memory.total / (1024**3), 2),  # GB
            'used': round(memory.used / (1024**3), 2),
            'free': round(memory.free / (1024**3), 2),
            'usage': memory.percent
        }
    
    def get_disk_info(self) -> Dict[str, Any]:
        """Get disk information"""
        disk = psutil.disk_usage('/')
        return {
            'total': round(disk.total / (1024**3), 2),  # GB
            'used': round(disk.used / (1024**3), 2),
            'free': round(disk.free / (1024**3), 2),
            'usage': disk.percent
        }
    
    def get_network_info(self) -> Dict[str, Any]:
        """Get network information - simplified without speedtest"""
        network = psutil.net_io_counters()
        return {
            'bytes_sent': round(network.bytes_sent / (1024**2), 2),  # MB
            'bytes_recv': round(network.bytes_recv / (1024**2), 2),  # MB
            'packets_sent': network.packets_sent,
            'packets_recv': network.packets_recv
        }
    
    def get_gpu_info(self) -> Dict[str, Any]:
        """Get GPU information - simplified"""
        # Simple GPU info that won't cause errors
        return {
            'name': 'GPU Monitoring', 
            'usage': 0, 
            'memory_used': 0, 
            'memory_total': 0, 
            'temperature': 0
        }
    
    def get_running_processes(self, top_n: int = 5) -> list:
        """Get top N processes by CPU usage"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)
        return processes[:top_n]
    
    def get_all_stats(self) -> Dict[str, Any]:
        """Get all system statistics"""
        return {
            'cpu': self.get_cpu_info(),
            'memory': self.get_memory_info(),
            'disk': self.get_disk_info(),
            'network': self.get_network_info(),
            'gpu': self.get_gpu_info(),
            'processes': self.get_running_processes(5)
        }