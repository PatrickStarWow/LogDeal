__author__ = 'Willie'
#encoding=utf-8
import urllib
import re
url = "http://*.*.*.*/log/"
def GetUrl(url):
    html = urllib.urlopen(url).read()
    #<a href="/log/2015-05-21-ErrorLog.txt">2015-05-21-ErrorLog.txt</a>
    # rule =r'<a href="(/log/\d{4,}-+\d{2,}-+\d{2,}-+ErrorLog\.txt)">'
    '''
    rule =re.compile('/log/\d{4,}-+\d{2,}-+\d{2,}-+ErrorLog\.txt')
    pullurl =rule.findall(html)
    '''
    rule =('/log/\d{4,}-+\d{2,}-+\d{2,}-+ErrorLog\.txt')
    pullurl =re.findall(rule,html)
    return pullurl


def DownLoad(point_url):
    a = 1
    for i in point_url:
        final_url="http://*.*.*.*"+i
        name =final_url[25:-4]
        print final_url
        urllib.urlretrieve(final_url,"%s.txt"%name)
        number = len(point_url)
        count = 100 * a / number
        print "%d %%"%count
        a += 1


if __name__=="__main__":
    point_url=GetUrl(url)
    DownLoad(point_url)