import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
import socket
from urllib.parse import urlparse
import threading

class WebScraperApp:
    def __init__(self, master):
        self.master = master
        master.title("Web Scraper with GUI")

        # Configure window size and grid layout
        master.geometry("800x600")
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(3, weight=1)
         # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # URL Entry
        ttk.Label(self.master, text="Enter URL:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.url_entry = ttk.Entry(self.master, width=50)
        self.url_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)

        # Buttons Frame
        button_frame = ttk.Frame(self.master)
        button_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.EW)

        


        
