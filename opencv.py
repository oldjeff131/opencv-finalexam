from PIL import Image
import os
import pytesseract
import cv2 as cv
import UI

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.ui=UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self._connectActions()

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe' 
img = Image.open('43698.jpg') 
text = pytesseract.image_to_string(img, lang='chi_tra') 
print(text)
	