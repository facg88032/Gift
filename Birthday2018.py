import time
import pygame
import tkinter as tk
window=tk.Tk()
window.title()
window.geometry('200x100')

l=tk.Label(window,text=' Dear Birthday',bg='green',font=('Arial',12),width=15,height=2)
l.pack()
def hit_me():
    b=tk.Botton(window,text='A',width=15,height=2 ,command =hit_me)
window.mainloop()
# red=(255,0,0)
# green=(0,255,0)
# white=(255,255,255)
# pygame.init()
# display_width=800
# display_height=600
#
# gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('Birthday')
#
#
#
#
# gameDisplay.fill(white)
# pygame.draw.rect(gameDisplay, green,(150,450,100,50))
# pygame.draw.rect(gameDisplay, red,(550,450,100,50))
