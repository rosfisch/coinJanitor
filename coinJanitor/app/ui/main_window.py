import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QStackedLayout, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("coinJanitor")
        self.setMinimumSize(800, 600)

        # create a stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # create all pages
        self.pages = {
            "nav": self._create_nav_page(),
            "page1": self._create_page_1(),
            "page2": self._create_page_2()
        }

        # add all pages to the stacked widget
        for page in self.pages.values():
            self.stacked_widget.addWidget(page)

        # show nav page by default
        self.stacked_widget.addWidget(self.pages["nav"])

    def _create_nav_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("NAv"))
        layout.addWidget(self._create_nav_button("Go to Page 1", "page1"))  
        layout.addWidget(self._create_nav_button("Go to Page 2", "page2"))  
        return page  
 
    def _create_nav_button(self, text, page_key):  
        btn = QPushButton(text)  
        # Connect button click to switching to the target page  
        btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.pages[page_key]))  
        return btn  
 
    def _create_page_1(self):  
        # Page 1 content (persistent reference in self.pages)  
        page = QWidget()  
        layout = QVBoxLayout(page)  
        layout.addWidget(QLabel("Page 1 Content (Persistent)"))  
        layout.addWidget(QPushButton("Back to Nav", clicked=lambda: self.stacked_widget.setCurrentWidget(self.pages["nav"])))  
        return page  
 
    def _create_page_2(self):  
        # Page 2 content (persistent reference in self.pages)  
        page = QWidget()  
        layout = QVBoxLayout(page)  
        layout.addWidget(QLabel("Page 2 Content (Persistent)"))  
        layout.addWidget(QPushButton("Back to Nav", clicked=lambda: self.stacked_widget.setCurrentWidget(self.pages["nav"])))  
        return page  

def get_greeting():
    daytime = datetime.now()
    if daytime.hour < 12:
        text = "Good morning sunshine!"
    elif daytime.hour < 18:
        text = "Good afternoon!"
    elif daytime.hour < 22:
        text = "Good evening you fanatic coin collector!"
    else:
        text = "You nightowl should better go to bed!"
    return QLabel(text)