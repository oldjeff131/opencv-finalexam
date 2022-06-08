import cv2 as cv
import numpy as np

kernel=np.ones((3,3),np.uint8)
class pictureFilter():
    def graycolor(self,changeing):
        return cv.cvtColor(changeing, cv.COLOR_BGR2GRAY)
    
    def threshold(self,changeing,value):
        return cv.threshold(changeing,value, 255, cv.THRESH_BINARY)

    def averaging(self,changeing):
        return cv.blur(changeing, (5, 5))
        
    def Dilation(self,changeing):
        global kernel
        return cv.dilate(changeing,kernel,iterations = 1)

    def Erosion(self,changeing):
        global kernel
        return cv.erode(changeing,kernel,iterations = 1)
    
    def Gaussia(self,changeing):
        return cv.GaussianBlur(changeing,(11,11),-1)
    
    def Bilateral(self,changeing):
        img_Gaussia=cv.GaussianBlur(changeing,(5,5),9)
        return cv.bilateralFilter(img_Gaussia,10,10,10)
    
    def medianBlur(self,changeing):
        return cv.medianBlur(changeing, 5)
