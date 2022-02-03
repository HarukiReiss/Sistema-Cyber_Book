from qt_core import *
import locale
import model.cliente_dao as cd
import model.book_dao as bd
import model.item_dao as ld
import model.sale_dao as vd
from model.sale import Sale
from model.item import Livro
from model import database

class NewSale(QWidget):
    def __init__(self, logged, mainWindow):
        super().__init__()
        uic.loadUi('view/nova_venda.ui', self)

        self.mainWindow = mainWindow
        self.booklist = None
        self.list = None
        self.itemlist = []
        self.itemidlist = []
        self.s_cliente = None
        self.s_item = None
        self.s_livro = None
        self.price = None
        self.full_price = 0
        self.logged = logged
        self.sale_fun.setText(logged)
        self.total_price.setText("R$ 0,00")
        self.book_price.setText("R$ 0,00")
        self.troco.setText("R$ 0,00")
        self.tabela_venda.verticalHeader().setVisible(False)
        self.tabela_venda.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_venda.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.remove_sale.setEnabled(False)
        self.add_sale.setEnabled(False)
        self.insert.setEnabled(False)
        self.finalizar.setEnabled(False)
        self.cancel_sale.hide()
        self.add_sale.clicked.connect(self.addLivro)
        self.pagamento.currentIndexChanged.connect(self.pay)
        self.insert.clicked.connect(self.addm)
        self.tabela_venda.clicked.connect(self.sbook)
        self.remove_sale.clicked.connect(self.removeBook)
        self.cancel_sale.clicked.connect(self.cancelBook)
        self.finalizar.clicked.connect(self.finish)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start()
        self.load()
        self.load_book()

    def finish(self):
        try:
            if self.s_cliente != None:
                vd.add(Sale(None, self.s_cliente.nome, self.logged, self.full_price, self.itemlist))
                QMessageBox.information(self, "Concluído!", "Compra executada com êxito.")
                sale_id = vd.selectHistoric()
                for saleid in self.itemidlist:
                    conn = database.connect()
                    cursor = conn.cursor()
                    sql = f"""UPDATE SaleBook SET sale_id={sale_id[0]} WHERE id=?"""
                    cursor.execute(sql, [saleid])
                    conn.commit()
                    conn.close()
                self.mainWindow.showMain()
            else:
                QMessageBox.warning(self, "Erro!", "Selecione um cliente.")
        except Exception as v:
            print(v)

    def pay(self):
        if self.pagamento.currentIndex() == 1:
            self.troco.hide()
            self.label_10.hide()
            self.pagamento.setTitle("Crédito")
        else:
            self.troco.show()
            self.label_10.show()
            self.pagamento.setTitle("Débito")
    
    def load(self):
        self.list = cd.selectAll()
        o = 0
        for c in self.list:
            self.sale_cliente.addItem(c.nome)
            o += 1
        self.sale_cliente.currentIndexChanged.connect(self.selectedCliente)

    def load_book(self):
        self.booklist = bd.selectAll()
        o = 0
        for b in self.booklist:
            self.book_box.addItem(b.nome)
            o += 1
        self.book_box.currentIndexChanged.connect(self.selectedBook)

    def load_livro(self):
        count = 0
        self.tabela_venda.setRowCount(0)
        for item in self.itemlist:
            count += 1
            self.tabela(item, count)

    def addLivro(self, index):
        locale.setlocale(locale.LC_ALL, '')
        id_item = self.s_item.id
        nome = self.s_item.nome
        qtd = self.qtd_item.value()
        valor = self.s_item.valor*qtd

        ld.add(Livro(None, id_item, nome, qtd, valor))
        sale_id = ld.selectSale()
        self.itemlist.append(Livro(sale_id[0][0], id_item, nome, qtd, valor))
        self.itemidlist.append(sale_id=[0][0])
        self.full_price += valor
        f_valor = locale.currency(self.full_price, grouping=True)
        self.total_price.setText(f_valor)
        self.finalizar.setEnabled(True)
        self.load_livro()

    def cancelBook(self):
        self.remove_sale.setEnabled(False)
        self.cancel_sale.hide()
        self.add_sale.setEnabled(True)
        self.book_box.setEnabled(True)
        self.book_qtd.setEnabled(True)
        self.book_price.setEnabled(True)
        self.s_livro = None

    def removeBook(self):
        locale.setlocale(locale.LC_ALL, '')
        self.full_price -= self.s_livro.livro_price
        self.total_price.setText(locale.currency(self.full_price, grouping=True))
        ld.remove(self.s_livro.id)
        self.itemlist.remove(self.s_livro)
        self.remove_sale.setEnabled(False)
        self.cancel_sale.hide()
        self.add_sale.setEnabled(True)
        self.book_box.setEnabled(True)
        self.book_qtd.setEnabled(True)
        self.book_price.setEnabled(True)
        self.load_livro()

    def tabela(self, item, count):
        locale.setlocale(locale.LC_ALL, '')
        row = self.tabela_venda.rowCount()
        self.tabela_venda.insertRow(row)

        price_livro = locale.currency(item.livro_price, grouping=True)
        qtd_livro = QTableWidgetItem(str(count))
        id = QTableWidgetItem(str(item.livro_id))
        nome = QTableWidgetItem(item.livro_nome)
        qt = QTableWidgetItem(str(item.livro_qtd))
        valor = QTableWidgetItem(str(price_livro))

        self.tabela_venda.setItem(row, 0, qtd_livro)
        self.tabela_venda.setItem(row, 1, id)
        self.tabela_venda.setItem(row, 2, nome)
        self.tabela_venda.setItem(row, 3, qt)
        self.tabela_venda.setItem(row, 4, valor)
        self.clear()

    def clear(self):
        self.book_qtd.setValue(1)
        self.book_price.setText("R$ 0")

    def selectedCliente(self, index):
        if self.sale_cliente.currentText() != "Selecione o Cliente":
            self.s_cliente = self.list[index]

    def selectedBook(self, index):
        locale.setlocale(locale.LC_ALL, '')
        if self.book_box.currentText() != "Selecione o Livro":
            self.add_sale.setEnabled(True)
            self.s_item = self.itemlist[index]
            self.price = locale.currency(self.s_item.sale_price, grouping=True)
            self.book_price.setText(str(self.price))
        else:
            self.book_price.setText("R$ 0,00")
            self.add_sale.setEnabled(False)

    def sbook(self):
        self.remove_sale.setEnabled(True)
        self.cancel_sale.show()
        self.add_sale.setEnabled(False)
        self.book_box.setEnabled(False)
        self.book_qtd.setEnabled(False)
        self.book_price.setEnabled(False)
        row = self.tabela_venda.currentRow()
        self.s_livro = self.itemlist[row]

    def addm(self):
        locale.setlocale(locale.LC_ALL, '')
        if self.full_price != 0:
            received_pay = int(self.recebido.text())
            restante = 0
            restante += received_pay
            falta = self.full_price - restante
            troco = restante - self.full_price
            troco_real = locale.currency(troco, grouping=True)
            self.troco.setText(troco_real)
        else:
            QMessageBox.warning(self, "Alerta!", "Nenhum produto foi adicionado.")

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString("hr:mn:sc")
        self.data.setText(text)
