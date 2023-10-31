# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Recuperar_senha.ui'
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

class Ui_Recuperar_senha(object):
    def setupUi(self, Recuperar_senha):
        if not Recuperar_senha.objectName():
            Recuperar_senha.setObjectName(u"Recuperar_senha")
        Recuperar_senha.resize(919, 597)
        Recuperar_senha.setMinimumSize(QSize(919, 597))
        Recuperar_senha.setMaximumSize(QSize(919, 597))
        self.centralwidget = QWidget(Recuperar_senha)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(919, 597))
        self.centralwidget.setMaximumSize(QSize(919, 597))
        self.frame_recuperar_senha = QFrame(self.centralwidget)
        self.frame_recuperar_senha.setObjectName(u"frame_recuperar_senha")
        self.frame_recuperar_senha.setGeometry(QRect(280, 120, 371, 371))
        self.frame_recuperar_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_recuperar_senha.setFrameShadow(QFrame.Raised)
        self.btn_recuperar_senha = QPushButton(self.frame_recuperar_senha)
        self.btn_recuperar_senha.setObjectName(u"btn_recuperar_senha")
        self.btn_recuperar_senha.setGeometry(QRect(10, 320, 351, 41))
        self.btn_recuperar_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recuperar_senha.setStyleSheet(u"QPushButton{\n"
"	color : #fffffffff;\n"
"	background-color : #154583;\n"
"	border : none;\n"
"	font-size: 20px;\n"
"	font-style: montserrat;\n"
"}")
        self.retangulo_azul = QLabel(self.frame_recuperar_senha)
        self.retangulo_azul.setObjectName(u"retangulo_azul")
        self.retangulo_azul.setGeometry(QRect(0, 0, 371, 371))
        self.retangulo_azul.setMouseTracking(True)
        self.retangulo_azul.setPixmap(QPixmap(u":/imagens/imagens/Rectangle_18backgroundarealogar-removebg-preview.png"))
        self.retangulo_azul.setScaledContents(True)
        self.retangulo_azul.setWordWrap(False)
        self.inp_senha = QLineEdit(self.frame_recuperar_senha)
        self.inp_senha.setObjectName(u"inp_senha")
        self.inp_senha.setGeometry(QRect(20, 110, 331, 31))
        self.inp_senha.setStyleSheet(u"QLineEdit{\n"
"	border: none; /* Remove a borda padr\u00e3o */\n"
"    border-bottom: 1px solid #fff; /* Adiciona uma borda inferior de 1px s\u00f3lida */\n"
"    background-color: transparent;/* Define o Background como transparente*/\n"
"	color: rgba(255, 255, 255, 0.5);\n"
"	font-size: 19px; /* Defina o tamanho do texto do placeholder desejado */\n"
"	padding-left: 10px;\n"
"	font-style: montserrat;\n"
"}\n"
"\n"
"")
        self.inp_senha.setDragEnabled(False)
        self.inp_senha.setReadOnly(False)
        self.inp_confirma_senha = QLineEdit(self.frame_recuperar_senha)
        self.inp_confirma_senha.setObjectName(u"inp_confirma_senha")
        self.inp_confirma_senha.setGeometry(QRect(20, 180, 331, 31))
        self.inp_confirma_senha.setStyleSheet(u"QLineEdit{\n"
"	border: none; /* Remove a borda padr\u00e3o */\n"
"    border-bottom: 1px solid #fff; /* Adiciona uma borda inferior de 1px s\u00f3lida */\n"
"    background-color: transparent;/* Define o Background como transparente*/\n"
"	color: rgba(255, 255, 255, 0.5);\n"
"	font-size: 19px; /* Defina o tamanho do texto do placeholder desejado */\n"
"	padding-left: 10px;\n"
"	font-style: montserrat;\n"
"}\n"
"\n"
"")
        self.lbl_estoque_medico = QLabel(self.frame_recuperar_senha)
        self.lbl_estoque_medico.setObjectName(u"lbl_estoque_medico")
        self.lbl_estoque_medico.setGeometry(QRect(0, 20, 371, 31))
        self.lbl_estoque_medico.setStyleSheet(u"")
        self.retangulo_azul.raise_()
        self.btn_recuperar_senha.raise_()
        self.inp_senha.raise_()
        self.inp_confirma_senha.raise_()
        self.lbl_estoque_medico.raise_()
        self.img_medico = QLabel(self.centralwidget)
        self.img_medico.setObjectName(u"img_medico")
        self.img_medico.setGeometry(QRect(-80, 0, 1011, 601))
        self.img_medico.setPixmap(QPixmap(u"imagens/image 4imagem_medico.jpg"))
        self.img_medico.setScaledContents(True)
        self.efeito_hub_academy = QLabel(self.centralwidget)
        self.efeito_hub_academy.setObjectName(u"efeito_hub_academy")
        self.efeito_hub_academy.setGeometry(QRect(130, -20, 331, 271))
        self.efeito_hub_academy.setPixmap(QPixmap(u":/imagens/imagens/Group_37hubacademyefeito-removebg-preview.png"))
        self.efeito_hub_academy.setScaledContents(True)
        self.efeito_traseiro = QLabel(self.centralwidget)
        self.efeito_traseiro.setObjectName(u"efeito_traseiro")
        self.efeito_traseiro.setGeometry(QRect(640, 380, 47, 111))
        self.efeito_traseiro.setPixmap(QPixmap(u":/imagens/imagens/Frame_1efeitoatrasdaarealogar-removebg-preview.png"))
        self.efeito_traseiro.setScaledContents(True)
        self.img_lateral_azul = QLabel(self.centralwidget)
        self.img_lateral_azul.setObjectName(u"img_lateral_azul")
        self.img_lateral_azul.setGeometry(QRect(0, 0, 61, 611))
        self.img_lateral_azul.setPixmap(QPixmap(u":/imagens/imagens/Group_36barraladoesquerdo_login-removebg-preview.png"))
        self.img_lateral_azul.setScaledContents(True)
        self.img_lateral_direita = QLabel(self.centralwidget)
        self.img_lateral_direita.setObjectName(u"img_lateral_direita")
        self.img_lateral_direita.setGeometry(QRect(900, 0, 71, 611))
        self.img_lateral_direita.setPixmap(QPixmap(u":/imagens/imagens/Group 10desenhoesquerdo_login.jpg"))
        self.img_lateral_direita.setScaledContents(True)
        Recuperar_senha.setCentralWidget(self.centralwidget)
        self.img_medico.raise_()
        self.efeito_hub_academy.raise_()
        self.efeito_traseiro.raise_()
        self.img_lateral_azul.raise_()
        self.img_lateral_direita.raise_()
        self.frame_recuperar_senha.raise_()

        self.retranslateUi(Recuperar_senha)

        QMetaObject.connectSlotsByName(Recuperar_senha)
    # setupUi

    def retranslateUi(self, Recuperar_senha):
        Recuperar_senha.setWindowTitle(QCoreApplication.translate("Recuperar_senha", u"MainWindow", None))
        self.btn_recuperar_senha.setText(QCoreApplication.translate("Recuperar_senha", u"Recuperar Senha", None))
        self.retangulo_azul.setText("")
        self.inp_senha.setText("")
        self.inp_senha.setPlaceholderText(QCoreApplication.translate("Recuperar_senha", u"Senha", None))
        self.inp_confirma_senha.setText("")
        self.inp_confirma_senha.setPlaceholderText(QCoreApplication.translate("Recuperar_senha", u"Confirmar Senha", None))
        self.lbl_estoque_medico.setText(QCoreApplication.translate("Recuperar_senha", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Estoque M\u00e9dico</span></p></body></html>", None))
        self.img_medico.setText("")
        self.efeito_hub_academy.setText("")
        self.efeito_traseiro.setText("")
        self.img_lateral_azul.setText("")
        self.img_lateral_direita.setText("")
    # retranslateUi

