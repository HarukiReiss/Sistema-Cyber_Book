
class Funcionario():
    def __init__(self, id, nome, senha, email):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.email = email

    def getUser(self):
        return [self.nome, self.senha, self.email]
