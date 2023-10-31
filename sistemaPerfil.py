
class TelaPerfilFuncional:
    def __init__(self, ui) -> None:
        self.tela_perfil = ui
        
        self.tela_perfil.inp_novaSenha.hide()
        self.tela_perfil.btn_salvarSenha.hide()
        self.tela_perfil.btn_alterarSenha.clicked.connect(self.aparecer_botoes)
        

    def aparecer_botoes(self):
        if self.tela_perfil.inp_novaSenha.isHidden():
            self.tela_perfil.inp_novaSenha.show()
            self.tela_perfil.btn_salvarSenha.show()
        else:
            self.tela_perfil.inp_novaSenha.hide()
            self.tela_perfil.btn_salvarSenha.hide()


    
        
        
   
        