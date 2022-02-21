from qt_core import *
import model.book_dao as book_dao
from model.book import Book
import locale
import os

class BookPage(QWidget):
    book_list = []
    s_book = None
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/book.ui', self)

        self.mainWindow = mainWindow
        self.img = None
        self.remove.hide()
        self.cancel.hide()
        self.remove.clicked.connect(self.delete)
        self.cancel.clicked.connect(self.cancelEdit)
        self.add_book.clicked.connect(self.save)
        self.validator = QDoubleValidator(0.00, 9999.00, 2, notation=QDoubleValidator.StandardNotation)
        self.book_price.setValidator(self.validator)
        self.book_price.textChanged.connect(self.formated)
        self.img_select.clicked.connect(self.imageSet)
        self.img_icon.setPixmap(QPixmap('assets/icons/set.jpg'))

        self.book_qtd.setValue(1)
        self.tabela_livros.verticalHeader().setVisible(False)
        self.tabela_livros.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_livros.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tabela_livros.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.tabela_livros.clicked.connect(self.select)
        self.load()

    def formated(self):
        self.validator.validate(self.book_price.text(), 14)[0]

    def cancelEdit(self):
        self.clear()
        self.remove.hide()
        self.cancel.hide()
    
    def save(self):
        nome = self.book_name.text()
        qtd = self.book_qtd.text()
        autor = self.escritor.text()
        valor = self.book_price.text()
        try:
            if nome != '' and qtd != '' and valor != '':
                if self.validator.validate(valor, 14)[0] == QValidator.Acceptable:
                    price = valor.replace(',','.')
                    if self.s_book != None:
                        book_dao.editBook(Book(self.s_book.id, self.img, nome, qtd, autor, valor))
                        self.load()
                    else:
                        book_dao.addBook(Book(None, self.img, nome, qtd, autor, valor))
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
        for book in self.book_list:
            self.painel(book)

    def delete(self):
        book_dao.removeBook(self.s_book.id)
        self.remove.hide()
        self.cancel.hide()
        self.load()    

    def painel(self, book):
        locale.setlocale(locale.LC_ALL, '')
        rowCount = self.tabela_livros.rowCount()
        self.tabela_livros.insertRow(rowCount)
        valor_livro = locale.currency(book.valor, grouping=True)

        id = QTableWidgetItem(str(book.id))
        nome = QTableWidgetItem(book.nome)
        autor = QTableWidgetItem(book.autor)
        qtd = QTableWidgetItem(str(book.qtd))
        price = QTableWidgetItem(str(valor_livro))

        self.tabela_livros.setItem(rowCount, 0, id)
        self.tabela_livros.setItem(rowCount, 1, nome)
        self.tabela_livros.setItem(rowCount, 2, autor)
        self.tabela_livros.setItem(rowCount, 3, qtd)
        self.tabela_livros.setItem(rowCount, 4, price)
    
    def select(self):
        self.cancel.show()
        self.remove.show()
        row = self.tabela_livros.currentRow()
        self.s_book = self.book_list[row]
        if self.s_book.img == None:
            self.img_icon.setPixmap(QPixmap('assets/icons/set.jpg'))
        else:
            self.img_icon.setPixmap(QPixmap(self.s_book.img))
        self.book_name.setText(self.s_book.nome)
        self.escritor.setText(self.s_book.autor)
        self.book_qtd.setValue(self.s_book.qtd)
        self.book_price.setText(str(self.s_book.valor))

    def clear(self):
        self.img_icon.setPixmap(QPixmap('assets/icons/set.jpg'))
        self.book_name.clear()
        self.escritor.clear()
        self.book_qtd.clear()
        self.book_price.clear()
        self.s_book = None
    
    def imageSet(self):
        filtro = 'File (*.jpg, *.jpeg, *.png)'
        picture = QFileDialog.getOpenFileName(self, "Escolha a imagem de capa", os.getcwd(), filtro)
        self.img = picture[0]
        if self.img != '':
            self.img_icon.setPixmap(QPixmap(self.img))
    

    
