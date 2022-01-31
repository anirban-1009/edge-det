#tkinter1.py
from tkinter import *  
import cv2

m, n = 100, 200

def change_m(a):
    global m
    m = a

def change_n(a):
    global n
    n = a
def simple_edge_detection(image):
    edges_detected = cv2.Canny(image, m, n)
    images = [image, edges_detected]
    return images

def change(simple_edge_detection):
    image=cv2.imread('pic.png')
    image=cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_CUBIC)
    images = simple_edge_detection(image)
    cv2.imwrite("pic.png",images[1])
    height, width= image.shape[:2]
    return height,width

height, width = change(simple_edge_detection)  
root = Tk() 
canvas = Canvas(root, width = width, height = height)      
canvas.pack()      
img = PhotoImage(file="pic.png") 
w = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=change_m)
w.pack()
change(simple_edge_detection)
w1 = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=change_n)
w1.pack()
change(simple_edge_detection)
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()