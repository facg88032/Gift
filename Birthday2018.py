import time
import tkinter as tk
import cv2
import pygame


window=tk.Tk()
window.title()
window.geometry('500x400')
window.configure(bg='SteelBlue1')
pygame.mixer.init()


#read image
img1=cv2.imread('image/Family.jpg')
img2=cv2.imread('image/87.jpg')
img3=cv2.imread('image/20180831.jpg')
img4=cv2.imread('image/2018722.jpg')
img5=cv2.imread('image/holdhands.jpg')
img6=cv2.imread('image/pratice.jpg')






l=tk.Label(window, text='text',bg='sky blue',fg='white',font=('Arial',12),width=20,height=3)#LABEL text
l.pack()


def chooseA():
    MusicA = pygame.mixer.music.load("Music/Family.mp3")#import Music
    pygame.mixer.music.play()#play Music
    list = ["blablabla", "blablabla", "blablabla",""]
    for i in list:
        time.sleep(2)
        print(i)#show in list text
    cv2.imshow('FAMILY', img1)#show image
def chooseB():
    MusicB = pygame.mixer.music.load("Music/87.mp3")
    pygame.mixer.music.play()
    list = ["blablabla!!", "blablabla", "blablabla", "blablabla",""]
    for i in list:
        time.sleep(2)
        print(i)
    cv2.imshow('487',img2)
def chooseC():
    MusicC = pygame.mixer.music.load("Music/sweet.mp3")
    pygame.mixer.music.play()
    list=["blablabla","blablabla",""]
    for i in list:
        time.sleep(2)
        print(i)
    cv2.imshow('Sweet',img3)
def chooseD():
    MusicD = pygame.mixer.music.load("Music/ToAnyWhere.mp3")
    pygame.mixer.music.play()
    list = ["blablabla", "blablabla","blablabla",
            "blablabla"," "]
    for i in list:
        time.sleep(2)
        print(i)
    cv2.imshow('ToAnyWhere',img4)
def chooseE():
    MusicF = pygame.mixer.music.load("Music/HoldHandDear.mp3")
    pygame.mixer.music.play()
    list = ["blablabla", "blablabla", "blablabla",
            "blablabla","blablabla",""]
    for i in list:
        time.sleep(2)
        print(i)
    cv2.imshow('HoldHandDear',img5)

def chooseF():
    MusicF = pygame.mixer.music.load("Music/pratice.mp3")
    pygame.mixer.music.play()
    list = ["blablabla", "blablabla",
            "blablabla", "blablabla",""]
    for i in list:
        time.sleep(2)
        print(i)
    cv2.imshow('Missyou',img6)
def chooseG():
    MusicA = pygame.mixer.music.load("Music/Finally.mp3") 
    pygame.mixer.music.play()
    list1 = ['blablablablablabla','blablabla','blablabla','blablabla'
             ]
   

    for i in list1:
        time.sleep(3)
        print(i)

    

b1 = tk.Button(window,
    text='Family',bg='orange red',
    width=15, height=2,
    command=chooseA)#BUTTON commd is set what you want to do when you click it
b1.place(x = 100,y = 100,anchor=tk.CENTER)
b2= tk.Button(window,
    text='HaHA',bg='dark orange',
    width=15, height=2,
    command=chooseB)
b2.place(x = 250,y = 100,anchor=tk.CENTER)
b3 = tk.Button(window,
    text='Sweet',bg='gold',
    width=15, height=2,
    command=chooseC)
b3.place(x = 400,y = 100,anchor=tk.CENTER)
b4 = tk.Button(window,
    text='AnyWhere',bg='green yellow',
    width=15, height=2,
    command=chooseD)
b4.place(x = 100,y = 200,anchor=tk.CENTER)
b5 = tk.Button(window,bg='RoyalBlue1',
    text='Portect',
    width=15, height=2,
    command=chooseE)
b5.place(x = 250,y = 200,anchor=tk.CENTER)
b6 = tk.Button(window,bg='purple2',
    text='Miss',
    width=15, height=2,
    command=chooseF)
b6.place(x = 400,y = 200,anchor=tk.CENTER)
b7 = tk.Button(window,bg='white',
    text='Finally!!',
    width=15, height=2,
    command=chooseG)
b7.place(x = 250,y = 300,anchor=tk.CENTER)

window.mainloop()#window forever loop to show it

