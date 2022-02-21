from qt_core import *
from controller.main_window import MainWindow
from model.funcionario import Funcionario
import model.funcionario_dao as fun_dao
class Login(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/login.ui', self)


        self.senha.setEchoMode(QLineEdit.Password)
        self.label_email.hide()
        self.email.hide()
        self.cad_btn.hide()
        self.cancel_btn.hide()
        self.enter_btn.clicked.connect(self.test)
        self.regis_btn.clicked.connect(self.regis)
        self.cad_btn.clicked.connect(self.cad)
        self.cancel_btn.clicked.connect(self.cancel)

    
    def test(self):
        user = self.usuario.text()
        key = self.senha.text()
        try:
            if user == '' and key == '':
                QMessageBox.about(self, "Erro!", "Insira os dados.")
            else:
                login = fun_dao.logon(user, key)
                if login == None:
                    QMessageBox.about(self, "Erro!", "Usuário ou senha incorretos.")
                else:
                    QMessageBox.about(self, "Acesso aceito!", "Login bem sucedido.")
                    logged = user
                    self.mainWindow = MainWindow(logged, self)
                    self.mainWindow.show()
                    
                    self.hide()
        except Exception as e:
            print(e)


    def cad(self):
        try:
            user = self.usuario.text()
            senha = self.senha.text()
            email = self.email.text()
            
            valid = QDoubleValidator(0, 100000000, 0)
            if user != '' and email != '':
                exist = fun_dao.selectOne(user)
                if exist == None:
                    if valid.validate(senha, 14)[0] == QValidator.Acceptable:
                        if len(str(senha)) >= 8:
                            fun_dao.regis(Funcionario(None, user, senha, email))
                            self.cad_btn.hide()
                            self.regis_btn.show()
                            self.enter_btn.show()
                            self.email.hide()
                            self.label_email.hide()
                            self.cancel_btn.hide()
                            self.usuario.clear()
                            self.senha.clear()
                            self.email.clear()
                        else:
                            QMessageBox.about(self, "Erro!", "A senha está muito fraca.")
                    else:
                        QMessageBox.about(self, "Erro!", "Senha inválida.")
                else:
                    QMessageBox.warning(self, "Erro!", "Conta já existente.")
            else:
                QMessageBox.warning(self, "Erro!", "Preencha todos os campos.")
        except Exception as e:
            print(e)
        
    
    def regis(self):
        self.enter_btn.hide()
        self.regis_btn.hide()
        self.cad_btn.show()
        self.label_email.show()
        self.email.show()
        self.cancel_btn.show()
    
    def cancel(self):
        self.cancel_btn.hide()
        self.label_email.hide()
        self.email.hide()
        self.cad_btn.hide()
        self.enter_btn.show()
        self.regis_btn.show()