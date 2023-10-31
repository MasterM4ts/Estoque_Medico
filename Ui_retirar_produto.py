# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_retirar_produto.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import QRC_login_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(919, 597)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(919, 597))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setBaseSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(919, 597))
        self.centralwidget.setMaximumSize(QSize(919, 597))
        self.centralwidget.setBaseSize(QSize(919, 597))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(150, 20, 771, 581))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(919, 597))
        self.stackedWidget.setMouseTracking(False)
        self.pag_perfil = QWidget()
        self.pag_perfil.setObjectName(u"pag_perfil")
        self.btn_alterarSenha = QPushButton(self.pag_perfil)
        self.btn_alterarSenha.setObjectName(u"btn_alterarSenha")
        self.btn_alterarSenha.setGeometry(QRect(420, 280, 111, 31))
        self.btn_alterarSenha.setAutoFillBackground(False)
        self.btn_alterarSenha.setStyleSheet(u"color: white;\n"
"background-color: black; \n"
"border-radius: 5px;")
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
        self.lbl_barraLateral.setGeometry(QRect(730, 0, 47, 601))
        self.lbl_barraLateral.setPixmap(QPixmap(u":/imagens/imagens/barra do perfil.png"))
        self.lbl_barraLateral.setScaledContents(True)
        self.lbl_imagemPerfil = QLabel(self.pag_perfil)
        self.lbl_imagemPerfil.setObjectName(u"lbl_imagemPerfil")
        self.lbl_imagemPerfil.setGeometry(QRect(50, 60, 251, 201))
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
        self.btn_alterarSenha1 = QPushButton(self.pag_perfil)
        self.btn_alterarSenha1.setObjectName(u"btn_alterarSenha1")
        self.btn_alterarSenha1.setGeometry(QRect(420, 280, 121, 31))
        self.btn_alterarSenha1.setStyleSheet(u"color: white;\n"
"background-color: black; \n"
"border-radius: 5px;\n"
"\n"
"")
        self.btn_salvar = QPushButton(self.pag_perfil)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setGeometry(QRect(420, 400, 121, 31))
        self.btn_salvar.setStyleSheet(u"color: white;\n"
"background-color: black; \n"
"border-radius: 5px;\n"
"\n"
"")
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
        font = QFont()
        self.inp_procurarProduto.setFont(font)
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
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font1);
        self.tbl_relatorio.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font1);
        self.tbl_relatorio.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        self.tbl_relatorio.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font1);
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
        __qtablewidgetitem8.setFont(font1);
        __qtablewidgetitem8.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font1);
        __qtablewidgetitem9.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font1);
        __qtablewidgetitem10.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(0, 2, __qtablewidgetitem10)
        brush = QBrush(QColor(0, 160, 32, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font1);
        __qtablewidgetitem11.setBackground(brush);
        __qtablewidgetitem11.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font1);
        __qtablewidgetitem12.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font1);
        __qtablewidgetitem13.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font1);
        __qtablewidgetitem14.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(1, 2, __qtablewidgetitem14)
        brush1 = QBrush(QColor(209, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font1);
        __qtablewidgetitem15.setBackground(brush1);
        __qtablewidgetitem15.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(1, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font1);
        __qtablewidgetitem16.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font1);
        __qtablewidgetitem17.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font1);
        __qtablewidgetitem18.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(2, 2, __qtablewidgetitem18)
        brush2 = QBrush(QColor(234, 130, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font1);
        __qtablewidgetitem19.setBackground(brush2);
        __qtablewidgetitem19.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(2, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font1);
        __qtablewidgetitem20.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font1);
        __qtablewidgetitem21.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font1);
        __qtablewidgetitem22.setFlags(Qt.ItemIsEnabled);
        self.tbl_relatorio.setItem(3, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font1);
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
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_salvar_em_pdf.setFont(font2)
        self.btn_salvar_em_pdf.setStyleSheet(u"background-color: rgb(38, 81, 137);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"imagens/save-file-option_icon-icons.com_73423.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_em_pdf.setIcon(icon)

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
        self.img_formaRelatorio_4 = QLabel(self.pag_relatorio)
        self.img_formaRelatorio_4.setObjectName(u"img_formaRelatorio_4")
        self.img_formaRelatorio_4.setGeometry(QRect(740, 50, 31, 101))
        self.img_formaRelatorio_4.setPixmap(QPixmap(u"imagens/Group 44img_formaRelatorio.png"))
        self.img_formaRelatorio_4.setScaledContents(True)
        self.img_formaRelatorio_5 = QLabel(self.pag_relatorio)
        self.img_formaRelatorio_5.setObjectName(u"img_formaRelatorio_5")
        self.img_formaRelatorio_5.setGeometry(QRect(730, 160, 51, 41))
        self.img_formaRelatorio_5.setPixmap(QPixmap(u"imagens/Group 45img_formaRelatorio.png"))
        self.img_formaRelatorio_5.setScaledContents(True)
        self.img_formaRelatorio_6 = QLabel(self.pag_relatorio)
        self.img_formaRelatorio_6.setObjectName(u"img_formaRelatorio_6")
        self.img_formaRelatorio_6.setGeometry(QRect(730, 210, 41, 91))
        self.img_formaRelatorio_6.setPixmap(QPixmap(u"imagens/Group 47img_formaRelatorio.png"))
        self.img_formaRelatorio_6.setScaledContents(True)
        self.img_formaRelatorio_7 = QLabel(self.pag_relatorio)
        self.img_formaRelatorio_7.setObjectName(u"img_formaRelatorio_7")
        self.img_formaRelatorio_7.setGeometry(QRect(726, 310, 51, 20))
        self.img_formaRelatorio_7.setPixmap(QPixmap(u"imagens/Group 46img_formaRelatorio.png"))
        self.img_formaRelatorio_7.setScaledContents(True)
        self.img_formaRelatorio_8 = QLabel(self.pag_relatorio)
        self.img_formaRelatorio_8.setObjectName(u"img_formaRelatorio_8")
        self.img_formaRelatorio_8.setGeometry(QRect(730, 340, 41, 91))
        self.img_formaRelatorio_8.setPixmap(QPixmap(u"imagens/Group 47img_formaRelatorio.png"))
        self.img_formaRelatorio_8.setScaledContents(True)
        self.img_formaRelatorio_9 = QLabel(self.pag_relatorio)
        self.img_formaRelatorio_9.setObjectName(u"img_formaRelatorio_9")
        self.img_formaRelatorio_9.setGeometry(QRect(730, 440, 51, 41))
        self.img_formaRelatorio_9.setPixmap(QPixmap(u"imagens/Group 45img_formaRelatorio.png"))
        self.img_formaRelatorio_9.setScaledContents(True)
        self.img_formaRelatorio = QLabel(self.pag_relatorio)
        self.img_formaRelatorio.setObjectName(u"img_formaRelatorio")
        self.img_formaRelatorio.setGeometry(QRect(740, 490, 31, 101))
        self.img_formaRelatorio.setPixmap(QPixmap(u"imagens/Group 44img_formaRelatorio.png"))
        self.img_formaRelatorio.setScaledContents(True)
        self.stackedWidget.addWidget(self.pag_relatorio)
        self.pag_adicionar_produto = QWidget()
        self.pag_adicionar_produto.setObjectName(u"pag_adicionar_produto")
        self.inp_nome_product = QLineEdit(self.pag_adicionar_produto)
        self.inp_nome_product.setObjectName(u"inp_nome_product")
        self.inp_nome_product.setGeometry(QRect(130, 80, 491, 20))
        font3 = QFont()
        font3.setPointSize(15)
        self.inp_nome_product.setFont(font3)
        self.inp_nome_product.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.img_design_baixo = QLabel(self.pag_adicionar_produto)
        self.img_design_baixo.setObjectName(u"img_design_baixo")
        self.img_design_baixo.setGeometry(QRect(0, 340, 121, 151))
        self.img_design_baixo.setPixmap(QPixmap(u":/imagens/Group 50imagens2.jpg"))
        self.img_design_baixo.setScaledContents(True)
        self.inp_quantidade_product = QLineEdit(self.pag_adicionar_produto)
        self.inp_quantidade_product.setObjectName(u"inp_quantidade_product")
        self.inp_quantidade_product.setGeometry(QRect(130, 330, 491, 20))
        self.inp_quantidade_product.setFont(font3)
        self.inp_quantidade_product.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.btn_registrar_product = QPushButton(self.pag_adicionar_produto)
        self.btn_registrar_product.setObjectName(u"btn_registrar_product")
        self.btn_registrar_product.setGeometry(QRect(290, 520, 151, 31))
        self.btn_registrar_product.setFont(font3)
        self.btn_registrar_product.setStyleSheet(u"QPushButton {\n"
"	\n"
"	border-radius:7px;\n"
"	background-color: #355BA5;\n"
"	color: white\n"
"}")
        self.inp_descricao_product = QLineEdit(self.pag_adicionar_produto)
        self.inp_descricao_product.setObjectName(u"inp_descricao_product")
        self.inp_descricao_product.setGeometry(QRect(130, 450, 491, 20))
        self.inp_descricao_product.setFont(font3)
        self.inp_descricao_product.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.inp_marca_product = QLineEdit(self.pag_adicionar_produto)
        self.inp_marca_product.setObjectName(u"inp_marca_product")
        self.inp_marca_product.setGeometry(QRect(130, 200, 491, 20))
        self.inp_marca_product.setFont(font3)
        self.inp_marca_product.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid #000000;\n"
"	background-color: transparent;\n"
"}")
        self.img_design_lateral = QLabel(self.pag_adicionar_produto)
        self.img_design_lateral.setObjectName(u"img_design_lateral")
        self.img_design_lateral.setGeometry(QRect(690, -10, 81, 601))
        self.img_design_lateral.setPixmap(QPixmap(u":/imagens/Group 49tracinhos.jpg"))
        self.img_design_lateral.setScaledContents(True)
        self.stackedWidget.addWidget(self.pag_adicionar_produto)
        self.pag_retirar_produto = QWidget()
        self.pag_retirar_produto.setObjectName(u"pag_retirar_produto")
        self.frame = QFrame(self.pag_retirar_produto)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, -10, 751, 571))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 120, 261, 16))
        font4 = QFont()
        font4.setPointSize(12)
        self.label.setFont(font4)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(460, 120, 113, 20))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 200, 181, 16))
        self.label_2.setFont(font4)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 280, 47, 13))
        self.label_3.setFont(font4)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 350, 47, 13))
        self.label_4.setFont(font4)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(460, 200, 113, 20))
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(460, 270, 113, 20))
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(460, 350, 113, 20))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 500, 75, 23))
        self.stackedWidget.addWidget(self.pag_retirar_produto)
        self.pag_editar_produto = QWidget()
        self.pag_editar_produto.setObjectName(u"pag_editar_produto")
        self.checkBox = QCheckBox(self.pag_editar_produto)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(190, 240, 70, 17))
        self.stackedWidget.addWidget(self.pag_editar_produto)
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
        self.btn_Relatorio.setStyleSheet(u"\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;")
        self.btn_Relatorio.setFlat(True)
        self.btn_Produtos_ADICIONAR = QPushButton(self.barra_fixa)
        self.btn_Produtos_ADICIONAR.setObjectName(u"btn_Produtos_ADICIONAR")
        self.btn_Produtos_ADICIONAR.setEnabled(True)
        self.btn_Produtos_ADICIONAR.setGeometry(QRect(35, 240, 81, 41))
        self.btn_Produtos_ADICIONAR.setStyleSheet(u"\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;")
        self.btn_Produtos_ADICIONAR.setFlat(True)
        self.btn_Sair = QPushButton(self.barra_fixa)
        self.btn_Sair.setObjectName(u"btn_Sair")
        self.btn_Sair.setGeometry(QRect(25, 553, 75, 23))
        self.btn_Sair.setStyleSheet(u"\n"
"color: white;\n"
"")
        self.btn_Sair.setFlat(True)
        self.btn_Perfil = QPushButton(self.barra_fixa)
        self.btn_Perfil.setObjectName(u"btn_Perfil")
        self.btn_Perfil.setGeometry(QRect(23, 140, 81, 41))
        self.btn_Perfil.setMouseTracking(False)
        self.btn_Perfil.setAutoFillBackground(False)
        self.btn_Perfil.setStyleSheet(u"\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;")
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
        self.btn_Produtos_RETIRAR_QTD.setStyleSheet(u"\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;")
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
        self.btn_Produtos_EDITAR.setStyleSheet(u"\n"
"color: white;\n"
"font-family: Montserrat;\n"
"font-size: 15px;")
        self.btn_Produtos_EDITAR.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.btn_Perfil.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.btn_alterarSenha.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_alterarSenha.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Alterar Senha</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_alterarSenha.setText(QCoreApplication.translate("MainWindow", u"Alterar Senha", None))
        self.inp_novaSenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nova Senha", None))
#if QT_CONFIG(tooltip)
        self.btn_salvarSenha.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_salvarSenha.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Alterar Senha</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_salvarSenha.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.lbl_nomeUsuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Matheus de Matos Nunes</span></p></body></html>", None))
        self.lbl_barraLateral.setText("")
        self.lbl_imagemPerfil.setText("")
        self.lbl_retanguloPretoAzul.setText("")
        self.lbl_emailUsuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Masterm4ts@gmail.com</span></p></body></html>", None))
        self.btn_alterarSenha1.setText(QCoreApplication.translate("MainWindow", u"Alterar Senha", None))
        self.btn_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.img_pesquisar.setText("")
        self.inp_procurarProduto.setText("")
        ___qtablewidgetitem = self.tbl_relatorio.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem1 = self.tbl_relatorio.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"MARCA", None));
        ___qtablewidgetitem2 = self.tbl_relatorio.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem3 = self.tbl_relatorio.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem4 = self.tbl_relatorio.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.tbl_relatorio.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem6 = self.tbl_relatorio.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem7 = self.tbl_relatorio.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));

        __sortingEnabled = self.tbl_relatorio.isSortingEnabled()
        self.tbl_relatorio.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tbl_relatorio.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Luva Descartavel", None));
        ___qtablewidgetitem9 = self.tbl_relatorio.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Farma", None));
        ___qtablewidgetitem10 = self.tbl_relatorio.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"100", None));
        ___qtablewidgetitem11 = self.tbl_relatorio.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Disponivel", None));
        ___qtablewidgetitem12 = self.tbl_relatorio.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Bisturi", None));
        ___qtablewidgetitem13 = self.tbl_relatorio.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Neo", None));
        ___qtablewidgetitem14 = self.tbl_relatorio.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem15 = self.tbl_relatorio.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Em Falta", None));
        ___qtablewidgetitem16 = self.tbl_relatorio.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Jaleco", None));
        ___qtablewidgetitem17 = self.tbl_relatorio.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Quimica", None));
        ___qtablewidgetitem18 = self.tbl_relatorio.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem19 = self.tbl_relatorio.item(2, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Esgotando", None));
        ___qtablewidgetitem20 = self.tbl_relatorio.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Mascara", None));
        ___qtablewidgetitem21 = self.tbl_relatorio.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Arena", None));
        ___qtablewidgetitem22 = self.tbl_relatorio.item(3, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"200", None));
        ___qtablewidgetitem23 = self.tbl_relatorio.item(3, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Disponivel", None));
        self.tbl_relatorio.setSortingEnabled(__sortingEnabled)

        self.btn_salvar_em_pdf.setText(QCoreApplication.translate("MainWindow", u"Salvar em PDF", None))
        self.img_formaRelatorio_2.setText("")
        self.img_formaRelatorio_3.setText("")
        self.img_formaRelatorio_4.setText("")
        self.img_formaRelatorio_5.setText("")
        self.img_formaRelatorio_6.setText("")
        self.img_formaRelatorio_7.setText("")
        self.img_formaRelatorio_8.setText("")
        self.img_formaRelatorio_9.setText("")
        self.img_formaRelatorio.setText("")
        self.inp_nome_product.setText("")
        self.inp_nome_product.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Produto", None))
        self.img_design_baixo.setText("")
        self.inp_quantidade_product.setText("")
        self.inp_quantidade_product.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.btn_registrar_product.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.inp_descricao_product.setText("")
        self.inp_descricao_product.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.inp_marca_product.setText("")
        self.inp_marca_product.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Marca do Produto", None))
        self.img_design_lateral.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Luva", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">50</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Oculos de prote\u00e7\u00e3o", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bisturi", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bota", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">25</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Retirar", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
#if QT_CONFIG(tooltip)
        self.barra_fixa.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbl_Usuario.setText(QCoreApplication.translate("MainWindow", u"Maur\u00edcio", None))
        self.btn_Relatorio.setText(QCoreApplication.translate("MainWindow", u"Rel\u00e1torio", None))
        self.btn_Produtos_ADICIONAR.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_Sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.btn_Perfil.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.btn_Produtos_RETIRAR_QTD.setText(QCoreApplication.translate("MainWindow", u"Retirar", None))
        self.btn_Produtos_EDITAR.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
    # retranslateUi

