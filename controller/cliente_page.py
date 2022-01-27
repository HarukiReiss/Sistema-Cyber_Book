from qt_core import *
from model.cliente import Cliente
import model.cliente_dao as cliente_dao
class ClientePage(QWidget):
    c_list = []
    c_select = None
    def __init__(self):
        super().__init__()
        uic.loadUi('view/cliente.ui', self)
        
        self.remove_btn.hide()
        self.cancel_edit_btn.hide()
        self.remove_btn.clicked.connect(self.remover)
        self.save_btn.clicked.connect(self.salvar)
        self.tabela_clientes.verticalHeader().setVisible(False)
        self.tabela_clientes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_clientes.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.lupa.clicked.connect(self.buscar)
        self.cancel_edit_btn.clicked.connect(self.cancelEdit)
        
        self.load()
        self.tabela_clientes.clicked.connect(self.selectedC)

    def load(self):
        self.c_list = cliente_dao.selectAll()
        self.clearC()
        self.tabela_clientes.setRowCount(0)
        for cliente in self.c_list:
            self.add_cliente(cliente)

    def buscar(self):
        pass


    def remover(self):
        cliente_dao.delete(self.c_select.id)
        self.remove_btn.hide()
        self.cancel_edit_btn.hide()
        self.load()

        

    def salvar(self):
        try:
            nome = self.nome.text()
            telefone = str(self.telefone.text())
            endereco = self.endereco.text()
            cpf = str(self.cpf.text())
            d1 = cpf[:3]
            d2 = cpf[3:6]
            d3 = cpf[6:9]
            d4 = cpf[9:]

            f_cpf = "{}.{}.{}-{}".format(d1, d2, d3, d4)
            valid = QDoubleValidator(0, 100000000000, 0)
            if nome != '' and telefone != '' and endereco != '' and cpf != '':
                if valid.validate(telefone, 14)[0] == QValidator.Acceptable and valid.validate(cpf, 14)[0] == QValidator.Acceptable:
                    if len(str(telefone)) == 11 and len(str(cpf)) == 11:
                        if self.c_at == None:
                            cliente_dao.add(Cliente(None, nome, telefone, endereco, f_cpf))
                            self.load()
                        else:
                            cliente_dao.edit(Cliente(self.c_at.id, nome, telefone, endereco, f_cpf))
                            self.load()
                    else:
                        QMessageBox.about(self, "Erro!", "O número de telefone e CPF inválidos.")
                else:
                    QMessageBox.about(self, "Erro!", "Telefone e CPF apenas devem conter números.")
            else:
                QMessageBox.about(self, "Erro!", "Preencha todos os campos.")
            

        except Exception as e:
            QMessageBox.about(self, "Erro!", "Preencha todos os campos")
            print(e)
        self.remove_btn.hide()
        self.cancel_edit_btn.hide()


    def cancelEdit(self):
        self.clearC()
        self.remove_btn.hide()
        self.cancel_edit_btn.hide()

    def selectedC(self):
        self.remove_btn.show()
        self.cancel_edit_btn.show()

        row = self.tabela_clientes.currentRow()
        self.c_select = self.c_list[row]
        cpf_c = str(self.c_select.cpf)
        d1 = cpf_c[:3]
        d2 = cpf_c[4:7]
        d3 = cpf_c[8:11]
        d4 = cpf_c[12:]
        f_cpf = '{}{}{}{}'.format(d1, d2, d3, d4)
        tel_c = str(self.c_select.telefone)
        self.nome.setText(self.c_select.nome)
        self.telefone.setText(tel_c)
        self.endereco.setText(self.c_select.endereco)
        self.cpf.setText(f_cpf)

    def clearC(self):
        self.nome.clear()
        self.telefone.clear()
        self.endereco.clear()
        self.cpf.clear()
        self.c_select = None

    def add_cliente(self, cliente):
        rowCount = self.tabela_clientes.rowCount()
        self.tabela_clientes.insertRow(rowCount)


        id = QTableWidgetItem(str(cliente.id))
        nome = QTableWidgetItem(cliente.nome)
        telefone = QTableWidgetItem(str(cliente.telefone))
        endereco = QTableWidgetItem(cliente.endereco)
        cpf = QTableWidgetItem(cliente.cpf)

        self.tabela_clientes.setItem(rowCount, 0, id)
        self.tabela_clientes.setItem(rowCount, 1, nome)
        self.tabela_clientes.setItem(rowCount, 2, telefone)
        self.tabela_clientes.setItem(rowCount, 3, endereco)
        self.tabela_clientes.setItem(rowCount, 4, cpf)




        