import time
import pygame
import tkinter as tk
import cv2
window=tk.Tk()
window.title()
window.geometry('300x400')
img1=cv2.imread('image/Family.jpg')
img2=cv2.imread('image/87.jpg')
img3=cv2.imread('image/20180831.jpg')
img4=cv2.imread('image/2018722.jpg')
img5=cv2.imread('image/holdhands.jpg')
img6=cv2.imread('image/pratice.jpg')


l=tk.Label(window, text='DEAR! Happy Birthday',bg='sky blue',fg='white',font=('Arial',12),width=15,height=2)
l.pack()


def chooseA():
    cv2.imshow('image1',img1)
def chooseB():
    cv2.imshow('image2',img2)
def chooseC():
    cv2.imshow('image3',img3)
def chooseD():
    cv2.imshow('image4',img4)
def chooseE():
    cv2.imshow('image5',img5)
def chooseF():
    cv2.imshow('image6',img6)
def chooseG():
    list1 = ['say to you'
             ]
    list2 = ['say to you']

    for i in list1:
        time.sleep(3)
        print(i)

    for j in list2:
        time.sleep(0.5)
        print(j)


b1 = tk.Button(window,
    text='chooseA',
    width=15, height=2,
    command=chooseA)
b1.pack()
b2= tk.Button(window,
    text='chooseB',
    width=15, height=2,
    command=chooseB)
b2.pack()
b3 = tk.Button(window,
    text='chooseC',
    width=15, height=2,
    command=chooseC)
b3.pack()
b4 = tk.Button(window,
    text='chooseD',
    width=15, height=2,
    command=chooseD)
b4.pack()
b5 = tk.Button(window,
    text='chooseE',
    width=15, height=2,
    command=chooseE)
b5.pack()
b6 = tk.Button(window,
    text='chooseF',
    width=15, height=2,
    command=chooseF)
b6.pack()
b7 = tk.Button(window,
    text='chooseG',
    width=15, height=2,
    command=chooseG)
b7.pack()

window.mainloop()

