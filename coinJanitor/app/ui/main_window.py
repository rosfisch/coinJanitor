import sys
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow, QLabel, QStackedWidget
from PyQt6.QtGui import QPixmap
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
            "page2": self._create_settings_page()
        }

        # add all pages to the stacked widget
        for page in self.pages.values():
            self.stacked_widget.addWidget(page)

        # show nav page by default
        self.stacked_widget.addWidget(self.pages["nav"])

    def _create_nav_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        greeting = QLabel(get_greeting())
        greeting.setStyleSheet("""color: white;
                                font-size: 35px;
                                font-weight: bold;
                                font-family: Inter;""")
        layout.addWidget(greeting)

        # add the setting button
        box_set = QWidget()
        box_set.setStyleSheet("""background-color: #7B0527; padding: 10px; margin: 25px;""")
        box_set_layout = QVBoxLayout(box_set)
        label_set = QLabel()
        pixmap = QPixmap('settings.png')
        label_set.setPixmap(pixmap)
        box_set_layout.addWidget(label_set)
        box_set_layout.addWidget(self._create_nav_button("", "page2"))
        layout.addWidget(box_set)

        '''
        bottomBtn = QPushButton(
            icon=QIcon("./icons/logo.svg"),
            text="Bottom",
            parent=self
        )
        '''

        # box for the current balance
        box = QWidget()
        box.setStyleSheet("""background-color: #D0FF26; border-radius: 15px; padding: 10px; margin: 25px;""")
        box_layout = QVBoxLayout(box)
        total_bal_Label = QLabel("Total Balance")
        total_bal_Label.setStyleSheet("""color: black;
                                            font-size: 25px;
                                            font-family: Comfortaa;""")
        box_layout.addWidget(total_bal_Label)
        layout.addWidget(box)

        # box that lists the coins
        box = QWidget()
        box.setStyleSheet("""background-color: #7B0527; border-radius: 15px; padding: 10px; margin: 25px;""")
        box_layout = QVBoxLayout(box)
        box_layout.addWidget(QLabel("COIN Collection"))
        box_layout.addWidget(self._create_nav_button("See all", "page1"))
        layout.addWidget(box)

        
        return page  
 
    def _create_nav_button(self, text, page_key):  
        btn = QPushButton(text) 
        btn.setStyleSheet("""color: white;""")
        btn.setToolTip("Click to see the whole collection")
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
 
    def _create_settings_page(self):  
        # Page 2 content (persistent reference in self.pages)  
        page = QWidget()  
        layout = QVBoxLayout(page)  
        layout.addWidget(QLabel("Settings")) 
        #<--------------------> box for the import of a csv
        box = QWidget()
        exportBtn = QPushButton("Export CSV")
        exportBtn.setStyleSheet("backround-color: #D0FF26")
        exportBtn.clicked.connect(self.onClick)
        # TODO add the export logic and the buttonOnClick event
        #layout.addWidget(QPushButton("Export CSV", clicked=lambda: self.stacked_widget.setCurrentWidget(self.pages["nav"]))) 

        # TODO add the import logic and the buttonOnClick event
        importBtn = QPushButton("Import CSV")
        importBtn.setStyleSheet("""background-color: #D0FF26""")
        layout.addWidget(QPushButton("Import CSV", clicked=lambda: self.stacked_widget.setCurrentWidget(self.pages["nav"]))) 
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
    return text

# TODO calc the total balance
def balance_calc():
    QLabel = "Total Balance"