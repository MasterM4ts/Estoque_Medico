# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import QRC_login_rc
import QRC_login_rc

class Ui_Tela_login(object):
    def setupUi(self, Tela_login):
        if not Tela_login.objectName():
            Tela_login.setObjectName(u"Tela_login")
        Tela_login.resize(919, 597)
        Tela_login.setMaximumSize(QSize(919, 597))
        Tela_login.setMouseTracking(False)
        Tela_login.setStyleSheet(u"")
        self.centralwidget = QWidget(Tela_login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.img_efeitoladoesquerdologin = QLabel(self.centralwidget)
        self.img_efeitoladoesquerdologin.setObjectName(u"img_efeitoladoesquerdologin")
        self.img_efeitoladoesquerdologin.setGeometry(QRect(0, -10, 61, 611))
        self.img_efeitoladoesquerdologin.setCursor(QCursor(Qt.ArrowCursor))
        self.img_efeitoladoesquerdologin.setStyleSheet(u"")
        self.img_efeitoladoesquerdologin.setPixmap(QPixmap(u":/imagens/imagens/Group_36barraladoesquerdo_login-removebg-preview.png"))
        self.img_efeitoladoesquerdologin.setScaledContents(True)
        self.img_backgroundlogin = QLabel(self.centralwidget)
        self.img_backgroundlogin.setObjectName(u"img_backgroundlogin")
        self.img_backgroundlogin.setGeometry(QRect(0, 0, 961, 601))
        self.img_backgroundlogin.setCursor(QCursor(Qt.ArrowCursor))
        self.img_backgroundlogin.setPixmap(QPixmap(u":/imagens/imagens/medica_imagemlogin.jpg"))
        self.img_backgroundlogin.setScaledContents(True)
        self.frame_arealogar = QFrame(self.centralwidget)
        self.frame_arealogar.setObjectName(u"frame_arealogar")
        self.frame_arealogar.setGeometry(QRect(280, 120, 371, 371))
        self.frame_arealogar.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_arealogar.setFrameShape(QFrame.StyledPanel)
        self.frame_arealogar.setFrameShadow(QFrame.Raised)
        self.img_backgroundarealogar = QLabel(self.frame_arealogar)
        self.img_backgroundarealogar.setObjectName(u"img_backgroundarealogar")
        self.img_backgroundarealogar.setGeometry(QRect(0, 0, 371, 371))
        self.img_backgroundarealogar.setCursor(QCursor(Qt.ArrowCursor))
        self.img_backgroundarealogar.setPixmap(QPixmap(u":/imagens/imagens/Rectangle_18backgroundarealogar-removebg-preview.png"))
        self.img_backgroundarealogar.setScaledContents(True)
        self.input_emaillogin = QLineEdit(self.frame_arealogar)
        self.input_emaillogin.setObjectName(u"input_emaillogin")
        self.input_emaillogin.setGeometry(QRect(10, 100, 351, 31))
        self.input_emaillogin.setCursor(QCursor(Qt.IBeamCursor))
        self.input_emaillogin.setStyleSheet(u"QLineEdit{\n"
"	border: none; /* Remove a borda padr\u00e3o */\n"
"    border-bottom: 1px solid #fff; /* Adiciona uma borda inferior de 1px s\u00f3lida */\n"
"    background-color: transparent;/* Define o Background como transparente*/\n"
"	color: #fffffffff;\n"
"	font-size: 20px; /* Defina o tamanho do texto do placeholder desejado */\n"
"	padding-left: 10px;\n"
"	font-style: montserrat;\n"
"}\n"
"\n"
"")
        self.input_emaillogin.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.input_emaillogin.setDragEnabled(False)
        self.input_emaillogin.setReadOnly(False)
        self.input_emaillogin.setPlaceholderText(u"E-mail")
        self.lbl_tituloestoque = QLabel(self.frame_arealogar)
        self.lbl_tituloestoque.setObjectName(u"lbl_tituloestoque")
        self.lbl_tituloestoque.setGeometry(QRect(6, 10, 361, 31))
        font = QFont()
        font.setPointSize(20)
        self.lbl_tituloestoque.setFont(font)
        self.lbl_tituloestoque.setCursor(QCursor(Qt.ArrowCursor))
        self.lbl_tituloestoque.setStyleSheet(u"font-style: montserrat;")
        self.input_senhalogin = QLineEdit(self.frame_arealogar)
        self.input_senhalogin.setObjectName(u"input_senhalogin")
        self.input_senhalogin.setGeometry(QRect(10, 180, 351, 31))
        self.input_senhalogin.setStyleSheet(u"QLineEdit{\n"
"	border: none; /* Remove a borda padr\u00e3o */\n"
"    border-bottom: 1px solid #fff; /* Adiciona uma borda inferior de 1px s\u00f3lida */\n"
"    background-color: transparent;/* Define o Background como transparente*/\n"
"	color: #fffffffff;\n"
"	font-size: 20px; /* Defina o tamanho do texto do placeholder desejado */\n"
"	padding-left: 10px;\n"
"	font-style: montserrat;\n"
"}\n"
"\n"
"")
        self.input_senhalogin.setEchoMode(QLineEdit.Password)
        self.input_senhalogin.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.input_senhalogin.setDragEnabled(False)
        self.input_senhalogin.setReadOnly(False)
        self.input_senhalogin.setPlaceholderText(u"Senha")
        self.btn_logar = QPushButton(self.frame_arealogar)
        self.btn_logar.setObjectName(u"btn_logar")
        self.btn_logar.setGeometry(QRect(10, 320, 351, 41))
        self.btn_logar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logar.setStyleSheet(u"QPushButton{\n"
"	color : #fffffffff;\n"
"	background-color : #154583;\n"
"	border : none;\n"
"	font-size: 20px;\n"
"	font-style: montserrat;\n"
"}")
        self.btn_esqueceusenha = QPushButton(self.frame_arealogar)
        self.btn_esqueceusenha.setObjectName(u"btn_esqueceusenha")
        self.btn_esqueceusenha.setGeometry(QRect(130, 240, 121, 23))
        self.btn_esqueceusenha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_esqueceusenha.setMouseTracking(True)
        self.btn_esqueceusenha.setStyleSheet(u"QPushButton{\n"
"	border : none;\n"
"	color : #ffffffff;\n"
"	text-decoration: underline;\n"
"	font-size: 12px;\n"
"	font-style: montserrat;\n"
"}")
        self.btn_cadastrar = QPushButton(self.frame_arealogar)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(210, 270, 81, 23))
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setMouseTracking(True)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	border : none;\n"
"	color : #ffffffff;\n"
"	text-decoration: underline;\n"
"	font-size: 12px;\n"
"	font-style: montserrat;\n"
"}")
        self.label = QLabel(self.frame_arealogar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 270, 121, 23))
        self.label.setCursor(QCursor(Qt.ArrowCursor))
        self.label.setStyleSheet(u"QLabel{\n"
"\n"
"	border : none;\n"
"	color : #ffffffff;\n"
"	font-size: 12px;\n"
"	font-style: montserrat;\n"
"}")
        self.img_efeitohubacademylogin = QLabel(self.centralwidget)
        self.img_efeitohubacademylogin.setObjectName(u"img_efeitohubacademylogin")
        self.img_efeitohubacademylogin.setGeometry(QRect(500, -10, 331, 271))
        self.img_efeitohubacademylogin.setCursor(QCursor(Qt.ArrowCursor))
        self.img_efeitohubacademylogin.setPixmap(QPixmap(u":/imagens/imagens/Group_37hubacademyefeito-removebg-preview.png"))
        self.img_efeitohubacademylogin.setScaledContents(True)
        self.img_efeitotraseiroarelogar = QLabel(self.centralwidget)
        self.img_efeitotraseiroarelogar.setObjectName(u"img_efeitotraseiroarelogar")
        self.img_efeitotraseiroarelogar.setGeometry(QRect(640, 380, 47, 111))
        self.img_efeitotraseiroarelogar.setCursor(QCursor(Qt.ArrowCursor))
        self.img_efeitotraseiroarelogar.setPixmap(QPixmap(u":/imagens/imagens/Frame_1efeitoatrasdaarealogar-removebg-preview.png"))
        self.img_efeitotraseiroarelogar.setScaledContents(True)
        Tela_login.setCentralWidget(self.centralwidget)
        self.img_backgroundlogin.raise_()
        self.img_efeitotraseiroarelogar.raise_()
        self.img_efeitohubacademylogin.raise_()
        self.img_efeitoladoesquerdologin.raise_()
        self.frame_arealogar.raise_()

        self.retranslateUi(Tela_login)

        QMetaObject.connectSlotsByName(Tela_login)
    # setupUi

    def retranslateUi(self, Tela_login):
        Tela_login.setWindowTitle(QCoreApplication.translate("Tela_login", u"MainWindow", None))
        self.img_efeitoladoesquerdologin.setText("")
        self.img_backgroundlogin.setText("")
        self.img_backgroundarealogar.setText("")
        self.input_emaillogin.setText("")
#if QT_CONFIG(tooltip)
        self.lbl_tituloestoque.setToolTip(QCoreApplication.translate("Tela_login", u"<html><head/><body><p><span style=\" font-size:12pt;\">u8-p</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lbl_tituloestoque.setWhatsThis(QCoreApplication.translate("Tela_login", u"<html><head/><body><p>sdfwesf</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lbl_tituloestoque.setText(QCoreApplication.translate("Tela_login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Estoque M\u00e9dico</span></p></body></html>", None))
        self.input_senhalogin.setText("")
        self.btn_logar.setText(QCoreApplication.translate("Tela_login", u"Login", None))
        self.btn_esqueceusenha.setText(QCoreApplication.translate("Tela_login", u"Esqueceu a senha?", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastrar.setToolTip(QCoreApplication.translate("Tela_login", u"<html><head/><body><p>Cadastrar-se</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cadastrar.setText(QCoreApplication.translate("Tela_login", u"Cadastre-se", None))
        self.label.setText(QCoreApplication.translate("Tela_login", u"N\u00e3o tem uma conta?", None))
        self.img_efeitohubacademylogin.setText("")
        self.img_efeitotraseiroarelogar.setText("")
    # retranslateUi

