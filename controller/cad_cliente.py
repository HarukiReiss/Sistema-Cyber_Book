from qt_core import *
from model.cliente import Cliente
import model.cliente_dao as cliente_dao

class CadCliente(QWidget):
    def __init__(self, cliente=None):
        super().__init__()
        uic.loadUi('view/cad_cliente.ui', self)

        self.cliente = cliente
        if cliente != False:
            self.load_cliente()

        self.excluir.hide()
        self.excluir.clicked.connect(self.delete)
        self.save.clicked.connect(self.salvar)

    def load_cliente(self):
        pass

    def salvar(self):
        try:
            nome = self.nome_edit.text()
            tel = int(self.tel_edit.text())
            end = self.end_edit.text()
            cpf = (self.cpf_edit.text())
            d1 = cpf[:3]
            d2 = cpf[3:6]
            d3 = cpf[6:9]
            d4 = cpf[9:]

            cpf_format = "{}.{}.{}-{}".format(d1,d2,d3,d4)
            if nome != '' and tel != '' and end != '' and cpf != '':
                if isinstance(tel, int) == True:
                    if len(str(tel)) == 11 and len(str(cpf)) == 11:
                        if self.cliente != False:
                            cliente_dao.add(Cliente(None, nome, tel, end, cpf_format))
                        else:
                            cliente_dao.edit(Cliente(self.moab.id, nome, tel, end, cpf_format))
                    else:
                        QMessageBox.about(self, "Número de Telefone e CPF inválidos. O requisito mínimo de digitos não foi atingido.")
                else:
                    QMessageBox.about(self, "Número de Telefone e CPF inválidos.")
            else:
                QMessageBox.about(self, "Insira todas as informações.")
        
        except Exception as e:
            QMessageBox.about(self, "Insira todas as informações.")
            print(e)

    def delete(self):
        pass


