from qt_core import *
from controller.cad_cliente import CadCliente
from controller.cliente_lista import ClienteList

class Home(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/home.ui', self)

        self.registro.clicked.connect(self.cadclient)

    def cadclient(self):
        self.cad_window = CadCliente()
        self.cad_window.show()

    def clientlist(self):
        self.client_window = ClienteList()
        self.client_window.show()

