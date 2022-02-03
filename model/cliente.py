from qt_core import *
class Cliente():
    def __init__(self, id, nome, tel, endereco, cpf):
        self.id = id
        self.nome = nome
        self.tel = tel
        self.endereco = endereco
        self.cpf = cpf

    def getData(self):
        return [self.nome, self.tel, self.endereco, self.cpf]
