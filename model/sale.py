from qt_core import *

class Sale():
    def __init__(self, id, cliente, funcionario, valor, info):
        self.id = id
        self.cliente = cliente
        self.funcionario = funcionario
        self.valor = valor
        self.info = info
        
    def getSale(self):
        return [self.cliente, self.funcionario, self.valor, self.info]
