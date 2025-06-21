


Web Scraper with GUI
A Python application with a simple Tkinter-based interface that allows users to:
•	 Fetch and view the HTML content of any webpage
•	 Retrieve the IP address of a given URL
Built using:
•	tkinter for GUI
•	requests for HTTP requests
•	socket for DNS resolution
•	threading for responsive GUI interaction

No browser required — just input a URL and hit a button!
________________________________________
 What is Web Scraping?
Web scraping is the process of automatically extracting data from websites. It involves sending a request to a web page, downloading the HTML content, and parsing it to find specific information.
This tool demonstrates the basics of scraping by allowing users to:
•	View raw HTML code of a webpage
•	Resolve the domain to its IP address
 Note: Web scraping should always respect a site's terms of service and robots.txt. Avoid scraping sensitive or copyrighted content.
________________________________________
 Features
•	 Fetch and display HTML from any valid URL
•	 Extract the domain’s IP address
•	 Scrollable text window to view large HTML content
•	 Status bar for real-time feedback
•	 Multithreaded for a responsive GUI
Error Handling
The app performs checks like:
•	Empty URL input
•	Missing protocol (http://)
•	Invalid domain or network errors

________________________________________
 GUI Overview
sql
-----------------------------------------------------
| Enter URL: [ https://example.com              ]   |
| [ Fetch HTML ]   [ Fetch IP Address ]             |
|--------------------------------------------------|
|                                                  |
|        (Scrollable HTML Content Window)          |
|                                                  |
|--------------------------------------------------|
| IP Address: 93.184.216.34                        |
|--------------------------------------------------|
| Status: HTML content fetched successfully        |
-----------------------------------------------------
________________________________________
 Installation
 Requirements
•	Python 3.6 or newer
•	The following Python standard libraries:
o	tkinter
o	requests
o	socket
o	threading
o	urllib
Install requests if not already available:
pip install requests
________________________________________
 How to Run
Clone the repository or download the Python file.
bash
CopyEdit
git clone https://github.com/yourusername/web-scraper-gui.git
cd web-scraper-gui
python web_scraper_gui.py
________________________________________
 Code Breakdown
GUI Setup
python
CopyEdit
root = tk.Tk()
app = WebScraperApp(root)
root.mainloop()
Fetch HTML
python
CopyEdit
def fetch_html(self):
    url = self.url_entry.get().strip()
    thread = threading.Thread(target=self._fetch_html_thread, args=(url,))
    thread.start()
Fetch IP Address
python
CopyEdit
def _fetch_ip_thread(self, url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    ip = socket.gethostbyname(domain)
________________________________________
 File Structure
web_scraper_gui.py     # Main application script
README.md              # Project documentation
________________________________________
 Sample Use
•	Input: https://example.com
•	Output:
o	HTML source of the site
o	IP Address: 93.184.216.34
________________________________________





