# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 312)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn.setGeometry(QtCore.QRect(110, 110, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushBtn.setFont(font)
        self.pushBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon.fromTheme("head")
        self.pushBtn.setIcon(icon)
        self.pushBtn.setObjectName("pushBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.textEdit2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(130, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit2.setFont(font)
        self.textEdit2.setObjectName("textEdit2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(20, 180, 311, 51))
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.textEdit1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(130, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit1.setFont(font)
        self.textEdit1.setObjectName("textEdit1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 18))
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
        self.pushBtn.setText(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow", "UserName"))
        self.label2.setText(_translate("MainWindow", "Password"))
