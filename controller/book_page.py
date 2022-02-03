from qt_core import *
import model.book_dao as book_dao
from model.book import Book
import locale

class Book(QWidget):
    book_list = []
    s_book = None
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/book.ui', self)
        self.mainWindow = mainWindow
        self.remove.hide()
        self.cancel.hide()
        self.remove.clicked.connect(self.delete)
        self.cancel.clicked.connect(self.cancelEdit)
        self.add_book.clicked.connect(self.save)




        self.tabela_livros.verticalHeader().setVisible(False)
        self.tabela_livros.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_livros.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tabela_livros.clicked.connect(self.select)
        self.load()

    def cancelEdit(self):
        self.clear()
        self.remove.hide()
        self.cancel.hide()
    
    def save(self):
        nome = self.book_name.text()
        qtd = self.book_qtd.text()
        valor = self.book_price.text()
        price = QDoubleValidator(0, float('inf'), 0)
        try:
            if nome != '' and qtd != '' and valor != '':
                if price.validate(valor, 14)[0] == QValidator.Acceptable:
                    if self.s_book != None:
                        book_dao.editBook(Book(self.s_book.id, nome, qtd, valor))
                        self.load()
                    else:
                        book_dao.addBook(Book(None, nome, qtd, valor))
                        self.load()
                else:
                    QMessageBox.warning(self, "Erro!", "Apenas números inteiros são válidos.")
            else:
                QMessageBox.warning(self, "Erro!", "Preencha todos os campos.")
        except Exception as s:
            print(s)
    
    def load(self):
        self.book_list = book_dao.selectAll()
        self.clear()
        self.tabela_livros.setRowCount(0)
        for livro in self.book_list:
            self.painel(livro)

    def delete(self):
        book_dao.delBook(self.s_book.id)
        self.remove.hide()
        self.cancel.hide()
        self.load()
    

    def painel(self, livro):
        locale.setlocale(locale.LC_ALL, '')
        rowCount = self.tabela_livros.rowCount()
        self.tabela_livros.insertRow(rowCount)
        valor_livro = locale.currency(livro.valor, grouping=True)

        id = QTableWidgetItem(str(livro.id))
        nome = QTableWidgetItem(livro.nome)
        qtd = QTableWidgetItem(str(livro.quantidade))
        valor = QTableWidgetItem(str(valor_livro))

        self.tabela_livros.setItem(rowCount, 0, id)
        self.tabela_livros.setItem(rowCount, 1, nome)
        self.tabela_livros.setItem(rowCount, 2, qtd)
        self.tabela_livros.setItem(rowCount, 3, valor)
    
    def select(self):
        self.cancel.show()
        self.remove.show()
        row = self.tabela_livros.currentRow()
        self.s_book = self.book_list[row]
        self.book_name.setText(self.s_book.nome)
        self.book_qtd.setValue(self.s_book.quantidade)
        self.book_price.setText(self.s_book.valor)

    def clear(self):
        self.book_name.clear()
        self.book_qtd.clear()
        self.book_price.clear()
        self.s_book = None

    

    
