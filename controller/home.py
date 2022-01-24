from qt_core import *
from controller.cad_cliente import CadCliente
from controller.cliente_lista import ClienteList
from controller.login import Login
from controller.cadastro import Cadastrar
from controller.book_list import BookList
from controller.add_book import AddBook

class Home(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/home.ui', self)

        self.registro.clicked.connect(self.cadclient)
        self.lista.clicked.connect(self.clientlist)
        self.login.clicked.connect(self.log)
        self.cadastro.clicked.connect(self.reg)
        self.historic.clicked.connect(self.hist)
        self.nova_venda.clicked.connect(self.new_sale)
        self.list.clicked.connect(self.lista_livro)
        self.editar.clicked.connect(self.book_edit)

    def cadclient(self):
        self.cad_window = CadCliente()
        self.cad_window.show()

    def clientlist(self):
        self.client_window = ClienteList()
        self.client_window.show()
    
    def log(self):
        self.logon = Login
        self.logon.show()

    def reg(self):
        self.reg_window = Cadastrar
        self.reg_window.show()
    
    def hist(self):
        pass

    def new_sale(self):
        pass

    def lista_livro(self):
        self.book_window = BookList()
        self.book_window.show()

    def book_edit(self):
        self.add_book = AddBook
        self.add_book.show()

