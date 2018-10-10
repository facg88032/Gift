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
    list1 = ['Dear 地瓜', '咪個眼半年過去了', '時間過的好像很快又不快 為何這麼說呢'
        , '每當以為我們是老夫老妻時 都會想起我們才六個月呢',
             '而每當想起跨年時才像昨天 怎麼已經過了半年'
        , '我很幸運 打從心裡這麼覺得能遇到妳這麼好地瓜哈哈',
             '很謝謝你總是等我 為我著想',
             '你總是說我想娛樂本來就是正常 當然我是真的想玩ㄎㄎ',
             '但每次玩都還有些愧疚感 辛苦你等了半天還要慣我玩個電動'
        , '所以玩個幾場就跑去找你這隻小地瓜討摸摸聊聊',
             '還是比較喜歡在你摸摸聊聊下偷玩XD ',
             '誰叫我是小壞蛋想要貪心同時兼得 :P',
             ' ',
             '看了你的報告覺得有些是對你抱歉啊 辛苦你了',
             '要你懂事、獨立、有同理心這事該怎說呢',
             '其實我討厭的不是他們幼稚',
             '我討厭的是把無理取鬧看得認真然後再來生氣跟你吵架',
             '很多事情用腦子想根本不可能做到',
             '如果開開玩笑胡鬧一下 那當然是嘴砲一下囉',
             '但是認真起來那就不好笑 只是在牽制對方',
             '第一任 很多不可能約束 像是不能跟女生聊天等等奇行',
             '第二任 對於別人給的太過理所當然 根本不在乎別人感受也不珍惜',
             '每當你提起需要幫忙我能做到的一定使命必達 因為你是我的公主<3',
             '而請你吃飯 幫你出錢 只是想幫你分擔一些壓力跟讚賞你一下哈哈',
             '我知道你跟第二任不一樣 所以不要有任何不安 因為你值得', '還有阿',
             '妞妞我很喜歡牠 把牠當作你不在時陪伴我的靈魂',
             '所以就當作是有多一個很愛牠的人',
             '我還恨不得把牠一直放在這裡呢',
             '所以不要有壓力有愧疚 好嗎? ',
             '啾啾',
             ' ',
             '我成了你的支柱 你也成了我的動力來源',
             '因為有你在讓我想努力把你娶回家顆顆 一起有個好的未來',
             '我知道我很多事情不細心 讓你有些失望 Sorry跟你說聲抱歉TAT',
             '但真的不是故意的 只能麻煩你提點一下我這個不細心得腦袋',
             '你的心思很細膩，連要告訴我不好的點都為我著想 ',
             '而我總是催促著你趕快說 一定很想打爆我齁哈哈哈',
             '話說還沒打字時 好想有很多話想表達 怎一打字就開始迷糊了XD',
             '所以要結尾了 挖哈哈哈哈哈 想到再補?',
             '最後希望能一起努力，建立我們想要的樣子',
             '完成我們夢想的樣子(這句你打得借用XD)'
             ]
    list2 = ['阿對了', '.', '.', '.', '.', '.', '.', '.', '.', '.', '就是', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '大富翁贏了真爽哈哈哈哈哈哈 啾啾啾啾啾啾啾最愛地瓜了<3', 'By 男神']

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

