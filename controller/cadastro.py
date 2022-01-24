from qt_core import *

class Cadastrar(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/cadastro.ui', self)