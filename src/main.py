# main.py
import customtkinter as ctk
from dashboard import HealthDashboard
from config import config

def main():
    # Create main window
    root = ctk.CTk()
    
    # Create dashboard
    app = HealthDashboard(root)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()