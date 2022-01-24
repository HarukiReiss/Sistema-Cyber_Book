from qt_core import *
from model.cliente import Cliente
from controller.cad_cliente import CadCliente
import model.cliente_dao as cliente_dao

class ClienteList(QWidget):

    lc = []
    moab = None

    def __init__(self):
        super().__init__()
        uic.loadUi('view/cliente_lista.ui', self)

        self.tabela_cliente.verticalHeader().setVisible(False)
        self.tabela_cliente.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_cliente.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        self.load()
        self.tabela_cliente.clicked.connect(self.boom)

    def load(self, cliente):
        self.lc = cliente_dao.selectAll()
        self.tabela_cliente.setRowCount(0)
        for c in self.lc:
            self.add_cliente(cliente)

    def boom(self):
        self.editcliente = CadCliente()
        self.editcliente.show

    def add_cliente(self, cliente):
        rowCount = self.tabela_cliente.rowCount()
        self.tabela_cliente.insertRow(rowCount)

        id = QTableWidgetItem(str(cliente.id))
        nome = QTableWidgetItem(cliente.nome)
        telefone = QTableWidgetItem(str(cliente.telefone))
        endereco = QTableWidgetItem(cliente.endereco)
        cpf = QTableWidgetItem(cliente.cpf)

        self.tabela_cliente.setItem(rowCount, 0, id)
        self.tabela_cliente.setItem(rowCount, 1, nome)
        self.tabela_cliente.setItem(rowCount, 2, telefone)
        self.tabela_cliente.setItem(rowCount, 3, endereco)
        self.tabela_cliente.setItem(rowCount, 4, cpf)





