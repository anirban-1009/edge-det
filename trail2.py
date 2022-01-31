import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pics\pics2\WhatsApp Image 2022-01-31 at 10.19.17 AM.jpeg', cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)

grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

cv2.imshow('grad X',grad_x)
cv2.imshow('grad Y',grad_y)
cv2.imwrite('Sobel Demo - Simple Edge Detector.jpg',grad)
cv2.waitKey()