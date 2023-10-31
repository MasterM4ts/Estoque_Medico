# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Cadastrar.ui'
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

class Ui_Tela_Cadastrar(object):
    def setupUi(self, Tela_Cadastrar):
        if not Tela_Cadastrar.objectName():
            Tela_Cadastrar.setObjectName(u"Tela_Cadastrar")
        Tela_Cadastrar.resize(919, 597)
        Tela_Cadastrar.setMinimumSize(QSize(919, 597))
        Tela_Cadastrar.setMaximumSize(QSize(919, 597))
        Tela_Cadastrar.setMouseTracking(False)
        Tela_Cadastrar.setStyleSheet(u"")
        self.centralwidget = QWidget(Tela_Cadastrar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_area_cadastrar = QFrame(self.centralwidget)
        self.frame_area_cadastrar.setObjectName(u"frame_area_cadastrar")
        self.frame_area_cadastrar.setGeometry(QRect(270, 90, 371, 411))
        self.frame_area_cadastrar.setFrameShape(QFrame.StyledPanel)
        self.frame_area_cadastrar.setFrameShadow(QFrame.Raised)
        self.img_backgroud_cadastrar = QLabel(self.frame_area_cadastrar)
        self.img_backgroud_cadastrar.setObjectName(u"img_backgroud_cadastrar")
        self.img_backgroud_cadastrar.setGeometry(QRect(0, 0, 371, 411))
        self.img_backgroud_cadastrar.setPixmap(QPixmap(u":/imagens/imagens/Rectangle_18backgroundarealogar-removebg-preview.png"))
        self.img_backgroud_cadastrar.setScaledContents(True)
        self.btn_cadastrar = QPushButton(self.frame_area_cadastrar)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(10, 350, 351, 41))
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color : #fffffffff;\n"
"	background-color : #154583;\n"
"	border : none;\n"
"	font-size: 20px;\n"
"	font-style: montserrat;\n"
"}")
        self.inp_email_cadastrar = QLineEdit(self.frame_area_cadastrar)
        self.inp_email_cadastrar.setObjectName(u"inp_email_cadastrar")
        self.inp_email_cadastrar.setGeometry(QRect(10, 180, 351, 31))
        self.inp_email_cadastrar.setStyleSheet(u"QLineEdit{\n"
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
        self.inp_email_cadastrar.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.inp_email_cadastrar.setDragEnabled(False)
        self.inp_email_cadastrar.setReadOnly(False)
        self.inp_email_cadastrar.setPlaceholderText(u"E-mail")
        self.inp_nome_cadastrar = QLineEdit(self.frame_area_cadastrar)
        self.inp_nome_cadastrar.setObjectName(u"inp_nome_cadastrar")
        self.inp_nome_cadastrar.setGeometry(QRect(10, 110, 351, 31))
        self.inp_nome_cadastrar.setStyleSheet(u"QLineEdit{\n"
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
        self.inp_nome_cadastrar.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.inp_nome_cadastrar.setDragEnabled(False)
        self.inp_nome_cadastrar.setReadOnly(False)
        self.inp_nome_cadastrar.setPlaceholderText(u"Nome")
        self.inp_senha_cadastrar_2 = QLineEdit(self.frame_area_cadastrar)
        self.inp_senha_cadastrar_2.setObjectName(u"inp_senha_cadastrar_2")
        self.inp_senha_cadastrar_2.setGeometry(QRect(10, 250, 351, 31))
        self.inp_senha_cadastrar_2.setStyleSheet(u"QLineEdit{\n"
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
        self.inp_senha_cadastrar_2.setMaxLength(13)
        self.inp_senha_cadastrar_2.setEchoMode(QLineEdit.Password)
        self.inp_senha_cadastrar_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.inp_senha_cadastrar_2.setDragEnabled(False)
        self.inp_senha_cadastrar_2.setReadOnly(False)
        self.inp_senha_cadastrar_2.setPlaceholderText(u"Senha")
        self.lbl_cadastrar_usuario = QLabel(self.frame_area_cadastrar)
        self.lbl_cadastrar_usuario.setObjectName(u"lbl_cadastrar_usuario")
        self.lbl_cadastrar_usuario.setGeometry(QRect(10, 20, 361, 31))
        font = QFont()
        font.setPointSize(20)
        self.lbl_cadastrar_usuario.setFont(font)
        self.lbl_cadastrar_usuario.setStyleSheet(u"font-style: montserrat;")
        self.img_background = QLabel(self.centralwidget)
        self.img_background.setObjectName(u"img_background")
        self.img_background.setGeometry(QRect(0, 0, 919, 597))
        self.img_background.setMaximumSize(QSize(919, 597))
        self.img_background.setPixmap(QPixmap(u"imagens/cadastra usuario.png"))
        self.img_background.setScaledContents(True)
        self.img_barra_lateral_esquerda = QLabel(self.centralwidget)
        self.img_barra_lateral_esquerda.setObjectName(u"img_barra_lateral_esquerda")
        self.img_barra_lateral_esquerda.setGeometry(QRect(0, 0, 51, 601))
        self.img_barra_lateral_esquerda.setPixmap(QPixmap(u"imagens/barra_lateral_esquerda.png"))
        self.img_barra_lateral_esquerda.setScaledContents(True)
        self.img_barra_lateral_direita = QLabel(self.centralwidget)
        self.img_barra_lateral_direita.setObjectName(u"img_barra_lateral_direita")
        self.img_barra_lateral_direita.setGeometry(QRect(850, 0, 71, 601))
        self.img_barra_lateral_direita.setPixmap(QPixmap(u"imagens/barra_lateral_direita.png"))
        self.img_barra_lateral_direita.setScaledContents(True)
        self.img_logo_hub_1 = QLabel(self.centralwidget)
        self.img_logo_hub_1.setObjectName(u"img_logo_hub_1")
        self.img_logo_hub_1.setGeometry(QRect(90, 310, 351, 281))
        self.img_logo_hub_1.setPixmap(QPixmap(u"imagens/Group_37hubacademyefeito-removebg-preview.png"))
        self.img_logo_hub_1.setScaledContents(True)
        self.img_logo_hub_2 = QLabel(self.centralwidget)
        self.img_logo_hub_2.setObjectName(u"img_logo_hub_2")
        self.img_logo_hub_2.setGeometry(QRect(470, 150, 351, 281))
        self.img_logo_hub_2.setPixmap(QPixmap(u"imagens/Group_37hubacademyefeito-removebg-preview.png"))
        self.img_logo_hub_2.setScaledContents(True)
        Tela_Cadastrar.setCentralWidget(self.centralwidget)
        self.img_background.raise_()
        self.img_logo_hub_2.raise_()
        self.img_logo_hub_1.raise_()
        self.frame_area_cadastrar.raise_()
        self.img_barra_lateral_esquerda.raise_()
        self.img_barra_lateral_direita.raise_()

        self.retranslateUi(Tela_Cadastrar)

        QMetaObject.connectSlotsByName(Tela_Cadastrar)
    # setupUi

    def retranslateUi(self, Tela_Cadastrar):
        Tela_Cadastrar.setWindowTitle(QCoreApplication.translate("Tela_Cadastrar", u"MainWindow", None))
        self.img_backgroud_cadastrar.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("Tela_Cadastrar", u"Cadastre-se", None))
        self.inp_email_cadastrar.setText("")
        self.inp_nome_cadastrar.setText("")
        self.inp_senha_cadastrar_2.setText("")
#if QT_CONFIG(tooltip)
        self.lbl_cadastrar_usuario.setToolTip(QCoreApplication.translate("Tela_Cadastrar", u"<html><head/><body><p><span style=\" font-size:12pt;\">u8-p</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lbl_cadastrar_usuario.setWhatsThis(QCoreApplication.translate("Tela_Cadastrar", u"<html><head/><body><p>sdfwesf</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lbl_cadastrar_usuario.setText(QCoreApplication.translate("Tela_Cadastrar", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Cadastrar Usu\u00e1rio</span></p></body></html>", None))
        self.img_background.setText("")
        self.img_barra_lateral_esquerda.setText("")
        self.img_barra_lateral_direita.setText("")
        self.img_logo_hub_1.setText("")
        self.img_logo_hub_2.setText("")
    # retranslateUi

