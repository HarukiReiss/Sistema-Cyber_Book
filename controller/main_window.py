from qt_core import *
from controller.home import Home
from controller.book_list import BookList

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.status.hide()
        self.home = Home()
        self.book_list = BookList()

        self.painel_widget.insertWidget(0, self.home)
        self.painel_widget.insertWidget(1, self.book_list)

        self.show_home()

        self.home_btn.clicked.connect(self.show_home)
        self.list_btn.clicked.connect(self.show_list)

    def show_home(self):
        self.painel_widget.setCurrentIndex(0)
    
    def show_list(self):
        self.painel_widget.setCurrentIndex(1)