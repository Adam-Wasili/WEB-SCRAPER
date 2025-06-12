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
