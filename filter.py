import cv2 as cv
import numpy as np

kernel=np.ones((3,3),np.uint8)
class pictureFilter():
    def graycolor(self,changeimg):
        return cv.cvtColor(changeimg, cv.COLOR_BGR2GRAY)
    
    def threshold(self,changeimg,value):
        return cv.threshold(changeimg,value, 255, cv.THRESH_BINARY)

    def averaging(self,changeimg):
        return cv.blur(changeimg, (5, 5))
        
    def Dilation(self,changeimg):
        global kernel
        return cv.dilate(changeimg,kernel,iterations = 2)

    def Erosion(self,changeimg):
        global kernel
        return cv.erode(changeimg,kernel,iterations = 1)
    
    def Gaussia(self,changeimg):
        return cv.GaussianBlur(changeimg,(11,11),-1)
    
    def Bilateral(self,changeimg):
        img_Gaussia=cv.GaussianBlur(changeimg,(5,5),9)
        return cv.bilateralFilter(img_Gaussia,10,10,10)
    
    def medianBlur(self,changeimg):
        return cv.medianBlur(changeimg, 7)
