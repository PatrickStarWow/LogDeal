# -*- coding: utf-8 -*-
__author__ = 'Willie'
import os
import re

dir = os.listdir("./")
b = len(dir)
for a in range(1,b,1):
    word = dir[a]
    txt = open(word,"r")
    intex = txt.read()
    txt.close()
    intex = unicode(intex,encoding="utf-8")

    rule = u"[\u4e00-\u9fa5]{2,2}\:\d{6,6} ip:\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
    output = re.findall(rule,intex)

    show = open("../sorce.txt","a")
    for i in output:
        i = i + "\n"
        show.write(i.encode("utf-8"))
        print(i)
        output = []
    show.close()