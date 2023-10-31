from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, 
QLineEdit,QApplication,QFormLayout,QWidget)
import sys
import smtplib
import secrets
class Mainwindow_senha(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('esqueceu senha ')
        self.setFixedSize(QSize(500,600))
        
        self.input_email=QLineEdit(self)
        self.email=self.input_email
        
        self.btn_trocar_senha=QPushButton(self)
        self.btn_trocar_senha.setText('Eviar Código')
        self.btn_trocar_senha.clicked.connect(self.trocar)
        self.btn_trocar_senha.clicked.connect(self.enviar_email)
        
        
        
        self.pagina=QFormLayout(self)
        self.pagina.addRow('Email = ',self.input_email)
        self.pagina.addRow(self.btn_trocar_senha)
        widgetFORmulario = QWidget(self)
        widgetFORmulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFORmulario)
        

    def trocar(self):
        lista_email=['thiagocassiano63991@gmail.com']
        
        if self.email.text() in lista_email:
            self.input_codigo=QLineEdit(self)
            self.input_trocar_senha=QLineEdit(self)
            self.btn_nova_senha=QPushButton(self)
            self.btn_nova_senha.setText('Atualizar Nova Senha')
            self.btn_nova_senha.clicked.connect(self.aviso_troca)
            self.pagina=QFormLayout(self)
            self.pagina.addRow('Código = ',self.input_codigo)
            self.pagina.addRow('Troca Senha = ',self.input_trocar_senha)
            self.pagina.addRow(self.btn_nova_senha)
            widgetFORmulario = QWidget()
            widgetFORmulario.setLayout(self.pagina)
            self.setCentralWidget(widgetFORmulario)
        else:
            self.lbl_erro=QLabel(self)
            self.pagina=QFormLayout(self)
            self.pagina.addRow('Email inválido',self.lbl_erro)
            widgetFORmulario = QWidget()
            widgetFORmulario.setLayout(self.pagina)
            self.setCentralWidget(widgetFORmulario)
            print('trocar erro')

    def aviso_troca(self):
        lista_codigo=[self.codigo]
        if self.input_codigo.text() in lista_codigo:
            self.lbl_aviso_troca=QLabel(self)
            self.lbl_aviso_troca.setText('Senha alterada com sucesso')
            self.pagina=QFormLayout(self)
            self.pagina.addRow(self.lbl_aviso_troca)
            widgetFORmulario = QWidget()
            widgetFORmulario.setLayout(self.pagina)
            self.setCentralWidget(widgetFORmulario)
        else:
            self.lbl_erro=QLabel(self)
            self.pagina=QFormLayout(self)
            self.pagina.addRow('Código Inválido',self.lbl_erro)
            widgetFORmulario = QWidget()
            widgetFORmulario.setLayout(self.pagina)
            self.setCentralWidget(widgetFORmulario)

    def enviar_email(self):
        self.codigo=(secrets.token_urlsafe(10))
        try:
            #definindo o servidor
            self.servidor = smtplib.SMTP('smtp.gmail.com', 587)

            #iniciando o servidor
            self.servidor.starttls()

            #logando
            self.servidor.login('estoquemedicohub@gmail.com', 'pifs imrb vvyo kdah')

            #montando o email
            self.remetente = 'estoquemedicohub@gmail.com'
            self.destinatarios = ['thiagocassiano63991@gmail.com']
            self.mensagem = self.codigo

            #enviando o email
            self.servidor.sendmail(self.remetente, self.destinatarios, self.mensagem)
        except Exception as error:
            print(f"Erro ao enviar o email --> {error}")
        finally:
            #encerrando a conexao do servidor
            self.servidor.quit()   