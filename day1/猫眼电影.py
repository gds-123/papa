from lxml import etree

import requests

class GetList:
    def __init__(self,url,num):
        self.url= url
        self.num= num

    # 获取列表
    def getlist(self):
        print("这是第%d页"%self.num)
        res = requests.get(self.url).text
        ele = etree.HTML(res)
        url_list= ele.xpath("//dl[@class='board-wrapper']/dd/a/@href")
        for i in url_list:
            url = "https://maoyan.com"+str(i)
            GetDetails().getdetails(url)
class GetDetails:
    def __init__(self):
        self.movie_name = "//h3[@class='name']/text()"
        self.movie_class = "//li[@class='ellipsis']/text()"
        self.movie_intro = "//span[@class='dra']/text()"
    #获取详情
    def getdetails(self,url):
        res = requests.get(url).text
        ele = etree.HTML(res)
        movie_name=ele.xpath(self.movie_name)[0]
        movie_classify=ele.xpath(self.movie_class)[0]
        m=ele.xpath(self.movie_class)[1]
        movie_addres=m.split()[0]
        movie_time=m.split()[2]
        movie_showtime=ele.xpath(self.movie_class)[2]
        movie_intro=ele.xpath(self.movie_intro)[0]
        print(movie_name,movie_classify,movie_addres,movie_time,movie_showtime,movie_intro)






if __name__ == '__main__':
    url = "https://maoyan.com/board/4?offset={}"
    # url = "https://maoyan.com/board/4?offset=10"
    # GetList(url).getlist()
    url=[GetList(url.format(i),i/10).getlist()for i in range(0,110,10)]
