from qt_core import *
class AddBook(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/add_book.ui', self)