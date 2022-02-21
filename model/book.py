from qt_core import *

class Book():
    def __init__(self, id, img, nome, qtd, autor, valor):
        self.id = id
        self.img = img
        self.nome = nome
        self.qtd = qtd
        self.autor = autor
        self.valor = valor
        
    def getBook(self):
        return [self.img, self.nome, self.qtd, self.autor, self.valor]
