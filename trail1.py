import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

path=r"pics\pics2"

img_list = os.listdir(path)
len = len(img_list)




def simple_edge_detection(image):
    edges_detected = cv2.Canny(image, 100, 100)
    images = [image, edges_detected]
    return images

location = [121, 122]
def process(images, location):
    for loc, edge_image in zip(location, images):
        plt.subplot(loc)
        plt.imshow(edge_image, cmap='gray')

for img in img_list:
    image = cv2.imread("pics\pics2\{}".format(img), 0)

    images = simple_edge_detection(image)

    process(images, location)

    len-=1
    cv2.imwrite('res\edge_plot{}.png'.format(len), images[1])

print("Processed....")

#('edge_detected.png', )
