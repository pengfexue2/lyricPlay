import re
import time
import printPlay
import pygame
import codecs
openLyric = codecs.open("无条件.lrc",encoding='utf-8')
lyricList = openLyric.readlines()
timeTable = []
lyricDict = {}
timeDict = {}

pattern = r'\d{2}:\d{2}.\d{2}'
for str in lyricList:
    strList = str.split(']')
    for i in range(len(strList)-1):
        if re.match(pattern,strList[i][1:]):
            t = (int(strList[i][1:][:2]) * 60 + int(strList[i][1:][3:5]))+ int(strList[i][1:][6:8])*0.01
            timeTable.append(t)
            lyricDict[t] = strList[-1][:-1]
#print(lyricDict)
#print(timeTable)

pygame.mixer.init()
track = pygame.mixer.music.load('无条件.mp3')
pygame.mixer.music.play()

print("~~~ 开始播放 无条件-陈奕迅 ~~~")
temp = 0
for t in timeTable:
    time.sleep(t-temp)
    temp = t
    text = ''.join(lyricDict[t].split(' '))
    #printPlay.printPlay(text,'★','　')
    printPlay.printPlay(text, '0', ' ')


