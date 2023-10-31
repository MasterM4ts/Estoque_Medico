#Fazer O Sistema logico do relatoriopy
'''
Passo a Passo do Sistema
1- Pegar todos os Dados Do produto Nome,Marca,Quantidade!
2- Passar esses Dados para a tela de Relatório de Estoque
3-Adicionar Botão de para imprimir o arquivo em .PDF
'''
from PySide6.QtWidgets import QLabel,QPushButton,QStackedWidget,QMainWindow,QWidget,QApplication
from reportlab.pdfgen import canvas #Baixar essa biblioteca no Terminal para utilizar
from reportlab.lib.pagesizes import A4
# from Ui_main import *
lista_nome = ["Luva","Jaleco","Agulha","Palito","Algodão"]
lista_marca = ["Adidas","Nike","Puma","Net","Abidas"]
lista_quantidade = ["100","20","0","100","50"]
lista_status = ["Disponivel","Esgotando","Em Falta","Disponivel","Esgotando"]

class Relatorio():


    def exibir_produtos_estoque(self):#Funcão que vai passar por toda a lista e exibir ela para o usuario    
        for a in lista_nome: 
            print(a)
        for b in lista_marca:
            print(b)
        for c in lista_quantidade:
            print(c)
        for d in lista_status:
            print(d)


    def salvar_relatorio(self):#Funçao que deve salvar os dados da lista em PDF
        pdf = canvas.Canvas('teste.pdf',pagesize=A4)
        pdf.setFont('Helvetica-Bold',16)
        
        y = 0
        for i in lista_nome:
            pdf.drawString(100,850 - y,i)
            y = y + 50
        y = 0
        for j in lista_marca:
            
            pdf.drawString(200,850 - y,j)
            y = y + 50
        y = 0
        for k in lista_quantidade:
            pdf.drawString(300,850 - y,k)
            y = y + 50
        y = 0    
        for l in lista_status:
            pdf.drawString(400,850 - y,l)
            y = y + 50
        pdf.save()