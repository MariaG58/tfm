# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwin_visualizador.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1183, 989)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.AbrirDICOM = QPushButton(self.centralwidget)
        self.AbrirDICOM.setObjectName(u"AbrirDICOM")

        self.horizontalLayout_2.addWidget(self.AbrirDICOM)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_2.addWidget(self.comboBox_4)

        self.zoomInButton = QPushButton(self.centralwidget)
        self.zoomInButton.setObjectName(u"zoomInButton")

        self.horizontalLayout_2.addWidget(self.zoomInButton)

        self.zoomOutButton = QPushButton(self.centralwidget)
        self.zoomOutButton.setObjectName(u"zoomOutButton")

        self.horizontalLayout_2.addWidget(self.zoomOutButton)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prevDICOMButton = QPushButton(self.centralwidget)
        self.prevDICOMButton.setObjectName(u"prevDICOMButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevDICOMButton.sizePolicy().hasHeightForWidth())
        self.prevDICOMButton.setSizePolicy(sizePolicy)
        self.prevDICOMButton.setMinimumSize(QSize(60, 60))
        self.prevDICOMButton.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_3.addWidget(self.prevDICOMButton)

        self.imageSelector = QTabWidget(self.centralwidget)
        self.imageSelector.setObjectName(u"imageSelector")
        self.L_CC = QWidget()
        self.L_CC.setObjectName(u"L_CC")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.L_CC.sizePolicy().hasHeightForWidth())
        self.L_CC.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.L_CC)
        self.gridLayout.setObjectName(u"gridLayout")
        self.left_cc_scroll_image = QScrollArea(self.L_CC)
        self.left_cc_scroll_image.setObjectName(u"left_cc_scroll_image")
        self.left_cc_scroll_image.setWidgetResizable(True)
        self.left_cc_scroll_image.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1007, 811))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.left_cc_scroll_image.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.left_cc_scroll_image, 0, 0, 1, 1)

        self.imageSelector.addTab(self.L_CC, "")
        self.R_CC = QWidget()
        self.R_CC.setObjectName(u"R_CC")
        sizePolicy1.setHeightForWidth(self.R_CC.sizePolicy().hasHeightForWidth())
        self.R_CC.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.R_CC)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.right_cc_scroll_image = QScrollArea(self.R_CC)
        self.right_cc_scroll_image.setObjectName(u"right_cc_scroll_image")
        self.right_cc_scroll_image.setWidgetResizable(True)
        self.right_cc_scroll_image.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1007, 811))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy1)
        self.right_cc_scroll_image.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.right_cc_scroll_image, 0, 0, 1, 1)

        self.imageSelector.addTab(self.R_CC, "")
        self.L_ML = QWidget()
        self.L_ML.setObjectName(u"L_ML")
        self.gridLayout_3 = QGridLayout(self.L_ML)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.left_ml_scroll_image = QScrollArea(self.L_ML)
        self.left_ml_scroll_image.setObjectName(u"left_ml_scroll_image")
        self.left_ml_scroll_image.setWidgetResizable(True)
        self.left_ml_scroll_image.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1007, 811))
        self.left_ml_scroll_image.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.left_ml_scroll_image, 0, 0, 1, 1)

        self.imageSelector.addTab(self.L_ML, "")
        self.R_ML = QWidget()
        self.R_ML.setObjectName(u"R_ML")
        self.gridLayout_4 = QGridLayout(self.R_ML)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.right_ml_scroll_image = QScrollArea(self.R_ML)
        self.right_ml_scroll_image.setObjectName(u"right_ml_scroll_image")
        self.right_ml_scroll_image.setWidgetResizable(True)
        self.right_ml_scroll_image.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1007, 811))
        self.right_ml_scroll_image.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_4.addWidget(self.right_ml_scroll_image, 0, 0, 1, 1)

        self.imageSelector.addTab(self.R_ML, "")

        self.horizontalLayout_3.addWidget(self.imageSelector)

        self.nextDICOMButton = QPushButton(self.centralwidget)
        self.nextDICOMButton.setObjectName(u"nextDICOMButton")
        sizePolicy.setHeightForWidth(self.nextDICOMButton.sizePolicy().hasHeightForWidth())
        self.nextDICOMButton.setSizePolicy(sizePolicy)
        self.nextDICOMButton.setMinimumSize(QSize(60, 60))
        self.nextDICOMButton.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_3.addWidget(self.nextDICOMButton)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.PatientName = QLabel(self.centralwidget)
        self.PatientName.setObjectName(u"PatientName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PatientName.sizePolicy().hasHeightForWidth())
        self.PatientName.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PatientName.setFont(font)
        self.PatientName.setFrameShape(QFrame.NoFrame)
        self.PatientName.setFrameShadow(QFrame.Sunken)
        self.PatientName.setTextFormat(Qt.PlainText)
        self.PatientName.setScaledContents(False)
        self.PatientName.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.PatientName, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1183, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(0)
        self.imageSelector.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Robolab Dicom Visualizer", None))
        self.AbrirDICOM.setText(QCoreApplication.translate("MainWindow", u"Abrir DICOM", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Nodulo", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Distorsion_arq", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Densidad_asim_foc", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Microcalcificaciones", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Calc_tip_benig", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Nodulo", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1 ", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Rectangulo", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Circulo", None))

        self.zoomInButton.setText(QCoreApplication.translate("MainWindow", u"Zoom +", None))
        self.zoomOutButton.setText(QCoreApplication.translate("MainWindow", u"Zoom -", None))
        self.prevDICOMButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.imageSelector.setTabText(self.imageSelector.indexOf(self.L_CC), QCoreApplication.translate("MainWindow", u"Izquierda-CC", None))
        self.imageSelector.setTabText(self.imageSelector.indexOf(self.R_CC), QCoreApplication.translate("MainWindow", u"Derecha-CC", None))
        self.imageSelector.setTabText(self.imageSelector.indexOf(self.L_ML), QCoreApplication.translate("MainWindow", u"Izquierda-ML", None))
        self.imageSelector.setTabText(self.imageSelector.indexOf(self.R_ML), QCoreApplication.translate("MainWindow", u"Derecha-ML", None))
        self.nextDICOMButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.PatientName.setText(QCoreApplication.translate("MainWindow", u"Patient Identifier", None))
    # retranslateUi

