import urllib
import urllib.request
import re


def send(url):
    head={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"}
    request = urllib.request.Request(url,headers = head)
    response = urllib.request.urlopen(request).read()
    match(response)

def match(content):
    con = re.findall('<div class="title">[^>]*>[^>]*>\n([^<]*)<',content.decode("utf-8"))
    for i in con:
        try:
            match = re.match('[\s]{2,}(.*)[\s]{2,}',i)
            print(match.string,end="")
        except Exception as result:
            print("")

if __name__ == "__main__":
    for a in range(0,250,25):
        send("https://www.douban.com/doulist/240962/?start=%d&sort=seq&playable=0&sub_type="%a)