from qt_core import *

class BookList(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/book_list.ui', self)