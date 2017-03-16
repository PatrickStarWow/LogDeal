# -*- coding: utf-8 -*-
__author__ = 'Willie'
import os
import re

dir = os.listdir("./")
b = len(dir)
for a in range(0,b-1,1):
    word = dir[a]
    txt = open(word,"r")
    # intex = txt.read()
    show = open("../sorce_error.txt","a")
    for line in txt.readlines():
        intex = unicode(line,encoding="utf-8")

        rule = u"[\u4e00-\u9fa5]{2,2}\:\d{6,6} ip:\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
        output = re.findall(rule,intex)
        print output
        if output != []:
            i = output[0] + "\n"
            show.write(i.encode("utf-8"))
            print(i)
            output = []

    show.close()
    txt.close()