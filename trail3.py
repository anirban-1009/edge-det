#trail3.py

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

path=r"pics\pics2"

img_list = os.listdir(path)
count = len(img_list)
len = len(img_list)

def process(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad


for img in img_list:
    str=path+"\\"+img
    img = cv2.imread(str, cv2.IMREAD_COLOR)
    res = process(img)
    count-=1
    cv2.imwrite('res\\res{}.png'.format(count),res)

print("Processed.....")