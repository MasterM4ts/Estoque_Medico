# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_perfil.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import QRC_login_rc
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Editar perfil")
        Form.resize(403, 195)
        Form.setMinimumSize(QSize(403, 195))
        Form.setMaximumSize(QSize(403, 195))
        self.btn_foto_de_perfil_bola = QPushButton(Form)
        self.btn_foto_de_perfil_bola.setObjectName(u"btn_foto_de_perfil_bola")
        self.btn_foto_de_perfil_bola.setGeometry(QRect(20, 40, 101, 101))
        self.btn_foto_de_perfil_bola.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_foto_de_perfil_bola.setStyleSheet(u"\n"
"border-radius: 5px;")
        icon = QIcon()
        icon.addFile("imagens/perfil_bola.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_foto_de_perfil_bola.setIcon(icon)
        self.btn_foto_de_perfil_bola.setIconSize(QSize(124, 89))
        self.btn_foto_de_perfil_gato = QPushButton(Form)
        self.btn_foto_de_perfil_gato.setObjectName(u"btn_foto_de_perfil_gato")
        self.btn_foto_de_perfil_gato.setGeometry(QRect(150, 40, 101, 101))
        self.btn_foto_de_perfil_gato.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile("imagens/foto_pefil_gato.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_foto_de_perfil_gato.setIcon(icon1)
        self.btn_foto_de_perfil_gato.setIconSize(QSize(102, 119))
        self.btn_foto_de_perfil_cachorro = QPushButton(Form)
        self.btn_foto_de_perfil_cachorro.setObjectName(u"btn_foto_de_perfil_cachorro")
        self.btn_foto_de_perfil_cachorro.setGeometry(QRect(280, 40, 101, 101))
        self.btn_foto_de_perfil_cachorro.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile("imagens/cachorro_perfil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_foto_de_perfil_cachorro.setIcon(icon2)
        self.btn_foto_de_perfil_cachorro.setIconSize(QSize(103, 104))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Editar perfil", u"Editar perfil", None))
        self.btn_foto_de_perfil_bola.setText("")
        self.btn_foto_de_perfil_gato.setText("")
        self.btn_foto_de_perfil_cachorro.setText("")
    # retranslateUi
