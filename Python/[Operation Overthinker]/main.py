import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QVBoxLayout, QWidget, QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the address bar (line edit)
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_page)

        # Create the web view
        self.web_view = QWebEngineView()

        # Create a vertical layout for the web view and address bar
        layout = QVBoxLayout()
        layout.addWidget(self.address_bar)
        layout.addWidget(self.web_view)

        # Create a central widget to hold the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.show()

    def load_page(self):
        url = QUrl(self.address_bar.text())
        self.web_view.load(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
