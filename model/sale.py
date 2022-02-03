from qt_core import *

class Sale():
    def __init__(self, id, cliente, funcionario, valor, livros_venda=[]):
        self.id = id
        self.cliente = cliente
        self.funcionario = funcionario
        self.valor = valor
        self.livros_venda = livros_venda
        
    def getSale(self):
        return [self.cliente, self.funcionario, self.valor]

    def getSellers(self):
        new_list = []
        self.livros_venda.extend(new_list)
        return [new_list]