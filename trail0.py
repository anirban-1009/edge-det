#trail0.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pics\pics2\WhatsApp Image 2022-01-31 at 10.19.27 AM.jpeg', 0)

def simple_edge_detection(image):
    edges_detected = cv2.Canny(image, 100, 200)
    images = [image, edges_detected]
    return images

images = simple_edge_detection(img)

location = [121, 122]
for loc, edge_image in zip(location, images):
    plt.subplot(loc)
    plt.imshow(edge_image, cmap='gray')

cv2.imwrite('edge_detected.png', images[1])
plt.imsave()
plt.show()