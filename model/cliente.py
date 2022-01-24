
class Cliente():
    def __init__(self, id, nome, tel, end, cpf):
        self.id = id
        self.nome = nome
        self.tel = tel
        self.end = end
        self.cpf = cpf

    def getSheet(self):
        return [self.nome, self.tel, self.end, self.cpf]
