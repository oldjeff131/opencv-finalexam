from PIL import Image
import os
import pytesseract
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe' 
img = Image.open('43698.jpg') 
text = pytesseract.image_to_string(img, lang='chi_tra') 
print(text)
	