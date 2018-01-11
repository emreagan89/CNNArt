# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'framework1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1340, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = Canvas(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(210, 10, 1101, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setObjectName("canvas")
        self.axial = QtWidgets.QPushButton(self.centralwidget)
        self.axial.setGeometry(QtCore.QRect(20, 100, 51, 31))
        self.axial.setObjectName("axial")
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(20, 20, 171, 21))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.setting_CNN = QtWidgets.QPushButton(self.centralwidget)
        self.setting_CNN.setGeometry(QtCore.QRect(20, 380, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.setting_CNN.setFont(font)
        self.setting_CNN.setObjectName("setting_CNN")
        self.deep_visualization = QtWidgets.QPushButton(self.centralwidget)
        self.deep_visualization.setGeometry(QtCore.QRect(20, 420, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deep_visualization.setFont(font)
        self.deep_visualization.setObjectName("deep_visualization")
        self.sagittal = QtWidgets.QPushButton(self.centralwidget)
        self.sagittal.setGeometry(QtCore.QRect(80, 100, 51, 31))
        self.sagittal.setObjectName("sagittal")
        self.coronal = QtWidgets.QPushButton(self.centralwidget)
        self.coronal.setGeometry(QtCore.QRect(140, 100, 51, 31))
        self.coronal.setObjectName("coronal")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 560, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.patching = QtWidgets.QPushButton(self.centralwidget)
        self.patching.setGeometry(QtCore.QRect(20, 340, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patching.setFont(font)
        self.patching.setObjectName("patching")
        self.arteselect = QtWidgets.QLabel(self.centralwidget)
        self.arteselect.setGeometry(QtCore.QRect(20, 150, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.arteselect.setFont(font)
        self.arteselect.setObjectName("arteselect")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 180, 181, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1340, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.axial.setText(_translate("MainWindow", "Axial"))
        self.setting_CNN.setText(_translate("MainWindow", "Set CNN"))
        self.deep_visualization.setText(_translate("MainWindow", "Deep Visualization"))
        self.sagittal.setText(_translate("MainWindow", "Sagittal"))
        self.coronal.setText(_translate("MainWindow", "Coronal"))
        self.label1.setText(_translate("MainWindow", "3D View"))
        self.pushButton.setText(_translate("MainWindow", "View Result"))
        self.patching.setText(_translate("MainWindow", "Data Preprocess"))
        self.arteselect.setText(_translate("MainWindow", "Artefects Selector"))

from canvas import Canvas
