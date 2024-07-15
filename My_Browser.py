import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView() # Creates a QWebEngineView widget, which is a widget for displaying web content.
        self.browser.setUrl(QUrl('http://google.com')) # Sets the initial URL of the browser
        self.setCentralWidget(self.browser) # Sets the QWebEngineView widget as the central widget of the main window.
        self.showMaximized() # Maximizes the main window.

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back) #  Connects the 'triggered' signal of the action to the back method of the browser, which navigates back in the web history.
        navbar.addAction(back_btn) # Adds the 'Back' action to the toolbar.

        # Forward button
        forward_btn = QAction('Forward', self) # Creates an action named 'Forward' for the toolbar.
        forward_btn.triggered.connect(self.browser.forward) # Connects the 'triggered' signal of the action to the forward method of the browser, which navigates forward in the web history.
        navbar.addAction(forward_btn) # Adds the 'Forward' action to the toolbar.

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Updating the URL bar
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q): # Defines the update_url method, which updates the URL bar with the current URL of the browser.
        self.url_bar.setText(q.toString())# Sets the text of the URL bar to the current URL.

    def switch_to_mobile_mode(self):
        mobile_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
        self.browser.page().profile().setHttpUserAgent(mobile_agent) # Sets the user agent of the browser to the mobile user agent string.

    def switch_to_desktop_mode(self):
        desktop_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        self.browser.page().profile().setHttpUserAgent(desktop_agent)

    def switch_to_incognito_mode(self):
        # Note: This is a simplified version of incognito mode
        # Real incognito mode would not store any history, cookies, or cache
        self.browser.page().profile().setHttpUserAgent("incognito")

app = QApplication(sys.argv) # Creates an application object and initializes it with command-line arguments.
QApplication.setApplicationName('Abid Browser')
window = Browser()
app.exec_() # Enters the main loop of the application, waiting for events such as button clicks.
