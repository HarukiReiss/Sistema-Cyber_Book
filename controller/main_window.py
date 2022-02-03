from controller.funcionario import Funcionario
from controller.book_page import Book
from qt_core import *
from controller.cliente_page import ClientePage
from controller.sale_page import NewSale
class MainWindow(QMainWindow):
    def __init__(self, logged):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.logged = logged

        self.funcionario_label.setText(logged+"!")
        self.clientes_btn.clicked.connect(self.showCliente)
        self.book_btn.clicked.connect(self.book)
        self.venda_btn.clicked.connect(self.venda)

        menu = QMenu()
        self.more.setMenu(menu)
        act1 = menu.addAction('Editar Funcionário')
        act1.triggered.connect(self.edit_fun)
        act2 = menu.addAction('Sair')
        act2.triggered.connect(self.exit)

    def showMain(self):
        self.tabela.setCurrentIndex(0)

    def showCliente(self):
        self.tabela.insertWidget(1, ClientePage())
        self.tabela.setCurrentIndex(1)

    def exit(self):
        pass

    def edit_fun(self):
        self.tabela.insertWidget(2, Funcionario(self.logged))
        self.tabela.setCurrentIndex(2)

    def book(self):
        self.tabela.insertWidget(3, Book(self))
        self.tabela.setCurrentIndex(3)

    def venda(self):
        self.tabela.insertWidget(4, NewSale(self.logged, self))
        self.tabela.setCurrentIndex(4)
        

        
        
