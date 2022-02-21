from qt_core import *
import locale
import os
from controller.funcionario import Funcionario
from controller.book_page import BookPage
from controller.cliente_page import ClientePage
from controller.sale_page import NewSale
import model.sale_dao as sale_dao
import model.item_dao as item_dao

class MainWindow(QMainWindow):
    def __init__(self, logged, login):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.logged = logged
        self.login = login
        self.l = []
        self.funcionario_label.setText(logged+"!")
        self.clientes_btn.clicked.connect(self.showCliente)
        self.book_btn.clicked.connect(self.book)
        self.venda_btn.clicked.connect(self.venda)
        self.icon.clicked.connect(self.showMain)
        self.historic.verticalHeader().setVisible(False)
        self.historic.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.historic.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.historic.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.historic.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)

        menu = QMenu()
        self.more.setMenu(menu)
        act1 = menu.addAction('Editar Funcionário')
        act1.triggered.connect(self.edit_fun)
        self.act2 = menu.addAction('Sair')
        self.act2.triggered.connect(self.exit)
        self.loadSellers()

    def showMain(self):
        item_dao.removeNull
        self.tabela.setCurrentIndex(0)
        self.loadSellers

    def showCliente(self):
        item_dao.removeNull
        self.tabela.insertWidget(1, ClientePage())
        self.tabela.setCurrentIndex(1)

    def exit(self):
        self.login.show()
        self.hide()

    def edit_fun(self):
        item_dao.removeNull
        self.tabela.insertWidget(2, Funcionario(self.logged))
        self.tabela.setCurrentIndex(2)

    def book(self):
        item_dao.removeNull
        self.tabela.insertWidget(3, BookPage(self))
        self.tabela.setCurrentIndex(3)

    def venda(self):
        item_dao.removeNull
        self.tabela.insertWidget(4, NewSale(self.logged, self))
        self.tabela.setCurrentIndex(4)
    
    def loadSellers(self):
        self.l = sale_dao.selectAll()
        self.historic.setRowCount(0)
        for s in self.l:
            self.addSale(s)
        for l in range(self.historic.rowCount()):
            if self.historic.rowCount() > -1:
                button = QPushButton(self.historic)
                button.setText('. . .')
                button.setGeometry(30, 30, 30, 30)
                button.setFixedSize(30, 30)
                button.setToolTip('Ver detalhes...')
                button.setCursor(Qt.PointingHandCursor)
                button.clicked.connect(self.show_more)
                self.historic.setCellWidget(l, 6, button)
    
    def addSale(self, s):
        locale.setlocale(locale.LC_ALL, '')
        row = self.historic.rowCount()
        self.historic.insertRow(row)
        list = item_dao.selectOne(s.id)
        pay = locale.currency(s.valor, grouping=True)
        id = QTableWidgetItem(str(s.id))
        funcionario = QTableWidgetItem(s.funcionario)
        cliente = QTableWidgetItem(s.cliente)
        qtd_book = QTableWidgetItem(str(len(list)))
        valor = QTableWidgetItem(str(pay))

        self.historic.setItem(row, 0, id)
        self.historic.setItem(row, 1, funcionario)
        self.historic.setItem(row, 2, cliente)
        self.historic.setItem(row, 3, qtd_book)
        self.historic.setItem(row, 4, valor)
        self.historic.setItem(row, 5, QTableWidgetItem(s.info))
    
    def show_more(self):
        locale.setlocale(locale.LC_ALL, '')
        row = self.historic.currentRow()
        l = self.historic.item(row, 0).text()
        sl = item_dao.selectOne(l)
        p = self.historic.item(row, 4).text()
        ls = []
        for li in sl:
            str = f"Nome: {li.book_nome}\n Quantidade: {li.qtd}\n Valor: {locale.currency(li.book_price, grouping=True)}\n"
            ls.append(str)

        ls_form = '\n'.join(ls)
        QMessageBox.information(self, 'Lista de Livros', f"{ls_form}")


        
        
