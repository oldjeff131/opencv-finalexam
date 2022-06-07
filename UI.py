# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelpicture = QtWidgets.QLabel(self.centralwidget)
        self.labelpicture.setGeometry(QtCore.QRect(10, 10, 800, 600))
        self.labelpicture.setObjectName("labelpicture")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(830, 10, 291, 311))
        self.groupBox.setObjectName("groupBox")
        self.picturetext = QtWidgets.QTextEdit(self.groupBox)
        self.picturetext.setGeometry(QtCore.QRect(10, 10, 271, 291))
        self.picturetext.setObjectName("picturetext")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(830, 330, 291, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadingpicture = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadingpicture.setObjectName("loadingpicture")
        self.verticalLayout.addWidget(self.loadingpicture)
        self.ROIButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ROIButton.setObjectName("ROIButton")
        self.verticalLayout.addWidget(self.ROIButton)
        self.pictureTFtextButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pictureTFtextButton.setObjectName("pictureTFtextButton")
        self.verticalLayout.addWidget(self.pictureTFtextButton)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(830, 460, 291, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.smallButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.smallButton.setObjectName("smallButton")
        self.horizontalLayout.addWidget(self.smallButton)
        self.bigButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bigButton.setObjectName("bigButton")
        self.horizontalLayout.addWidget(self.bigButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 21))
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
        self.labelpicture.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "圖片資訊"))
        self.groupBox_2.setTitle(_translate("MainWindow", "工作按鈕"))
        self.loadingpicture.setText(_translate("MainWindow", "載入圖片"))
        self.ROIButton.setText(_translate("MainWindow", "擷取"))
        self.pictureTFtextButton.setText(_translate("MainWindow", "文字偵測"))
        self.groupBox_3.setTitle(_translate("MainWindow", "尺寸改變"))
        self.smallButton.setText(_translate("MainWindow", "zoom in"))
        self.bigButton.setText(_translate("MainWindow", "zoom out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

