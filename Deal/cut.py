# -*- coding: utf-8 -*-
__author__ = 'Willie'
ciku=open(r'sorce.txt','r')
xieci=open(r'quchong.txt','w')
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