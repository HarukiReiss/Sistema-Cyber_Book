from qt_core import *
class Book(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/book.ui', self)
        self.mainWindow = mainWindow

        self.tabela_livros.verticalHeader().setVisible(False)
        self.tabela_livros.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_livros.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.add_book_btn.clicked.connect(self.add_book)

    
    def add_book(self):
        self.mainWindow.showAdd()
