import requests
from lxml import etree
import time

#获取
class GetDetails:
    def __init__(self,url,head):
        self.url = url
        self.head = head
        self.xpath="//div[@class='post-content']/p/img/@src"
    def getdetails(self):

        res=requests.get(self.url,headers=self.head).text
        # time.sleep(2)
        result = etree.HTML(res)
        href = result.xpath(self.xpath)
        for i in href:
            SaveText(i).save()

#写入

class SaveText:
    def __init__(self,href):
        self.href=href

    def save(self):
        href =requests.get(self.href).content
        name = self.href[-14:]
        print(name)
        with open("haha/%s"%name,"ab+") as w:
            w.write(href)

if __name__ == '__main__':
    head={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
        "Referer": "http://duanziwang.com/category/%E6%90%9E%E7%AC%91%E5%9B%BE/"
    }



    url="http://duanziwang.com/category/%E6%90%9E%E7%AC%91%E5%9B%BE/{}/"
    a=[GetDetails(url=url.format(i),head=head).getdetails() for i in range(3,10)]
    print("全部爬完")
    # page=2
    # url="http://duanziwang.com/category/%E6%90%9E%E7%AC%91%E5%9B%BE/"+str(page)+"/"
    # while True:
    #     GetDetails(url,head).getdetails()
    #     page+=1
