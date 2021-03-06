import os ,UI,filter,sys
import pytesseract
import cv2 as cv
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pytesseract import Output
from PIL import Image

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.ui=UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ft=filter.pictureFilter()
        self.setup_control()
    
    def setup_control(self):
        self.ui.loadingpicture.clicked.connect(self.open_file)
        self.ui.pictureTFtextButton.clicked.connect(self.pictureTftext)
        self.ui.pushButton.clicked.connect(self.savetext)

    def open_file(self): #載入的圖片
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
        if filename is '':
            return
        self.img = cv.imread(filename, -1)
        self.img_path=filename
        if self.img.size == 1:
            return
        self.showImage()

    def showImage(self): #顯示載入的圖片
        height, width, Channel = self.img.shape
        bytesPerline = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qImg)
        self.qpixmap_height = self.qpixmap.height()
        self.ui.labelpicture.setPixmap(QPixmap.fromImage(self.qImg))

    def pictureTftext(self):
        pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
        changeimg=self.img
        if self.ui.graycheckBox.isChecked():
            changeimg = changeimg=self.ft.graycolor(changeimg)
        if self.ui.thresholdcheckBox.isChecked():
            value=int(self.ui.thresholdlineEdit.text())
            if value=='' or value>255 or value<1:
                QMessageBox.information(None, '錯誤', '數值輸入錯誤')
            else:
                ret, changeimg =self.ft.threshold(changeimg,value)
        if self.ui.ErosioncheckBox.isChecked():
            changeimg=self.ft.Erosion(changeimg)
        if self.ui.DilationcheckBox.isChecked():
            changeimg=self.ft.Dilation(changeimg)
        if self.ui.averagingcheckBox.isChecked():#平均濾波器
            changeimg= self.ft.averaging(changeimg)
        if self.ui.GaussiacheckBox.isChecked():#高斯濾波
            changeimg=self.ft.Gaussia(changeimg)
        if self.ui.BilateralcheckBox.isChecked():
             changeimg=self.ft.Bilateral(changeimg)
        if self.ui.medianBlurcheckBox.isChecked():#中值濾波
            changeimg = self.ft.medianBlur(changeimg)
        cv.imshow("end", changeimg)
        text = pytesseract.image_to_string(changeimg, lang='chi_tra')#繁體:chi_tra 英文:eng
        self.ui.picturetext.setPlainText(text)
        print(text)

    def savetext(self):
        S__File =QFileDialog.getSaveFileName(None,'SaveTextFile','/', "Text Files (*.txt)")
        Text = self.ui.picturetext.toPlainText()
        if S__File[0]:
            with open(S__File[0], 'w') as file:
                file.write(Text)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())
	