# config.py
import json

class Config:
    def __init__(self):
        self.refresh_interval = 2000  # 2 seconds
        self.warning_thresholds = {
            'cpu': 80,          # 80% usage
            'memory': 85,       # 85% usage  
            'disk': 90,         # 90% usage
            'temperature': 75   # 75°C
        }
        self.window_size = "800x600"
        
    def save_settings(self):
        with open('settings.json', 'w') as f:
            json.dump(self.__dict__, f)
    
    def load_settings(self):
        try:
            with open('settings.json', 'r') as f:
                data = json.load(f)
                self.__dict__.update(data)
        except FileNotFoundError:
            self.save_settings()

config = Config()
config.load_settings()