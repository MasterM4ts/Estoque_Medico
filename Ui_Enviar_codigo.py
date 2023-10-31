# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Enviar_codigo.ui'
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

class Ui_Enviar_Codigo(object):
    def setupUi(self, Enviar_Codigo):
        if not Enviar_Codigo.objectName():
            Enviar_Codigo.setObjectName(u"Enviar_Codigo")
        Enviar_Codigo.resize(919, 597)
        Enviar_Codigo.setMinimumSize(QSize(919, 597))
        Enviar_Codigo.setMaximumSize(QSize(919, 597))
        self.centralwidget = QWidget(Enviar_Codigo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.img_imagem_medico = QLabel(self.centralwidget)
        self.img_imagem_medico.setObjectName(u"img_imagem_medico")
        self.img_imagem_medico.setGeometry(QRect(-80, 0, 1011, 601))
        self.img_imagem_medico.setPixmap(QPixmap(u"imagens/image 4imagem_medico.jpg"))
        self.img_imagem_medico.setScaledContents(True)
        self.framecodigo_para_confirmar = QFrame(self.centralwidget)
        self.framecodigo_para_confirmar.setObjectName(u"framecodigo_para_confirmar")
        self.framecodigo_para_confirmar.setGeometry(QRect(280, 120, 371, 371))
        self.framecodigo_para_confirmar.setFrameShape(QFrame.StyledPanel)
        self.framecodigo_para_confirmar.setFrameShadow(QFrame.Raised)
        self.label_codigo = QLabel(self.framecodigo_para_confirmar)
        self.label_codigo.setObjectName(u"label_codigo")
        self.label_codigo.setGeometry(QRect(-10, 0, 381, 371))
        self.label_codigo.setPixmap(QPixmap(u":/imagens/imagens/Rectangle_18backgroundarealogar-removebg-preview.png"))
        self.label_codigo.setScaledContents(True)
        self.label_estoque_medico = QLabel(self.framecodigo_para_confirmar)
        self.label_estoque_medico.setObjectName(u"label_estoque_medico")
        self.label_estoque_medico.setGeometry(QRect(80, 30, 201, 61))
        self.label_estoque_medico.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"    border-bottom:1px solid #fff;\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-size: 20px;\n"
"    padding-left: 10px;\n"
"  \n"
"}")
        self.lineEdit_inserir_codigo = QLineEdit(self.framecodigo_para_confirmar)
        self.lineEdit_inserir_codigo.setObjectName(u"lineEdit_inserir_codigo")
        self.lineEdit_inserir_codigo.setGeometry(QRect(10, 160, 351, 31))
        self.lineEdit_inserir_codigo.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"    border-bottom:1px solid #fff;\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-size: 20px;\n"
"    padding-left: 10px;\n"
"  \n"
"}")
        self.btn_enviar_codigo = QPushButton(self.framecodigo_para_confirmar)
        self.btn_enviar_codigo.setObjectName(u"btn_enviar_codigo")
        self.btn_enviar_codigo.setGeometry(QRect(10, 320, 351, 41))
        self.btn_enviar_codigo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_codigo.setStyleSheet(u"QPushButton{\n"
"	color : #fffffffff;\n"
"	background-color : #154583;\n"
"	border : none;\n"
"	font-size: 20px;\n"
"	font-style: montserrat;\n"
"}")
        self.efeito_senac_hub = QLabel(self.centralwidget)
        self.efeito_senac_hub.setObjectName(u"efeito_senac_hub")
        self.efeito_senac_hub.setGeometry(QRect(130, -20, 331, 271))
        self.efeito_senac_hub.setPixmap(QPixmap(u":/imagens/imagens/Group_37hubacademyefeito-removebg-preview.png"))
        self.efeito_senac_hub.setScaledContents(True)
        self.img_lateral_direito = QLabel(self.centralwidget)
        self.img_lateral_direito.setObjectName(u"img_lateral_direito")
        self.img_lateral_direito.setGeometry(QRect(900, 0, 61, 611))
        self.img_lateral_direito.setPixmap(QPixmap(u":/imagens/imagens/Group 10desenhoesquerdo_login.jpg"))
        self.img_lateral_direito.setScaledContents(True)
        self.img_lateral_esquerdo = QLabel(self.centralwidget)
        self.img_lateral_esquerdo.setObjectName(u"img_lateral_esquerdo")
        self.img_lateral_esquerdo.setGeometry(QRect(0, -10, 61, 611))
        self.img_lateral_esquerdo.setPixmap(QPixmap(u":/imagens/imagens/barra_lateral_esquerda.png"))
        self.img_lateral_esquerdo.setScaledContents(True)
        self.img_efeito = QLabel(self.centralwidget)
        self.img_efeito.setObjectName(u"img_efeito")
        self.img_efeito.setGeometry(QRect(640, 380, 47, 111))
        self.img_efeito.setPixmap(QPixmap(u":/imagens/imagens/Frame_1efeitoatrasdaarealogar-removebg-preview.png"))
        self.img_efeito.setScaledContents(True)
        Enviar_Codigo.setCentralWidget(self.centralwidget)
        self.img_imagem_medico.raise_()
        self.efeito_senac_hub.raise_()
        self.framecodigo_para_confirmar.raise_()
        self.img_lateral_direito.raise_()
        self.img_lateral_esquerdo.raise_()
        self.img_efeito.raise_()

        self.retranslateUi(Enviar_Codigo)

        QMetaObject.connectSlotsByName(Enviar_Codigo)
    # setupUi

    def retranslateUi(self, Enviar_Codigo):
        Enviar_Codigo.setWindowTitle(QCoreApplication.translate("Enviar_Codigo", u"MainWindow", None))
        self.img_imagem_medico.setText("")
        self.label_codigo.setText("")
        self.label_estoque_medico.setText(QCoreApplication.translate("Enviar_Codigo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Estoque M\u00e9dico</span></p></body></html>", None))
        self.lineEdit_inserir_codigo.setPlaceholderText(QCoreApplication.translate("Enviar_Codigo", u"C\u00f3digo", None))
        self.btn_enviar_codigo.setText(QCoreApplication.translate("Enviar_Codigo", u"Enviar C\u00f3digo", None))
        self.efeito_senac_hub.setText("")
        self.img_lateral_direito.setText("")
        self.img_lateral_esquerdo.setText("")
        self.img_efeito.setText("")
    # retranslateUi

