__author__ = 'Willie'
# -*- coding: utf-8 -*-
import os

dir = os.listdir("./")
b = len(dir)
for a in range(1,b,1):
    word = dir[0]
    ciku=open(r'word','r')
    xieci=open(r'quchong_log.txt','a')
    cikus=ciku.readlines()
    ciku.close()
    list2 = {}.fromkeys(cikus).keys()
    i=1
    for line in list2:
        if line[0]!=',':
            print  u"写入第："+`i`+u" 个"
            i+=1
            xieci.writelines(line)
    xieci.close()