__author__ = 'Willie'
#encoding=utf-8
import urllib
import re
url = "http://*.*.*.*/log/"
def GetUrl(url):
    html = urllib.urlopen(url).read()
    rule =('/log/\d{4,}-+\d{2,}-+\d{2,}-+log\.txt')
    pullurl =re.findall(rule,html)
    return pullurl


def DownLoad(point_url):
    a = 1
    for i in point_url:
        final_url="http://*.*.*.*"+i
        name =final_url[25:-4]
        print name
        print final_url
        urllib.urlretrieve(final_url,"%s.txt"%name)
        number = len(point_url)
        count = 100 * a / number
        print "%d %%"%count
        a += 1


if __name__=="__main__":
    point_url=GetUrl(url)
    DownLoad(point_url)