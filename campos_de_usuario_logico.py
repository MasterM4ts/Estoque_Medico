######################################################
# Muda as telas de acordo com os botões pressionados #
######################################################

class IndexChanger:
    def __init__(self, ui):
        self.ui = ui  # Armazena a instância da janela principal

        self.ui.btn_Perfil.clicked.connect(self.index_perfil)
        self.ui.btn_Relatorio.clicked.connect(self.index_relatorio)
        self.ui.btn_Produtos_ADICIONAR.clicked.connect(self.index_produto_ADICIONAR)
        self.ui.btn_Produtos_RETIRAR_QTD.clicked.connect(self.index_produto_RETIRAR_QTD)
        self.ui.btn_Produtos_EDITAR.clicked.connect(self.index_produto_EDITAR)
        self.ui.stackedWidget.setCurrentIndex(0)


    def index_perfil(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def index_relatorio(self):
        self.ui.stackedWidget.setCurrentIndex(1)


    def index_produto_ADICIONAR(self):
        self.ui.stackedWidget.setCurrentIndex(2)


    def index_produto_RETIRAR_QTD(self):
        self.ui.stackedWidget.setCurrentIndex(3)


    def index_produto_EDITAR(self):
        self.ui.stackedWidget.setCurrentIndex(4)

        



