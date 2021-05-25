import urllib
import urllib.request
import re

n=1
head={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
}
request = urllib.request.Request("http://top.baidu.com/buzz?b=341&c=514",headers = head)
response = urllib.request.urlopen(request).read()
con = re.findall('<td class="keyword">[^>]*>([^<]*)<',response.decode("gb2312"))
for i in con:
        print("%d.%s"%(n,i),end="\n")
        n = n + 1