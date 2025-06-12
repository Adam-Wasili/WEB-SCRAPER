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
        
        # Fetch HTML Button
        self.fetch_html_btn = ttk.Button(
            button_frame,
            text="Fetch HTML",
            command=self.fetch_html
        )
        self.fetch_html_btn.pack(side=tk.LEFT, padx=2)

        # Fetch IP Button
        self.fetch_ip_btn = ttk.Button(
            button_frame,
            text="Fetch IP Address",
            command=self.fetch_ip
        )
        self.fetch_ip_btn.pack(side=tk.LEFT, padx=2)
          # HTML Display
        self.html_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.html_display.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NSEW)

        # IP Display
        self.ip_label = ttk.Label(self.master, text="IP Address: ")
        self.ip_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.SW)

        # Status Bar
        self.status_bar = ttk.Label(self.master, text="", relief=tk.SUNKEN)
        self.status_bar.grid(row=4, column=0, padx=5, pady=5, sticky=tk.EW)

    def fetch_html(self):
        url = self.url_entry.get().strip()
        if not url:
            self.update_status("Error: URL cannot be empty")
            return
        if not url.startswith(('http://', 'https://')):
            self.update_status("Error: URL must include http:// or https://")
            return

        self.toggle_buttons(False)
        self.update_status("Fetching HTML...")

        thread = threading.Thread(target=self._fetch_html_thread, args=(url,))
        thread.start()

        


        
