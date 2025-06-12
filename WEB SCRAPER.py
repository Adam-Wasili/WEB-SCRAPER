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
        
if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()

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
        
    def _fetch_html_thread(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            html_content = response.text
            self.master.after(0, self._display_html, html_content, None)
        except Exception as e:
            self.master.after(0, self._display_html, None, str(e))
        finally:
            self.master.after(0, self.toggle_buttons, True)

    def _display_html(self, content, error):
        if error:
            self.update_status(f"Error: {error}")
            return

        self.html_display.delete('1.0', tk.END)
        self.html_display.insert(tk.END, content)
        self.update_status("HTML content fetched successfully")

    def fetch_ip(self):
        url = self.url_entry.get().strip()
        if not url:
            self.update_status("Error: URL cannot be empty")
            return

        self.toggle_buttons(False)
        self.update_status("Fetching IP address...")

        thread = threading.Thread(target=self._fetch_ip_thread, args=(url,))
        thread.start()
        
    def _fetch_ip_thread(self, url):
        try:
            # Add protocol if missing for proper parsing
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            parsed_url = urlparse(url)
            domain = parsed_url.netloc

            # Get IP address
            ip = socket.gethostbyname(domain)
            self.master.after(0, self._display_ip, ip, None)
        except Exception as e:
            self.master.after(0, self._display_ip, None, str(e))
        finally:
            self.master.after(0, self.toggle_buttons, True)
            
    def _display_ip(self, ip, error):
        if error:
            self.update_status(f"Error: {error}")
            self.ip_label.config(text="IP Address: ")
            return

        self.ip_label.config(text=f"IP Address: {ip}")
        self.update_status("IP address fetched successfully")
        
    def toggle_buttons(self, state):
        self.fetch_html_btn.config(state=tk.NORMAL if state else tk.DISABLED)
        self.fetch_ip_btn.config(state=tk.NORMAL if state else tk.DISABLED)
          def update_status(self, message):
        self.status_bar.config(text=message)
        # Clear status after 5 seconds
        self.master.after(5000, lambda: self.status_bar.config(text=""))



        


        


        
