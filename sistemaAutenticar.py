from typing import Optional
import PySide6.QtCore
from Ui_main import *
from Ui_login import *
from campos_de_usuario_logico import *
from PySide6.QtWidgets import QMessageBox, QMainWindow
from armazenar_produto import Info_Getter
from Ui_Esqueceu_Senha import Ui_Esqueceu_Senha
from UI_Cadastrar import Ui_Tela_Cadastrar
from sistemaPerfil import TelaPerfilFuncional
from Ui_Enviar_codigo import Ui_Enviar_Codigo
from Ui_Confirmar_Senha import Ui_Confirmar_Senha
from Ui_Recuperar_Senha import Ui_Recuperar_senha

class LoginSistemaAutenticar(QMainWindow, Ui_Tela_login):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
    
        
        self.btn_logar.clicked.connect(self.login)
        self.btn_esqueceusenha.clicked.connect(self.esqueceusenha)
        self.btn_cadastrar.clicked.connect(self.cadastrar)

        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.btn_logar.click() 


    def login(self):
        email_armazenado = ['@gmail.com', '@hotmail.com', '@yahoo.com', '']
        senha_armazenada = ['123','456', '789', '']

        email_digitado = self.input_emaillogin.text()
        senha_digitado = self.input_senhalogin.text()


#Verificando se o e-mail existe na lista email_armazenado
    
        if email_digitado in email_armazenado:
            
            index_email_lista = email_armazenado.index(email_digitado)

            # Verificando se a senha digitada possui o index na mesma posição do e-mail encontrado
            if senha_digitado == senha_armazenada[index_email_lista]:

                # Limpa as informações da tela de login
                self.input_emaillogin.clear()
                self.input_senhalogin.clear()
                  
                # Faz com que a tela main seja aberta, substituindo a janela de login 
                self.telamain = QMainWindow()
                self.ui_telamain = Ui_Main()
                self.ui_telamain.setupUi(self.telamain)

                self.checking_btn_Info_Gette = Info_Getter(self.ui_telamain)

                
                # Faz com que a main faça a troca de telas
                self.index = IndexChanger(self.ui_telamain)
                
                # Faz com que a tela de perfil seja funcional 
                self.perfil = TelaPerfilFuncional(self.ui_telamain)
                self.telamain.show()
                self.close()
                
                self.ui_telamain.btn_Sair.clicked.connect(self.closemain)
                
            else:

                QMessageBox.critical(self, 'Erro', 'Senha incorreta')
                self.input_senhalogin.clear()
               
        else:
        
            QMessageBox.critical(self, 'Erro', 'Usuário não Cadastrado')
            self.input_emaillogin.clear()
            self.input_senhalogin.clear()
            
    def esqueceusenha(self):
        self.tela_senha = QMainWindow()
        self.tela_senha_setup = Ui_Esqueceu_Senha()
        self.tela_senha_setup.setupUi(self.tela_senha)
        self.enviar_codigo()
        
        self.tela_senha.show() 
          
    def cadastrar(self):
        self.tela_cadastrar = QMainWindow()
        self.tela_cadastrar_setup = Ui_Tela_Cadastrar()
        self.tela_cadastrar_setup.setupUi(self.tela_cadastrar)
        self.tela_cadastrar.show()

    def enviar_codigo(self):
        self.ui_enviar = Ui_Enviar_Codigo()
        self.tela = QMainWindow()
        self.tela_senha_setup.btn_Enviar.clicked.connect(self.abrir_tela)
       
    def abrir_tela(self):
        self.ui_enviar.setupUi(self.tela)
        self.tela_senha.close()
        self.tela.show()
            
        self.recuperar_senha = Ui_Recuperar_senha() # recebe a classe da tela de recuperar senha
        self.ui_enviar.btn_enviar_codigo.clicked.connect(self.abrir_recuperar) # botão da tela de enviar codigo
        
    def abrir_recuperar(self): # def feita para executar/abrir a tela de recuperar a senha
        self.recuperar_senha.setupUi(self.tela)
        self.tela.close()
        self.tela.show()
        self.recuperar_senha.btn_recuperar_senha.clicked.connect(self.fechar_recuperar)
        
    def fechar_recuperar(self):
        self.tela.close()

    def closemain(self):
        self.telamain.close()
        self.show()