# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import QRC_login_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setEnabled(True)
        Main.resize(919, 597)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setMaximumSize(QSize(919, 597))
        Main.setSizeIncrement(QSize(0, 0))
        Main.setBaseSize(QSize(0, 0))
        Main.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(919, 597))
        self.centralwidget.setMaximumSize(QSize(919, 597))
        self.centralwidget.setBaseSize(QSize(919, 597))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(140, 0, 801, 597))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(919, 597))
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setFocusPolicy(Qt.StrongFocus)
        self.pag_perfil = QWidget()
        self.pag_perfil.setObjectName(u"pag_perfil")
        self.btn_alterarSenha = QPushButton(self.pag_perfil)
        self.btn_alterarSenha.setObjectName(u"btn_alterarSenha")
        self.btn_alterarSenha.setGeometry(QRect(420, 280, 111, 31))
        font = QFont()
        font.setKerning(True)
        self.btn_alterarSenha.setFont(font)
        self.btn_alterarSenha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterarSenha.setFocusPolicy(Qt.NoFocus)
        self.btn_alterarSenha.setAutoFillBackground(False)
        self.btn_alterarSenha.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: black; \n"
"border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.inp_novaSenha = QLineEdit(self.pag_perfil)
        self.inp_novaSenha.setObjectName(u"inp_novaSenha")
        self.inp_novaSenha.setGeometry(QRect(420, 340, 261, 31))
        self.inp_novaSenha.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.btn_salvarSenha = QPushButton(self.pag_perfil)
        self.btn_salvarSenha.setObjectName(u"btn_salvarSenha")
        self.btn_salvarSenha.setGeometry(QRect(420, 400, 111, 31))
        self.btn_salvarSenha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvarSenha.setAutoFillBackground(False)
        self.btn_salvarSenha.setStyleSheet(u"color: white;\n"
"background-color: black; \n"
"border-radius: 5px;")
        self.lbl_nomeUsuario = QLabel(self.pag_perfil)
        self.lbl_nomeUsuario.setObjectName(u"lbl_nomeUsuario")
        self.lbl_nomeUsuario.setGeometry(QRect(420, 70, 261, 61))
        self.lbl_nomeUsuario.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;")
        self.lbl_barraLateral = QLabel(self.pag_perfil)
        self.lbl_barraLateral.setObjectName(u"lbl_barraLateral")
        self.lbl_barraLateral.setGeometry(QRect(730, 0, 51, 601))
        self.lbl_barraLateral.setPixmap(QPixmap(u":/imagens/imagens/barra do perfil.png"))
        self.lbl_barraLateral.setScaledContents(True)
        self.lbl_imagemPerfil = QLabel(self.pag_perfil)
        self.lbl_imagemPerfil.setObjectName(u"lbl_imagemPerfil")
        self.lbl_imagemPerfil.setGeometry(QRect(50, 60, 251, 241))
        self.lbl_imagemPerfil.setPixmap(QPixmap(u":/imagens/imagens/profileimg.jpg"))
        self.lbl_imagemPerfil.setScaledContents(True)
        self.lbl_retanguloPretoAzul = QLabel(self.pag_perfil)
        self.lbl_retanguloPretoAzul.setObjectName(u"lbl_retanguloPretoAzul")
        self.lbl_retanguloPretoAzul.setGeometry(QRect(-80, 380, 441, 321))
        self.lbl_retanguloPretoAzul.setPixmap(QPixmap(u":/imagens/imagens/retangulo preto e azul.jpg"))
        self.lbl_retanguloPretoAzul.setScaledContents(True)
        self.lbl_emailUsuario = QLabel(self.pag_perfil)
        self.lbl_emailUsuario.setObjectName(u"lbl_emailUsuario")
        self.lbl_emailUsuario.setGeometry(QRect(420, 170, 261, 61))
        self.lbl_emailUsuario.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;")
        self.btn_alterar_foto_perfil = QPushButton(self.pag_perfil)
        self.btn_alterar_foto_perfil.setObjectName(u"btn_alterar_foto_perfil")
        self.btn_alterar_foto_perfil.setGeometry(QRect(270, 260, 31, 31))
        self.btn_alterar_foto_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_foto_perfil.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"imagens/pencil_edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_foto_perfil.setIcon(icon)
        self.btn_alterar_foto_perfil.setIconSize(QSize(38, 25))
        self.stackedWidget.addWidget(self.pag_perfil)
        self.pag_relatorio = QWidget()
        self.pag_relatorio.setObjectName(u"pag_relatorio")
        self.frame_tabelaRelatorio = QFrame(self.pag_relatorio)
        self.frame_tabelaRelatorio.setObjectName(u"frame_tabelaRelatorio")
        self.frame_tabelaRelatorio.setGeometry(QRect(120, 140, 561, 411))
        self.frame_tabelaRelatorio.setFrameShape(QFrame.StyledPanel)
        self.frame_tabelaRelatorio.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_tabelaRelatorio)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_pesquisa = QFrame(self.frame_tabelaRelatorio)
        self.frame_pesquisa.setObjectName(u"frame_pesquisa")
        self.frame_pesquisa.setFrameShape(QFrame.StyledPanel)
        self.frame_pesquisa.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_pesquisa)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_pesquisar = QLabel(self.frame_pesquisa)
        self.img_pesquisar.setObjectName(u"img_pesquisar")
        self.img_pesquisar.setMinimumSize(QSize(20, 20))
        self.img_pesquisar.setMaximumSize(QSize(20, 20))
        self.img_pesquisar.setPixmap(QPixmap(u"imagens/searchmagnifierinterfacesymbol1_79893.ico"))
        self.img_pesquisar.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img_pesquisar)

        self.inp_procurarProduto = QLineEdit(self.frame_pesquisa)
        self.inp_procurarProduto.setObjectName(u"inp_procurarProduto")
        self.inp_procurarProduto.setMinimumSize(QSize(125, 20))
        font1 = QFont()
        self.inp_procurarProduto.setFont(font1)
        self.inp_procurarProduto.setStyleSheet(u"QLineEdit{\n"
"	border: none; /* Remove a borda padr\u00e3o */\n"
"    border-bottom: 1px solid #000; /* Adiciona uma borda inferior de 1px s\u00f3lida */\n"
"    background-color: transparent;/* Define o Background como transparente*/\n"
"	color: #000000000;\n"
"	font-size: 13px; /* Defina o tamanho do texto do placeholder desejado */\n"
"	padding-left: 0px;\n"
"	font-style: montserrat;\n"
"}\n"
"\n"
"")
        self.inp_procurarProduto.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.inp_procurarProduto.setDragEnabled(False)
        self.inp_procurarProduto.setReadOnly(False)
        self.inp_procurarProduto.setPlaceholderText(u"Digite o produto...")

        self.horizontalLayout.addWidget(self.inp_procurarProduto)


        self.verticalLayout_3.addWidget(self.frame_pesquisa, 0, Qt.AlignLeft)

        self.tbl_relatorio = QTableWidget(self.frame_tabelaRelatorio)
        if (self.tbl_relatorio.columnCount() < 4):
            self.tbl_relatorio.setColumnCount(4)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font2);
        self.tbl_relatorio.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font2);
        self.tbl_relatorio.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font2);
        self.tbl_relatorio.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font2);
        self.tbl_relatorio.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tbl_relatorio.rowCount() < 4):
            self.tbl_relatorio.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tbl_relatorio.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tbl_relatorio.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tbl_relatorio.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tbl_relatorio.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font2);
        __qtablewidgetitem8.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font2);
        __qtablewidgetitem9.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font2);
        __qtablewidgetitem10.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(0, 2, __qtablewidgetitem10)
        brush = QBrush(QColor(0, 160, 32, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font2);
        __qtablewidgetitem11.setBackground(brush);
        __qtablewidgetitem11.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font2);
        __qtablewidgetitem12.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font2);
        __qtablewidgetitem13.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font2);
        __qtablewidgetitem14.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(1, 2, __qtablewidgetitem14)
        brush1 = QBrush(QColor(209, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font2);
        __qtablewidgetitem15.setBackground(brush1);
        __qtablewidgetitem15.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(1, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font2);
        __qtablewidgetitem16.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font2);
        __qtablewidgetitem17.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font2);
        __qtablewidgetitem18.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(2, 2, __qtablewidgetitem18)
        brush2 = QBrush(QColor(234, 130, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font2);
        __qtablewidgetitem19.setBackground(brush2);
        __qtablewidgetitem19.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(2, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font2);
        __qtablewidgetitem20.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font2);
        __qtablewidgetitem21.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font2);
        __qtablewidgetitem22.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(3, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font2);
        __qtablewidgetitem23.setBackground(brush);
        __qtablewidgetitem23.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(3, 3, __qtablewidgetitem23)
        self.tbl_relatorio.setObjectName(u"tbl_relatorio")
        self.tbl_relatorio.setAlternatingRowColors(True)
        self.tbl_relatorio.setSortingEnabled(True)
        self.tbl_relatorio.setCornerButtonEnabled(True)
        self.tbl_relatorio.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_relatorio.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbl_relatorio.horizontalHeader().setStretchLastSection(True)
        self.tbl_relatorio.verticalHeader().setVisible(False)
        self.tbl_relatorio.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_relatorio.verticalHeader().setHighlightSections(True)
        self.tbl_relatorio.verticalHeader().setProperty("showSortIndicator", False)
        self.tbl_relatorio.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.tbl_relatorio)

        self.btn_salvar_em_pdf = QPushButton(self.frame_tabelaRelatorio)
        self.btn_salvar_em_pdf.setObjectName(u"btn_salvar_em_pdf")
        self.btn_salvar_em_pdf.setMinimumSize(QSize(120, 35))
        self.btn_salvar_em_pdf.setMaximumSize(QSize(120, 120))
        font3 = QFont()
        font3.setFamilies([u"Microsoft JhengHei"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_salvar_em_pdf.setFont(font3)
        self.btn_salvar_em_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_em_pdf.setStyleSheet(u"background-color: rgb(38, 81, 137);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"imagens/save-file-option_icon-icons.com_73423.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_em_pdf.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.btn_salvar_em_pdf, 0, Qt.AlignRight)

        self.img_formaRelatorio_2 = QLabel(self.pag_relatorio)
        self.img_formaRelatorio_2.setObjectName(u"img_formaRelatorio_2")
        self.img_formaRelatorio_2.setGeometry(QRect(-150, 370, 271, 261))
        self.img_formaRelatorio_2.setPixmap(QPixmap(u"imagens/Group 48img_formaRelatorio.png"))
        self.img_formaRelatorio_2.setScaledContents(True)
        self.img_formaRelatorio_3 = QLabel(self.pag_relatorio)
        self.img_formaRelatorio_3.setObjectName(u"img_formaRelatorio_3")
        self.img_formaRelatorio_3.setGeometry(QRect(540, -100, 331, 251))
        self.img_formaRelatorio_3.setPixmap(QPixmap(u"imagens/Group 43img_formaRelatorio.png"))
        self.img_formaRelatorio_3.setScaledContents(True)
        self.lbl_barraLateral_2 = QLabel(self.pag_relatorio)
        self.lbl_barraLateral_2.setObjectName(u"lbl_barraLateral_2")
        self.lbl_barraLateral_2.setGeometry(QRect(740, 50, 41, 551))
        self.lbl_barraLateral_2.setPixmap(QPixmap(u":/imagens/imagens/barra do perfil.png"))
        self.lbl_barraLateral_2.setScaledContents(True)
        self.stackedWidget.addWidget(self.pag_relatorio)
        self.pag_adicionar_produto = QWidget()
        self.pag_adicionar_produto.setObjectName(u"pag_adicionar_produto")
        self.inp_nome_product = QLineEdit(self.pag_adicionar_produto)
        self.inp_nome_product.setObjectName(u"inp_nome_product")
        self.inp_nome_product.setGeometry(QRect(130, 80, 491, 20))
        font4 = QFont()
        font4.setPointSize(15)
        self.inp_nome_product.setFont(font4)
        self.inp_nome_product.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.img_design_baixo = QLabel(self.pag_adicionar_produto)
        self.img_design_baixo.setObjectName(u"img_design_baixo")
        self.img_design_baixo.setGeometry(QRect(-34, 448, 121, 151))
        self.img_design_baixo.setPixmap(QPixmap(u":/imagens/Group 50imagens2.jpg"))
        self.img_design_baixo.setScaledContents(True)
        self.inp_quantidade_product = QLineEdit(self.pag_adicionar_produto)
        self.inp_quantidade_product.setObjectName(u"inp_quantidade_product")
        self.inp_quantidade_product.setGeometry(QRect(130, 330, 491, 20))
        self.inp_quantidade_product.setFont(font4)
        self.inp_quantidade_product.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.btn_registrar_product = QPushButton(self.pag_adicionar_produto)
        self.btn_registrar_product.setObjectName(u"btn_registrar_product")
        self.btn_registrar_product.setGeometry(QRect(290, 520, 151, 31))
        self.btn_registrar_product.setFont(font4)
        self.btn_registrar_product.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar_product.setStyleSheet(u"QPushButton {\n"
"	\n"
"	border-radius:7px;\n"
"	background-color: #355BA5;\n"
"	color: white\n"
"}")
        self.inp_descricao_product = QLineEdit(self.pag_adicionar_produto)
        self.inp_descricao_product.setObjectName(u"inp_descricao_product")
        self.inp_descricao_product.setGeometry(QRect(130, 450, 491, 20))
        self.inp_descricao_product.setFont(font4)
        self.inp_descricao_product.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.inp_marca_product = QLineEdit(self.pag_adicionar_produto)
        self.inp_marca_product.setObjectName(u"inp_marca_product")
        self.inp_marca_product.setGeometry(QRect(130, 200, 491, 20))
        self.inp_marca_product.setFont(font4)
        self.inp_marca_product.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.img_design_lateral = QLabel(self.pag_adicionar_produto)
        self.img_design_lateral.setObjectName(u"img_design_lateral")
        self.img_design_lateral.setGeometry(QRect(730, 0, 51, 601))
        self.img_design_lateral.setPixmap(QPixmap(u"imagens/barra do perfil.png"))
        self.img_design_lateral.setScaledContents(True)
        self.stackedWidget.addWidget(self.pag_adicionar_produto)
        self.pag_retirar_produto = QWidget()
        self.pag_retirar_produto.setObjectName(u"pag_retirar_produto")
        self.lbl_N_M_Q_R = QLabel(self.pag_retirar_produto)
        self.lbl_N_M_Q_R.setObjectName(u"lbl_N_M_Q_R")
        self.lbl_N_M_Q_R.setGeometry(QRect(90, 70, 531, 41))
        self.lbl_N_M_Q_R.setStyleSheet(u"Background-color:rgb(32,90,153);\n"
"color:white;\n"
"border-radius:5px;")
        self.inp_nome_product_3 = QLineEdit(self.pag_retirar_produto)
        self.inp_nome_product_3.setObjectName(u"inp_nome_product_3")
        self.inp_nome_product_3.setGeometry(QRect(110, 40, 511, 20))
        self.inp_nome_product_3.setFont(font4)
        self.inp_nome_product_3.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.spinBox = QSpinBox(self.pag_retirar_produto)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(520, 110, 42, 22))
        self.btn_confirmar = QPushButton(self.pag_retirar_produto)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        self.btn_confirmar.setGeometry(QRect(280, 530, 151, 31))
        self.btn_confirmar.setMinimumSize(QSize(151, 31))
        self.btn_confirmar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirmar.setStyleSheet(u"Background-color:rgb(32,90,153);\n"
"color:white;\n"
"border-radius:5px;")
        self.lbl_barraLateral_3 = QLabel(self.pag_retirar_produto)
        self.lbl_barraLateral_3.setObjectName(u"lbl_barraLateral_3")
        self.lbl_barraLateral_3.setGeometry(QRect(740, 0, 41, 601))
        self.lbl_barraLateral_3.setStyleSheet(u"")
        self.lbl_barraLateral_3.setPixmap(QPixmap(u":/imagens/imagens/barra do perfil.png"))
        self.lbl_barraLateral_3.setScaledContents(True)
        self.lbl_retanguloPretoAzul_3 = QLabel(self.pag_retirar_produto)
        self.lbl_retanguloPretoAzul_3.setObjectName(u"lbl_retanguloPretoAzul_3")
        self.lbl_retanguloPretoAzul_3.setGeometry(QRect(-30, 540, 121, 81))
        self.lbl_retanguloPretoAzul_3.setCursor(QCursor(Qt.OpenHandCursor))
        self.lbl_retanguloPretoAzul_3.setPixmap(QPixmap(u":/imagens/imagens/retangulo preto e azul.jpg"))
        self.lbl_retanguloPretoAzul_3.setScaledContents(True)
        self.img_pesquisar_3 = QLabel(self.pag_retirar_produto)
        self.img_pesquisar_3.setObjectName(u"img_pesquisar_3")
        self.img_pesquisar_3.setGeometry(QRect(80, 40, 20, 20))
        self.img_pesquisar_3.setMinimumSize(QSize(20, 20))
        self.img_pesquisar_3.setMaximumSize(QSize(20, 20))
        self.img_pesquisar_3.setPixmap(QPixmap(u"imagens/searchmagnifierinterfacesymbol1_79893.ico"))
        self.img_pesquisar_3.setScaledContents(True)
        self.pushButton = QPushButton(self.pag_retirar_produto)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(582, 101, 18, 31))
        self.pushButton.setMaximumSize(QSize(16777215, 16777192))
        font5 = QFont()
        font5.setPointSize(39)
        self.pushButton.setFont(font5)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color: red;\n"
"background-color: transparent;\n"
"}")
        self.tbl_retirada = QListWidget(self.pag_retirar_produto)
        QListWidgetItem(self.tbl_retirada)
        self.tbl_retirada.setObjectName(u"tbl_retirada")
        self.tbl_retirada.setGeometry(QRect(90, 110, 531, 401))
        self.tbl_retirada.setAutoFillBackground(False)
        self.tbl_retirada.setStyleSheet(u"")
        self.tbl_retirada.setFrameShape(QFrame.StyledPanel)
        self.tbl_retirada.setFrameShadow(QFrame.Plain)
        self.pushButton_2 = QPushButton(self.pag_retirar_produto)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(580, 107, 21, 23))
        font6 = QFont()
        font6.setPointSize(33)
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setCursor(QCursor(Qt.ClosedHandCursor))
        self.pushButton_2.setStyleSheet(u"color:red;\n"
"background-color:transparent;\n"
"")
        self.spinBox_2 = QSpinBox(self.pag_retirar_produto)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(520, 110, 42, 22))
        self.stackedWidget.addWidget(self.pag_retirar_produto)
        self.pag_editar_produto = QWidget()
        self.pag_editar_produto.setObjectName(u"pag_editar_produto")
        self.btn_Salvar = QPushButton(self.pag_editar_produto)
        self.btn_Salvar.setObjectName(u"btn_Salvar")
        self.btn_Salvar.setGeometry(QRect(480, 530, 101, 31))
        self.btn_Salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(53, 91, 165);\n"
"}")
        self.inp_Marca_do_Produto = QLineEdit(self.pag_editar_produto)
        self.inp_Marca_do_Produto.setObjectName(u"inp_Marca_do_Produto")
        self.inp_Marca_do_Produto.setGeometry(QRect(390, 260, 301, 21))
        font7 = QFont()
        font7.setPointSize(10)
        self.inp_Marca_do_Produto.setFont(font7)
        self.inp_Marca_do_Produto.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(97, 95, 95);\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent\n"
"}")
        self.inp_descricao = QLineEdit(self.pag_editar_produto)
        self.inp_descricao.setObjectName(u"inp_descricao")
        self.inp_descricao.setGeometry(QRect(380, 400, 301, 91))
        self.inp_descricao.setFont(font7)
        self.inp_descricao.setStyleSheet(u"QLineEdit{\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"	border-color: black;\n"
"}")
        self.inp_descricao.setCursorPosition(0)
        self.inp_descricao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.img_lupa = QLabel(self.pag_editar_produto)
        self.img_lupa.setObjectName(u"img_lupa")
        self.img_lupa.setGeometry(QRect(240, 70, 21, 21))
        self.img_lupa.setPixmap(QPixmap(u"imagens/searchmagnifierinterfacesymbol1_79893.ico"))
        self.img_lupa.setScaledContents(True)
        self.listWidget = QListWidget(self.pag_editar_produto)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.NoBrush)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.NoBrush)
        font8 = QFont()
        font8.setPointSize(20)
        font8.setKerning(False)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font8);
        __qlistwidgetitem.setBackground(brush4);
        __qlistwidgetitem.setForeground(brush3);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(60, 130, 301, 431))
        self.listWidget.setStyleSheet(u"QListWidget{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(53, 91, 165);\n"
"	color: white;\n"
"\n"
"}")
        self.listWidget.setFrameShape(QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.inp_pesquisar_produto = QLineEdit(self.pag_editar_produto)
        self.inp_pesquisar_produto.setObjectName(u"inp_pesquisar_produto")
        self.inp_pesquisar_produto.setGeometry(QRect(260, 70, 291, 20))
        self.inp_pesquisar_produto.setFont(font7)
        self.inp_pesquisar_produto.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent\n"
"}")
        self.inp_Nome_do_Produto = QLineEdit(self.pag_editar_produto)
        self.inp_Nome_do_Produto.setObjectName(u"inp_Nome_do_Produto")
        self.inp_Nome_do_Produto.setGeometry(QRect(390, 190, 301, 21))
        self.inp_Nome_do_Produto.setFont(font7)
        self.inp_Nome_do_Produto.setToolTipDuration(-1)
        self.inp_Nome_do_Produto.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(97, 95, 95);\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent\n"
"	\n"
"}")
        self.img_triangulo_azul = QLabel(self.pag_editar_produto)
        self.img_triangulo_azul.setObjectName(u"img_triangulo_azul")
        self.img_triangulo_azul.setGeometry(QRect(-10, 520, 101, 91))
        self.img_triangulo_azul.setPixmap(QPixmap(u"imagens/Group 50imagens2.jpg"))
        self.img_triangulo_azul.setScaledContents(True)
        self.lbl_descricao = QLabel(self.pag_editar_produto)
        self.lbl_descricao.setObjectName(u"lbl_descricao")
        self.lbl_descricao.setGeometry(QRect(390, 380, 61, 16))
        self.lbl_descricao.setFont(font7)
        self.lbl_descricao.setAutoFillBackground(False)
        self.lbl_quantidade = QLineEdit(self.pag_editar_produto)
        self.lbl_quantidade.setObjectName(u"lbl_quantidade")
        self.lbl_quantidade.setGeometry(QRect(390, 330, 301, 21))
        self.lbl_quantidade.setFont(font7)
        self.lbl_quantidade.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(97, 95, 95);\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent\n"
"}")
        self.lbl_quantidade.setReadOnly(True)
        self.lbl_barraLateral_4 = QLabel(self.pag_editar_produto)
        self.lbl_barraLateral_4.setObjectName(u"lbl_barraLateral_4")
        self.lbl_barraLateral_4.setGeometry(QRect(800, 100, 51, 601))
        self.lbl_barraLateral_4.setPixmap(QPixmap(u":/imagens/imagens/barra do perfil.png"))
        self.lbl_barraLateral_4.setScaledContents(True)
        self.lbl_barraLateral_5 = QLabel(self.pag_editar_produto)
        self.lbl_barraLateral_5.setObjectName(u"lbl_barraLateral_5")
        self.lbl_barraLateral_5.setGeometry(QRect(730, 0, 51, 601))
        self.lbl_barraLateral_5.setPixmap(QPixmap(u":/imagens/imagens/barra do perfil.png"))
        self.lbl_barraLateral_5.setScaledContents(True)
        self.stackedWidget.addWidget(self.pag_editar_produto)
        self.img_triangulo_azul.raise_()
        self.btn_Salvar.raise_()
        self.inp_Marca_do_Produto.raise_()
        self.inp_descricao.raise_()
        self.img_lupa.raise_()
        self.listWidget.raise_()
        self.inp_pesquisar_produto.raise_()
        self.inp_Nome_do_Produto.raise_()
        self.lbl_descricao.raise_()
        self.lbl_quantidade.raise_()
        self.lbl_barraLateral_4.raise_()
        self.lbl_barraLateral_5.raise_()
        self.barra_fixa = QFrame(self.centralwidget)
        self.barra_fixa.setObjectName(u"barra_fixa")
        self.barra_fixa.setEnabled(True)
        self.barra_fixa.setGeometry(QRect(0, 0, 161, 821))
        sizePolicy.setHeightForWidth(self.barra_fixa.sizePolicy().hasHeightForWidth())
        self.barra_fixa.setSizePolicy(sizePolicy)
        self.barra_fixa.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #383897, stop:1 #1E5C99);")
        self.barra_fixa.setFrameShape(QFrame.StyledPanel)
        self.barra_fixa.setFrameShadow(QFrame.Raised)
        self.lbl_Usuario = QLabel(self.barra_fixa)
        self.lbl_Usuario.setObjectName(u"lbl_Usuario")
        self.lbl_Usuario.setGeometry(QRect(40, 10, 61, 31))
        self.lbl_Usuario.setStyleSheet(u"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;")
        self.btn_Relatorio = QPushButton(self.barra_fixa)
        self.btn_Relatorio.setObjectName(u"btn_Relatorio")
        self.btn_Relatorio.setGeometry(QRect(33, 190, 81, 41))
        self.btn_Relatorio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Relatorio.setStyleSheet(u"border: none;\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;\n"
"background-color: transparent")
        self.btn_Relatorio.setFlat(True)
        self.btn_Produtos_ADICIONAR = QPushButton(self.barra_fixa)
        self.btn_Produtos_ADICIONAR.setObjectName(u"btn_Produtos_ADICIONAR")
        self.btn_Produtos_ADICIONAR.setEnabled(True)
        self.btn_Produtos_ADICIONAR.setGeometry(QRect(35, 240, 81, 41))
        self.btn_Produtos_ADICIONAR.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Produtos_ADICIONAR.setStyleSheet(u"border: none;\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;\n"
"background-color: transparent")
        self.btn_Produtos_ADICIONAR.setFlat(True)
        self.btn_Sair = QPushButton(self.barra_fixa)
        self.btn_Sair.setObjectName(u"btn_Sair")
        self.btn_Sair.setGeometry(QRect(25, 553, 75, 23))
        self.btn_Sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Sair.setStyleSheet(u"border:none;\n"
"color: white;\n"
"background-color: transparent")
        self.btn_Sair.setFlat(True)
        self.btn_Perfil = QPushButton(self.barra_fixa)
        self.btn_Perfil.setObjectName(u"btn_Perfil")
        self.btn_Perfil.setGeometry(QRect(23, 140, 81, 41))
        self.btn_Perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Perfil.setMouseTracking(False)
        self.btn_Perfil.setAutoFillBackground(False)
        self.btn_Perfil.setStyleSheet(u"border: none;\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;\n"
"background-color: transparent")
        self.btn_Perfil.setCheckable(False)
        self.btn_Perfil.setAutoRepeat(True)
        self.btn_Perfil.setAutoDefault(False)
        self.btn_Perfil.setFlat(True)
        self.img_IconSair = QLabel(self.barra_fixa)
        self.img_IconSair.setObjectName(u"img_IconSair")
        self.img_IconSair.setGeometry(QRect(10, 550, 31, 31))
        self.img_IconSair.setStyleSheet(u"color: white;\n"
"")
        self.img_IconSair.setText(u"")
        self.img_IconSair.setTextFormat(Qt.AutoText)
        self.img_IconSair.setPixmap(QPixmap(u"imagens/sair_icon.png"))
        self.img_IconSair.setScaledContents(False)
        self.img_IconSair.setAlignment(Qt.AlignCenter)
        self.img_IconSair.setWordWrap(False)
        self.img_IconSair.setMargin(0)
        self.img_perfil = QLabel(self.barra_fixa)
        self.img_perfil.setObjectName(u"img_perfil")
        self.img_perfil.setGeometry(QRect(10, 150, 21, 21))
        self.img_perfil.setStyleSheet(u"color: white;\n"
"")
        self.img_perfil.setText(u"")
        self.img_perfil.setTextFormat(Qt.AutoText)
        self.img_perfil.setPixmap(QPixmap(u"imagens/perfil_icon.png"))
        self.img_perfil.setScaledContents(False)
        self.img_perfil.setAlignment(Qt.AlignCenter)
        self.img_perfil.setMargin(-1)
        self.img_add_produto = QLabel(self.barra_fixa)
        self.img_add_produto.setObjectName(u"img_add_produto")
        self.img_add_produto.setGeometry(QRect(10, 250, 21, 21))
        self.img_add_produto.setStyleSheet(u"color: white;\n"
"")
        self.img_add_produto.setTextFormat(Qt.AutoText)
        self.img_add_produto.setPixmap(QPixmap(u"imagens/icon_add_product.png"))
        self.img_add_produto.setScaledContents(False)
        self.img_add_produto.setAlignment(Qt.AlignCenter)
        self.img_add_produto.setWordWrap(False)
        self.img_add_produto.setMargin(0)
        self.img_relatorio = QLabel(self.barra_fixa)
        self.img_relatorio.setObjectName(u"img_relatorio")
        self.img_relatorio.setGeometry(QRect(10, 200, 21, 21))
        self.img_relatorio.setStyleSheet(u"color: white;\n"
"")
        self.img_relatorio.setText(u"")
        self.img_relatorio.setTextFormat(Qt.AutoText)
        self.img_relatorio.setPixmap(QPixmap(u"imagens/list_icon.png"))
        self.img_relatorio.setScaledContents(False)
        self.img_relatorio.setAlignment(Qt.AlignCenter)
        self.img_relatorio.setWordWrap(False)
        self.img_relatorio.setMargin(0)
        self.img_remover_produto = QLabel(self.barra_fixa)
        self.img_remover_produto.setObjectName(u"img_remover_produto")
        self.img_remover_produto.setGeometry(QRect(10, 300, 21, 21))
        self.img_remover_produto.setStyleSheet(u"color: white;\n"
"")
        self.img_remover_produto.setTextFormat(Qt.AutoText)
        self.img_remover_produto.setPixmap(QPixmap(u"imagens/icon_retirar_produt.png"))
        self.img_remover_produto.setScaledContents(False)
        self.img_remover_produto.setAlignment(Qt.AlignCenter)
        self.img_remover_produto.setWordWrap(False)
        self.img_remover_produto.setMargin(0)
        self.btn_Produtos_RETIRAR_QTD = QPushButton(self.barra_fixa)
        self.btn_Produtos_RETIRAR_QTD.setObjectName(u"btn_Produtos_RETIRAR_QTD")
        self.btn_Produtos_RETIRAR_QTD.setEnabled(True)
        self.btn_Produtos_RETIRAR_QTD.setGeometry(QRect(27, 290, 81, 41))
        self.btn_Produtos_RETIRAR_QTD.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Produtos_RETIRAR_QTD.setStyleSheet(u"border:none;\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;\n"
"background-color: transparent")
        self.btn_Produtos_RETIRAR_QTD.setFlat(True)
        self.img_IconSair_6 = QLabel(self.barra_fixa)
        self.img_IconSair_6.setObjectName(u"img_IconSair_6")
        self.img_IconSair_6.setGeometry(QRect(10, 350, 21, 21))
        self.img_IconSair_6.setStyleSheet(u"color: white;\n"
"")
        self.img_IconSair_6.setText(u"")
        self.img_IconSair_6.setTextFormat(Qt.AutoText)
        self.img_IconSair_6.setPixmap(QPixmap(u"imagens/icon_edit_product.png"))
        self.img_IconSair_6.setScaledContents(False)
        self.img_IconSair_6.setAlignment(Qt.AlignCenter)
        self.img_IconSair_6.setWordWrap(False)
        self.img_IconSair_6.setMargin(-20)
        self.btn_Produtos_EDITAR = QPushButton(self.barra_fixa)
        self.btn_Produtos_EDITAR.setObjectName(u"btn_Produtos_EDITAR")
        self.btn_Produtos_EDITAR.setEnabled(True)
        self.btn_Produtos_EDITAR.setGeometry(QRect(26, 340, 81, 41))
        self.btn_Produtos_EDITAR.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Produtos_EDITAR.setStyleSheet(u"border:none;\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;\n"
"background-color: transparent")
        self.btn_Produtos_EDITAR.setFlat(True)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.stackedWidget.setCurrentIndex(0)
        self.btn_Perfil.setDefault(False)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.btn_alterarSenha.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_alterarSenha.setWhatsThis(QCoreApplication.translate("Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_alterarSenha.setText(QCoreApplication.translate("Main", u"Alterar Senha", None))
        self.inp_novaSenha.setPlaceholderText(QCoreApplication.translate("Main", u"Nova Senha", None))
#if QT_CONFIG(tooltip)
        self.btn_salvarSenha.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_salvarSenha.setWhatsThis(QCoreApplication.translate("Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Alterar Senha</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_salvarSenha.setText(QCoreApplication.translate("Main", u"Salvar", None))
        self.lbl_nomeUsuario.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Matheus de Matos Nunes</span></p></body></html>", None))
        self.lbl_barraLateral.setText("")
        self.lbl_imagemPerfil.setText("")
        self.lbl_retanguloPretoAzul.setText("")
        self.lbl_emailUsuario.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Masterm4ts@gmail.com</span></p></body></html>", None))
        self.btn_alterar_foto_perfil.setText("")
        self.img_pesquisar.setText("")
        self.inp_procurarProduto.setText("")
        ___qtablewidgetitem = self.tbl_relatorio.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Main", u"NOME", None));
        ___qtablewidgetitem1 = self.tbl_relatorio.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Main", u"MARCA", None));
        ___qtablewidgetitem2 = self.tbl_relatorio.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Main", u"QUANTIDADE", None));
        ___qtablewidgetitem3 = self.tbl_relatorio.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Main", u"STATUS", None));
        ___qtablewidgetitem4 = self.tbl_relatorio.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Main", u"1", None));
        ___qtablewidgetitem5 = self.tbl_relatorio.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Main", u"2", None));
        ___qtablewidgetitem6 = self.tbl_relatorio.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Main", u"3", None));
        ___qtablewidgetitem7 = self.tbl_relatorio.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Main", u"4", None));

        __sortingEnabled = self.tbl_relatorio.isSortingEnabled()
        self.tbl_relatorio.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tbl_relatorio.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Main", u"Luva Descartavel", None));
        ___qtablewidgetitem9 = self.tbl_relatorio.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Main", u"Farma", None));
        ___qtablewidgetitem10 = self.tbl_relatorio.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Main", u"100", None));
        ___qtablewidgetitem11 = self.tbl_relatorio.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Main", u"Disponivel", None));
        ___qtablewidgetitem12 = self.tbl_relatorio.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Main", u"Bisturi", None));
        ___qtablewidgetitem13 = self.tbl_relatorio.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Main", u"Neo", None));
        ___qtablewidgetitem14 = self.tbl_relatorio.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Main", u"0", None));
        ___qtablewidgetitem15 = self.tbl_relatorio.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Main", u"Em Falta", None));
        ___qtablewidgetitem16 = self.tbl_relatorio.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Main", u"Jaleco", None));
        ___qtablewidgetitem17 = self.tbl_relatorio.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Main", u"Quimica", None));
        ___qtablewidgetitem18 = self.tbl_relatorio.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Main", u"10", None));
        ___qtablewidgetitem19 = self.tbl_relatorio.item(2, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Main", u"Esgotando", None));
        ___qtablewidgetitem20 = self.tbl_relatorio.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Main", u"Mascara", None));
        ___qtablewidgetitem21 = self.tbl_relatorio.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Main", u"Arena", None));
        ___qtablewidgetitem22 = self.tbl_relatorio.item(3, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Main", u"200", None));
        ___qtablewidgetitem23 = self.tbl_relatorio.item(3, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Main", u"Disponivel", None));
        self.tbl_relatorio.setSortingEnabled(__sortingEnabled)

        self.btn_salvar_em_pdf.setText(QCoreApplication.translate("Main", u"Salvar em PDF", None))
        self.img_formaRelatorio_2.setText("")
        self.img_formaRelatorio_3.setText("")
        self.lbl_barraLateral_2.setText("")
        self.inp_nome_product.setText("")
        self.inp_nome_product.setPlaceholderText(QCoreApplication.translate("Main", u"Nome do Produto", None))
        self.img_design_baixo.setText("")
        self.inp_quantidade_product.setText("")
        self.inp_quantidade_product.setPlaceholderText(QCoreApplication.translate("Main", u"Quantidade", None))
        self.btn_registrar_product.setText(QCoreApplication.translate("Main", u"Adicionar", None))
        self.inp_descricao_product.setText("")
        self.inp_descricao_product.setPlaceholderText(QCoreApplication.translate("Main", u"Descri\u00e7\u00e3o", None))
        self.inp_marca_product.setText("")
        self.inp_marca_product.setPlaceholderText(QCoreApplication.translate("Main", u"Marca do Produto", None))
        self.img_design_lateral.setText("")
        self.lbl_N_M_Q_R.setText(QCoreApplication.translate("Main", u"                  Nome                                  Marca                               Quantidade                        Retirada", None))
        self.inp_nome_product_3.setText("")
        self.inp_nome_product_3.setPlaceholderText(QCoreApplication.translate("Main", u"Pesquisar...", None))
        self.btn_confirmar.setText(QCoreApplication.translate("Main", u"Confirmar", None))
        self.lbl_barraLateral_3.setText("")
        self.lbl_retanguloPretoAzul_3.setText("")
        self.img_pesquisar_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("Main", u"-", None))

        __sortingEnabled1 = self.tbl_retirada.isSortingEnabled()
        self.tbl_retirada.setSortingEnabled(False)
        ___qlistwidgetitem = self.tbl_retirada.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Main", u"          Capacete                                Peels                                12 unidades", None));
        self.tbl_retirada.setSortingEnabled(__sortingEnabled1)

        self.pushButton_2.setText(QCoreApplication.translate("Main", u"-", None))
        self.btn_Salvar.setText(QCoreApplication.translate("Main", u"Salvar", None))
        self.inp_Marca_do_Produto.setText("")
        self.inp_Marca_do_Produto.setPlaceholderText(QCoreApplication.translate("Main", u"Marca do produto", None))
        self.inp_descricao.setPlaceholderText("")
        self.img_lupa.setText("")

        __sortingEnabled2 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Main", u"Dipirona", None));
        self.listWidget.setSortingEnabled(__sortingEnabled2)

        self.inp_pesquisar_produto.setInputMask("")
        self.inp_pesquisar_produto.setText("")
        self.inp_pesquisar_produto.setPlaceholderText(QCoreApplication.translate("Main", u"Pesquise o Produto...", None))
        self.inp_Nome_do_Produto.setText("")
        self.inp_Nome_do_Produto.setPlaceholderText(QCoreApplication.translate("Main", u"Nome do Produto", None))
        self.img_triangulo_azul.setText("")
        self.lbl_descricao.setText(QCoreApplication.translate("Main", u"Descri\u00e7\u00e3o", None))
        self.lbl_quantidade.setInputMask("")
        self.lbl_quantidade.setText(QCoreApplication.translate("Main", u"Quantidade: 100", None))
        self.lbl_quantidade.setPlaceholderText("")
        self.lbl_barraLateral_4.setText("")
        self.lbl_barraLateral_5.setText("")
#if QT_CONFIG(tooltip)
        self.barra_fixa.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbl_Usuario.setText(QCoreApplication.translate("Main", u"Maur\u00edcio", None))
        self.btn_Relatorio.setText(QCoreApplication.translate("Main", u"Rel\u00e1torio", None))
        self.btn_Produtos_ADICIONAR.setText(QCoreApplication.translate("Main", u"Adicionar", None))
        self.btn_Sair.setText(QCoreApplication.translate("Main", u"Sair", None))
        self.btn_Perfil.setText(QCoreApplication.translate("Main", u"Perfil", None))
        self.btn_Produtos_RETIRAR_QTD.setText(QCoreApplication.translate("Main", u"Retirar", None))
        self.btn_Produtos_EDITAR.setText(QCoreApplication.translate("Main", u"Editar", None))
    # retranslateUi

