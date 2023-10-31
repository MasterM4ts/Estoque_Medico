from produto_list import Product
from PySide6.QtWidgets import QMessageBox

class Info_Getter():
    def __init__(self,ui):
    
        self.ui = ui
        self.ui.btn_registrar_product.clicked.connect(self.product_save)
        
    def product_save(self):
        
        if self.ui.inp_nome_product.text() != "":
          self.prod_nome = self.ui.inp_nome_product.text()
          
        elif self.ui.inp_nome_product.text() == "":
            self.ui.inp_nome_product.clear()
            self.Message_Error()
            
        if self.ui.inp_marca_product.text() != "":    
            self.prod_marca = self.ui.inp_marca_product.text()
            
        elif self.ui.inp_marca_product.text() == "":
            self.ui.inp_marca_product.clear()
            self.Message_Error()
       
        if self.ui.inp_quantidade_product.text() != "":
            try:
                self.prod_quantidade = int(self.ui.inp_quantidade_product.text())
            except:
                self.Message_Error()
                
        elif self.ui.inp_quantidade_product.text() == "":
            self.ui.inp_quantidade_product.clear()
            self.Message_Error()
        
        if self.ui.inp_descricao_product.text() != "":    
            self.prod_descricao = self.ui.inp_descricao_product.text()  
       
        elif self.ui.inp_descricao_product.text() == "":
            
            self.ui.inp_descricao_product.clear()
            self.Message_Error()
            
        try: 
            self.prod_info = Product(self.prod_nome, self.prod_marca, self.prod_quantidade, self.prod_descricao)           
          
            self.ui.inp_nome_product.clear()
            self.ui.inp_marca_product.clear()
            self.ui.inp_descricao_product.clear()
            self.ui.inp_quantidade_product.clear()
            
            del self.prod_nome
            del self.prod_marca
            del self.prod_quantidade
            del self.prod_descricao
            
        except:
            pass
        
        
    def Message_Error(self):        
        self.mensagem_informação = QMessageBox()
        self.mensagem_informação.setText('Preencha todos os campos corretamente!')
        self.mensagem_informação.show()
        self.mensagem_informação.setIcon(QMessageBox.Information)
        self.mensagem_informação.setWindowTitle('ERRO')