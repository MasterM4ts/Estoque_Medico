# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Esqueceu_Senha.ui'
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

class Ui_Esqueceu_Senha(object):
    def setupUi(self, Esqueceu_Senha):
        if not Esqueceu_Senha.objectName():
            Esqueceu_Senha.setObjectName(u"Esqueceu_Senha")
        Esqueceu_Senha.resize(919, 597)
        Esqueceu_Senha.setMinimumSize(QSize(919, 597))
        Esqueceu_Senha.setMaximumSize(QSize(919, 597))
        self.centralwidget = QWidget(Esqueceu_Senha)
        self.centralwidget.setObjectName(u"centralwidget")
        self.img_medico = QLabel(self.centralwidget)
        self.img_medico.setObjectName(u"img_medico")
        self.img_medico.setGeometry(QRect(-80, 0, 1011, 601))
        self.img_medico.setPixmap(QPixmap(u"imagens/image 4imagem_medico.jpg"))
        self.img_medico.setScaledContents(True)
        self.frame_esqueceu_senha = QFrame(self.centralwidget)
        self.frame_esqueceu_senha.setObjectName(u"frame_esqueceu_senha")
        self.frame_esqueceu_senha.setGeometry(QRect(280, 120, 371, 371))
        self.frame_esqueceu_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_esqueceu_senha.setFrameShadow(QFrame.Raised)
        self.retangulo_azul = QLabel(self.frame_esqueceu_senha)
        self.retangulo_azul.setObjectName(u"retangulo_azul")
        self.retangulo_azul.setGeometry(QRect(0, 0, 371, 371))
        self.retangulo_azul.setMouseTracking(True)
        self.retangulo_azul.setPixmap(QPixmap(u":/imagens/imagens/Rectangle_18backgroundarealogar-removebg-preview.png"))
        self.retangulo_azul.setScaledContents(True)
        self.retangulo_azul.setWordWrap(False)
        self.label_recuperarsenha = QLabel(self.frame_esqueceu_senha)
        self.label_recuperarsenha.setObjectName(u"label_recuperarsenha")
        self.label_recuperarsenha.setGeometry(QRect(6, 10, 361, 31))
        font = QFont()
        font.setPointSize(20)
        self.label_recuperarsenha.setFont(font)
        self.lineEdit_email = QLineEdit(self.frame_esqueceu_senha)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(10, 160, 351, 31))
        self.lineEdit_email.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"    border-bottom:1px solid #fff;\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-size: 20px;\n"
"    padding-left: 10px;\n"
"  \n"
"}")
        self.lineEdit_email.setEchoMode(QLineEdit.Normal)
        self.lineEdit_email.setClearButtonEnabled(False)
        self.btn_Enviar = QPushButton(self.frame_esqueceu_senha)
        self.btn_Enviar.setObjectName(u"btn_Enviar")
        self.btn_Enviar.setGeometry(QRect(10, 320, 351, 41))
        self.btn_Enviar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Enviar.setStyleSheet(u"QPushButton{\n"
"	color : #fffffffff;\n"
"	background-color : #154583;\n"
"	border : none;\n"
"	font-size: 20px;\n"
"	font-style: montserrat;\n"
"}")
        self.efeito_hub_academy = QLabel(self.centralwidget)
        self.efeito_hub_academy.setObjectName(u"efeito_hub_academy")
        self.efeito_hub_academy.setGeometry(QRect(130, -20, 331, 271))
        self.efeito_hub_academy.setPixmap(QPixmap(u":/imagens/imagens/Group_37hubacademyefeito-removebg-preview.png"))
        self.efeito_hub_academy.setScaledContents(True)
        self.lateral_azul = QLabel(self.centralwidget)
        self.lateral_azul.setObjectName(u"lateral_azul")
        self.lateral_azul.setGeometry(QRect(0, 0, 61, 611))
        self.lateral_azul.setPixmap(QPixmap(u":/imagens/imagens/Group_36barraladoesquerdo_login-removebg-preview.png"))
        self.lateral_azul.setScaledContents(True)
        self.efeito_traseiro = QLabel(self.centralwidget)
        self.efeito_traseiro.setObjectName(u"efeito_traseiro")
        self.efeito_traseiro.setGeometry(QRect(640, 380, 47, 111))
        self.efeito_traseiro.setPixmap(QPixmap(u":/imagens/imagens/Frame_1efeitoatrasdaarealogar-removebg-preview.png"))
        self.efeito_traseiro.setScaledContents(True)
        self.lateral_direita = QLabel(self.centralwidget)
        self.lateral_direita.setObjectName(u"lateral_direita")
        self.lateral_direita.setGeometry(QRect(910, 0, 61, 611))
        self.lateral_direita.setPixmap(QPixmap(u":/imagens/imagens/Group 10desenhoesquerdo_login.jpg"))
        self.lateral_direita.setScaledContents(True)
        Esqueceu_Senha.setCentralWidget(self.centralwidget)
        self.img_medico.raise_()
        self.efeito_hub_academy.raise_()
        self.frame_esqueceu_senha.raise_()
        self.lateral_azul.raise_()
        self.efeito_traseiro.raise_()
        self.lateral_direita.raise_()

        self.retranslateUi(Esqueceu_Senha)

        QMetaObject.connectSlotsByName(Esqueceu_Senha)
    # setupUi

    def retranslateUi(self, Esqueceu_Senha):
        Esqueceu_Senha.setWindowTitle(QCoreApplication.translate("Esqueceu_Senha", u"MainWindow", None))
        self.img_medico.setText("")
        self.retangulo_azul.setText("")
        self.label_recuperarsenha.setText(QCoreApplication.translate("Esqueceu_Senha", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Recuperar Senha</span></p></body></html>", None))
        self.lineEdit_email.setInputMask("")
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Esqueceu_Senha", u"E-mail", None))
        self.btn_Enviar.setText(QCoreApplication.translate("Esqueceu_Senha", u"Enviar", None))
        self.efeito_hub_academy.setText("")
        self.lateral_azul.setText("")
        self.efeito_traseiro.setText("")
        self.lateral_direita.setText("")
    # retranslateUi

