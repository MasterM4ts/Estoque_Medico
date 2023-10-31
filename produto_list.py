from PySide6.QtWidgets import QMessageBox
class Product():
    
    lista_produtos = []
    list_quant = []
    lista_Geral = []
    
    def __init__(self, nome, marca, quantidade, descricao) -> None:
       
        
        self.mensagem_informação = QMessageBox()
        self.mensagem_informação.setText('Produto Registrado!')
        self.mensagem_informação.show()
        self.mensagem_informação.setIcon(QMessageBox.Information)
        self.mensagem_informação.setWindowTitle('Confirmação')
        
        self.lista_produtos.append(nome)
        self.lista_produtos.append(marca)
        self.list_quant.append(quantidade)
        self.lista_produtos.append(descricao)
        
        self.lista_Geral.append(nome)
        self.lista_Geral.append(marca)
        self.lista_Geral.append(quantidade)
        self.lista_Geral.append(descricao)

        print(f"Quantidade: {self.list_quant}. Produto: {self.lista_produtos}. \n {self.lista_Geral}")
        
        
    def __str__(self) -> str:
        return (f"Quantidade: {self.list_quant}. Produto: {self.lista_produtos}. ")
        
        

        