import sys
from PIL import Image
import os
import pytesseract
import cv2 as cv
import numpy as np
import UI
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.ui=UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
    
    def setup_control(self):
        self.ui.loadingpicture.clicked.connect(self.open_file)
        self.ui.pictureTFtextButton.clicked.connect(self.pictureTftext)
        self.ui.pushButton.clicked.connect(self.picturetextbox)

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
            changeimg = cv.cvtColor(changeimg, cv.COLOR_BGR2GRAY)
        if self.ui.thresholdcheckBox.isChecked():
            value=int(self.ui.thresholdlineEdit.text())
            if value=='' or value>255 or value<1:
                QMessageBox.information(None, '錯誤', '數值輸入錯誤')
            else:
                ret, changeimg = cv.threshold(changeimg,value, 255, cv.THRESH_BINARY)
        kernel=np.ones((3,3),np.uint8)
        if self.ui.checkBox.isChecked():
            changeimg=cv.dilate(changeimg,kernel,iterations = 2)
        if self.ui.checkBox_2.isChecked():
            changeimg=cv.erode(changeimg,kernel,iterations = 1)
        if self.ui.checkBox_3.isChecked():
            kernel = np.array([[-2, -1, 0],[-1, 1, 1],[0, 1, 2]])
            changeimg = cv.filter2D(changeimg, -1, kernel)
        if self.ui.checkBox_4.isChecked():
            kernel = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])
            changeimg = cv.filter2D(changeimg, -1, kernel)
        cv.imshow("gray", changeimg)
        #ret,binary=cv.threshold(gray,250,255,cv.THRESH_BINARY)
        #cv.imshow("binary", binary)
        #end=cv.medianBlur(gray,5)
        text = pytesseract.image_to_string(changeimg, lang='chi_tra')
        self.ui.picturetext.setPlainText(text)
        print(text)

    def picturetextbox(self):
        img =self.img
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())
	