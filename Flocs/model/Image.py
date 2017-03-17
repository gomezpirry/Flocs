#!/usr/bin/env python
'''
Created on 21/02/2017

@author: augusto
'''

import cv2

class Image:
    #def __init__(self):
        #self.image
    
    def loadImage(self, path):
        self.image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        
    def getBinaryImage(self):
        self.image = cv2.medianBlur(self.image, 5)
        self.thresholdImage = cv2.adaptiveThreshold(self.image ,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
     
    def showImage(self):   
        cv2.imshow('Image Threshold', self.image )
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        