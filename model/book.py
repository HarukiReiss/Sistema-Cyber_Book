from qt_core import *

class Book():
    def __init__(self, id, nome, qtd, valor):
        self.id = id
        self.nome = nome
        self.qtd = qtd
        self.valor = valor
        
    def getBook(self):
        return [self.nome, self.qtd, self.valor]