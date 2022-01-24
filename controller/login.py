from qt_core import *

class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/login.ui', self)