from qt_core import *
class Funcionario(QWidget):
    def __init__(self, logged):
        super().__init__()
        uic.loadUi('view/funcionario.ui', self)

        self.logged = logged

