import urllib
import urllib.request

def sendpost(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74"
        
        }
    for i in range(0,10):
        date = bytes(urllib.parse.urlencode({"username":str(i*10),"password":str(i*20)}),encoding = "utf-8")
        request = urllib.request.Request(url,data=date,headers = head)
        response = urllib.request.urlopen(request)
        print(response.read())

if __name__ == "__main__":
    sendpost("http://httpbin.org/post")
