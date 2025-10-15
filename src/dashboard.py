# dashboard.py
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from monitor import SystemMonitor
from config import config

class HealthDashboard:
    def __init__(self, root):
        self.root = root
        self.monitor = SystemMonitor()
        self.setup_ui()
        self.setup_charts()
        self.update_data()
    
    def setup_ui(self):
        """Setup the main user interface"""
        # Configure window
        self.root.title("System Health Monitor")
        self.root.geometry(config.window_size)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create tabs
        self.tabview = ctk.CTkTabview(self.main_frame)
        self.tabview.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Add tabs
        self.overview_tab = self.tabview.add("Overview")
        self.process_tab = self.tabview.add("Processes")
        self.charts_tab = self.tabview.add("Charts")
        
        self.setup_overview_tab()
        self.setup_process_tab()
    
    def setup_overview_tab(self):
        """Setup the overview tab with system metrics"""
        # CPU Frame
        cpu_frame = ctk.CTkFrame(self.overview_tab)
        cpu_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkLabel(cpu_frame, text="CPU", font=("Arial", 16, "bold")).pack(pady=5)
        self.cpu_usage_label = ctk.CTkLabel(cpu_frame, text="Usage: 0%")
        self.cpu_usage_label.pack()
        self.cpu_cores_label = ctk.CTkLabel(cpu_frame, text="Cores: 0")
        self.cpu_cores_label.pack()
        
        # Memory Frame
        memory_frame = ctk.CTkFrame(self.overview_tab)
        memory_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkLabel(memory_frame, text="Memory", font=("Arial", 16, "bold")).pack(pady=5)
        self.memory_usage_label = ctk.CTkLabel(memory_frame, text="Usage: 0%")
        self.memory_usage_label.pack()
        self.memory_used_label = ctk.CTkLabel(memory_frame, text="Used: 0 GB")
        self.memory_used_label.pack()
        
        # Disk Frame
        disk_frame = ctk.CTkFrame(self.overview_tab)
        disk_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkLabel(disk_frame, text="Disk", font=("Arial", 16, "bold")).pack(pady=5)
        self.disk_usage_label = ctk.CTkLabel(disk_frame, text="Usage: 0%")
        self.disk_usage_label.pack()
        self.disk_free_label = ctk.CTkLabel(disk_frame, text="Free: 0 GB")
        self.disk_free_label.pack()
        
        # GPU Frame
        gpu_frame = ctk.CTkFrame(self.overview_tab)
        gpu_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkLabel(gpu_frame, text="GPU", font=("Arial", 16, "bold")).pack(pady=5)
        self.gpu_usage_label = ctk.CTkLabel(gpu_frame, text="Usage: 0%")
        self.gpu_usage_label.pack()
        self.gpu_temp_label = ctk.CTkLabel(gpu_frame, text="Temp: 0°C")
        self.gpu_temp_label.pack()
        
        # Configure grid weights
        self.overview_tab.grid_columnconfigure(0, weight=1)
        self.overview_tab.grid_columnconfigure(1, weight=1)
        self.overview_tab.grid_rowconfigure(0, weight=1)
        self.overview_tab.grid_rowconfigure(1, weight=1)
    
    def setup_process_tab(self):
        """Setup the processes tab"""
        # Processes label
        ctk.CTkLabel(self.process_tab, text="Top Processes by CPU Usage", 
                    font=("Arial", 16, "bold")).pack(pady=10)
        
        # Processes frame
        self.processes_frame = ctk.CTkScrollableFrame(self.process_tab)
        self.processes_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Will be populated in update_data
    
    def setup_charts(self):
        """Setup matplotlib charts"""
        # Create figure for charts
        self.fig = Figure(figsize=(10, 8), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, self.charts_tab)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Create subplots
        self.ax1 = self.fig.add_subplot(221)  # CPU
        self.ax2 = self.fig.add_subplot(222)  # Memory
        self.ax3 = self.fig.add_subplot(223)  # Disk
        self.ax4 = self.fig.add_subplot(224)  # GPU
        
        self.fig.tight_layout(pad=3.0)
        
        # Initialize data for charts
        self.cpu_data = [0]
        self.memory_data = [0]
        self.disk_data = [0]
        self.gpu_data = [0]
    
    def update_charts(self, stats):
        """Update the matplotlib charts"""
        # Add new data
        self.cpu_data.append(stats['cpu']['usage'])
        self.memory_data.append(stats['memory']['usage'])
        self.disk_data.append(stats['disk']['usage'])
        self.gpu_data.append(stats['gpu']['usage'])
        
        # Keep only last 20 points
        if len(self.cpu_data) > 20:
            self.cpu_data = self.cpu_data[-20:]
            self.memory_data = self.memory_data[-20:]
            self.disk_data = self.disk_data[-20:]
            self.gpu_data = self.gpu_data[-20:]
        
        # Clear and update plots
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()
        
        # CPU Chart
        self.ax1.plot(self.cpu_data, 'r-')
        self.ax1.set_title('CPU Usage %')
        self.ax1.set_ylim(0, 100)
        
        # Memory Chart
        self.ax2.plot(self.memory_data, 'b-')
        self.ax2.set_title('Memory Usage %')
        self.ax2.set_ylim(0, 100)
        
        # Disk Chart
        self.ax3.plot(self.disk_data, 'g-')
        self.ax3.set_title('Disk Usage %')
        self.ax3.set_ylim(0, 100)
        
        # GPU Chart
        self.ax4.plot(self.gpu_data, 'purple')
        self.ax4.set_title('GPU Usage %')
        self.ax4.set_ylim(0, 100)
        
        self.canvas.draw()
    
    def update_data(self):
        """Update all data in the dashboard"""
        try:
            # Get current stats
            stats = self.monitor.get_all_stats()
            
            # Update overview labels
            self.cpu_usage_label.configure(text=f"Usage: {stats['cpu']['usage']:.1f}%")
            self.cpu_cores_label.configure(text=f"Cores: {stats['cpu']['cores']}")
            
            self.memory_usage_label.configure(text=f"Usage: {stats['memory']['usage']:.1f}%")
            self.memory_used_label.configure(text=f"Used: {stats['memory']['used']} GB / {stats['memory']['total']} GB")
            
            self.disk_usage_label.configure(text=f"Usage: {stats['disk']['usage']:.1f}%")
            self.disk_free_label.configure(text=f"Free: {stats['disk']['free']} GB")
            
            self.gpu_usage_label.configure(text=f"Usage: {stats['gpu']['usage']:.1f}%")
            self.gpu_temp_label.configure(text=f"Temp: {stats['gpu']['temperature']}°C")
            
            # Update processes
            self.update_processes_display(stats['processes'])
            
            # Update charts
            self.update_charts(stats)
            
            # Check warnings
            self.check_warnings(stats)
            
        except Exception as e:
            print(f"Error updating data: {e}")
        
        # Schedule next update
        self.root.after(config.refresh_interval, self.update_data)
    
    def update_processes_display(self, processes):
        """Update the processes display"""
        # Clear existing processes
        for widget in self.processes_frame.winfo_children():
            widget.destroy()
        
        # Add header
        header_frame = ctk.CTkFrame(self.processes_frame)
        header_frame.pack(fill="x", pady=2)
        
        ctk.CTkLabel(header_frame, text="Process Name", width=200, anchor="w").pack(side="left", padx=5)
        ctk.CTkLabel(header_frame, text="CPU %", width=80).pack(side="left", padx=5)
        ctk.CTkLabel(header_frame, text="Memory %", width=80).pack(side="left", padx=5)
        ctk.CTkLabel(header_frame, text="PID", width=80).pack(side="left", padx=5)
        
        # Add process rows
        for proc in processes:
            proc_frame = ctk.CTkFrame(self.processes_frame)
            proc_frame.pack(fill="x", pady=1)
            
            ctk.CTkLabel(proc_frame, text=proc['name'][:30], width=200, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(proc_frame, text=f"{proc['cpu_percent'] or 0:.1f}", width=80).pack(side="left", padx=5)
            ctk.CTkLabel(proc_frame, text=f"{proc['memory_percent'] or 0:.2f}", width=80).pack(side="left", padx=5)
            ctk.CTkLabel(proc_frame, text=f"{proc['pid']}", width=80).pack(side="left", padx=5)
    
    def check_warnings(self, stats):
        """Check for warning conditions"""
        warnings = []
        
        if stats['cpu']['usage'] > config.warning_thresholds['cpu']:
            warnings.append(f"High CPU usage: {stats['cpu']['usage']:.1f}%")
        
        if stats['memory']['usage'] > config.warning_thresholds['memory']:
            warnings.append(f"High Memory usage: {stats['memory']['usage']:.1f}%")
        
        if stats['disk']['usage'] > config.warning_thresholds['disk']:
            warnings.append(f"High Disk usage: {stats['disk']['usage']:.1f}%")
        
        if stats['gpu']['temperature'] > config.warning_thresholds['temperature']:
            warnings.append(f"High GPU temperature: {stats['gpu']['temperature']}°C")
        
        # You could add a warning display here
        if warnings:
            print("Warnings:", ", ".join(warnings))