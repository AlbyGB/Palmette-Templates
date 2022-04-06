'''
Docs for OpenCV module: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
First make sure to run 'pip install -r requirements.txt'
'''
import cv2 as cv
import numpy as np

image = cv.imread('PalmetteLogo.png')
GrayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
LaplacianImage = cv.Laplacian(image, cv.CV_64F)
SobelxImage = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=5)
SobelyImage = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=5)
CannyImage = cv.Canny(image, 100, 200)
BlurImage = cv.GaussianBlur(image, (5,5), 0)

cv.imshow('Image', image)
cv.waitKey(0)
cv.imshow('Canny image', CannyImage)
cv.waitKey(0)