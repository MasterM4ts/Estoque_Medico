# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Confirmar_Senha.ui'
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

class Ui_Confirmar_Senha(object):
    def setupUi(self, Confirmar_Senha):
        if not Confirmar_Senha.objectName():
            Confirmar_Senha.setObjectName(u"Confirmar_Senha")
        Confirmar_Senha.resize(914, 587)
        self.centralwidget = QWidget(Confirmar_Senha)
        self.centralwidget.setObjectName(u"centralwidget")
        self.img_medico_fundo = QLabel(self.centralwidget)
        self.img_medico_fundo.setObjectName(u"img_medico_fundo")
        self.img_medico_fundo.setGeometry(QRect(-80, 0, 1001, 601))
        self.img_medico_fundo.setPixmap(QPixmap(u":/imagens/image 4imagem_medico.jpg"))
        self.img_medico_fundo.setScaledContents(True)
        self.frame_recuperar_senha = QFrame(self.centralwidget)
        self.frame_recuperar_senha.setObjectName(u"frame_recuperar_senha")
        self.frame_recuperar_senha.setGeometry(QRect(280, 120, 371, 371))
        self.frame_recuperar_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_recuperar_senha.setFrameShadow(QFrame.Raised)
        self.label_retangulo = QLabel(self.frame_recuperar_senha)
        self.label_retangulo.setObjectName(u"label_retangulo")
        self.label_retangulo.setGeometry(QRect(0, 0, 371, 371))
        self.label_retangulo.setPixmap(QPixmap(u":/imagens/imagens/Rectangle_18backgroundarealogar-removebg-preview.png"))
        self.label_retangulo.setScaledContents(True)
        self.label_estoque_medico = QLabel(self.frame_recuperar_senha)
        self.label_estoque_medico.setObjectName(u"label_estoque_medico")
        self.label_estoque_medico.setGeometry(QRect(6, 10, 361, 61))
        self.lineEdit_senha = QLineEdit(self.frame_recuperar_senha)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(10, 160, 351, 31))
        self.lineEdit_senha.setStyleSheet(u"QLineEdit{\n"
"   border:none;\n"
"   border-bottom: 1px solid #fff; \n"
"   background-color: transparent;\n"
"   color:#fff;\n"
"   font-size: 20px;\n"
"   padding-left: 10px;\n"
"\n"
"}")
        self.lineEdit_confirmar_senha = QLineEdit(self.frame_recuperar_senha)
        self.lineEdit_confirmar_senha.setObjectName(u"lineEdit_confirmar_senha")
        self.lineEdit_confirmar_senha.setGeometry(QRect(10, 220, 351, 31))
        self.lineEdit_confirmar_senha.setStyleSheet(u"QLineEdit{\n"
"   border:none;\n"
"   border-bottom: 1px solid #fff; \n"
"   background-color: transparent;\n"
"   color:#fff;\n"
"   font-size: 20px;\n"
"   padding-left: 10px;\n"
"\n"
"}")
        self.Button_confirmar_senha = QPushButton(self.frame_recuperar_senha)
        self.Button_confirmar_senha.setObjectName(u"Button_confirmar_senha")
        self.Button_confirmar_senha.setGeometry(QRect(10, 320, 351, 41))
        self.Button_confirmar_senha.setStyleSheet(u"QPushButton{\n"
"	color : #fffffffff;\n"
"	background-color : #154583;\n"
"	border : none;\n"
"	font-size: 20px;\n"
"	font-style: montserrat;\n"
"}")
        self.label_retangulo.raise_()
        self.lineEdit_senha.raise_()
        self.lineEdit_confirmar_senha.raise_()
        self.Button_confirmar_senha.raise_()
        self.label_estoque_medico.raise_()
        self.lateral_esquerda = QLabel(self.centralwidget)
        self.lateral_esquerda.setObjectName(u"lateral_esquerda")
        self.lateral_esquerda.setGeometry(QRect(0, 0, 61, 611))
        self.lateral_esquerda.setPixmap(QPixmap(u":/imagens/imagens/barra_lateral_esquerda.png"))
        self.lateral_esquerda.setScaledContents(True)
        self.label_efeito_senac_hub = QLabel(self.centralwidget)
        self.label_efeito_senac_hub.setObjectName(u"label_efeito_senac_hub")
        self.label_efeito_senac_hub.setGeometry(QRect(130, -20, 331, 271))
        self.label_efeito_senac_hub.setPixmap(QPixmap(u":/imagens/imagens/Group_37hubacademyefeito-removebg-preview.png"))
        self.label_efeito_senac_hub.setScaledContents(True)
        self.lateral_direita = QLabel(self.centralwidget)
        self.lateral_direita.setObjectName(u"lateral_direita")
        self.lateral_direita.setGeometry(QRect(900, 0, 61, 611))
        self.lateral_direita.setPixmap(QPixmap(u":/imagens/imagens/Group 10desenhoesquerdo_login.jpg"))
        self.lateral_direita.setScaledContents(True)
        self.label_efeito_traseiro = QLabel(self.centralwidget)
        self.label_efeito_traseiro.setObjectName(u"label_efeito_traseiro")
        self.label_efeito_traseiro.setGeometry(QRect(640, 380, 47, 111))
        self.label_efeito_traseiro.setPixmap(QPixmap(u":/imagens/imagens/Frame_1efeitoatrasdaarealogar-removebg-preview.png"))
        self.label_efeito_traseiro.setScaledContents(True)
        Confirmar_Senha.setCentralWidget(self.centralwidget)
        self.img_medico_fundo.raise_()
        self.lateral_esquerda.raise_()
        self.label_efeito_senac_hub.raise_()
        self.frame_recuperar_senha.raise_()
        self.lateral_direita.raise_()
        self.label_efeito_traseiro.raise_()

        self.retranslateUi(Confirmar_Senha)

        QMetaObject.connectSlotsByName(Confirmar_Senha)
    # setupUi

    def retranslateUi(self, Confirmar_Senha):
        Confirmar_Senha.setWindowTitle(QCoreApplication.translate("Confirmar_Senha", u"MainWindow", None))
        self.img_medico_fundo.setText("")
        self.label_retangulo.setText("")
        self.label_estoque_medico.setText(QCoreApplication.translate("Confirmar_Senha", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Estoque M\u00e9dico</span></p></body></html>", None))
        self.lineEdit_senha.setPlaceholderText(QCoreApplication.translate("Confirmar_Senha", u"Senha", None))
        self.lineEdit_confirmar_senha.setPlaceholderText(QCoreApplication.translate("Confirmar_Senha", u"Confirmar Senha", None))
        self.Button_confirmar_senha.setText(QCoreApplication.translate("Confirmar_Senha", u"Confirmar Senha", None))
        self.lateral_esquerda.setText("")
        self.label_efeito_senac_hub.setText("")
        self.lateral_direita.setText("")
        self.label_efeito_traseiro.setText("")
    # retranslateUi

