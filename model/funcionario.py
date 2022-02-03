from qt_core import *
class Funcionario():
    def __init__(self, id, nickname, senha, email):
        self.id = id
        self.nickname = nickname
        self.senha = senha
        self.email = email
    
    def getUser(self):
        return [self.nickname, self.senha, self.email]
        
        