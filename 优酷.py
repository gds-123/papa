import sys
from urllib import parse
import requests,re,time
import you_get
from lxml import etree

cookies={
    "cookie":"__ysuid=15639316954065cX; cna=aEW4FY31wTcCAQHK+xqQI1B5; juid=01dho1go8719ts; ysestep=1; yseidcount=1; ystep=1; ctoken=shpLftxqXKLoD5q2kYvSGLm1; _uab_collina=156551144709385084164942; _m_h5_tk=9e0aca42778fe9f5ebe0d5b39fe00292_1565516715899; _m_h5_tk_enc=eab4c28d3856edb143621800f6f3e371; __aryft=1565511679; __ayft=1565511073109; __aysid=1565511073110F7T; __arpvid=1565512723421qYKfqY-1565512723449; __ayscnt=1; __aypstp=31; __ayspstp=31; P_ck_ctl=6DB93425760992F6B1AB6125E511C174; isg=BDQ0Y5R71SieNUHg4_mG3aeeEfJmpVCQKlez1M6Vzb9COdSD9hjyheLruzFE2pBP"
}
headers={
    "user-agent":"Spider",
    "upgrade-insecure-requests":"1",
    "referer":"https://movie.youku.com/?spm=a2ha1.12675304.m_6913_c_14318.d_3&scm=20140719.manual.6913.url_in_blank_http%3A%2F%2Fmovie.youku.com",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.8",

}


class GetList:
    def __init__(self,url):
        self.url=url
    def getList(self):
        res = requests.get(self.url,cookies=cookies,headers=headers).text
        ele = etree.HTML(res)
        result=ele.xpath("//script[last()-9]/text()")[0].replace("\\","")
        ele = etree.HTML(result)

        #所有电影节点
        url1=ele.xpath("//div[@class='sk-mod mod-zy'] |//div[@class='sk-mod']")
        self.userOperation(url1)
    #用户操作
    def userOperation(self,urllist):
        #每个电影
        num = 1
        url_list1=[]
        for i in urllist:
            name = i.xpath(".//a[@data-spm='dtitle']/@title")[0]
            url = i.xpath(".//a[@data-spm='dtitle']/@href")[0]
            if url.startswith("http"):
                print(num,".",name,url,i)
                url_list1.append(i)

                num += 1

        #客户选择
        while 1:
            inp = input("请输入要查看的序号：  \n下一页请输入*\n")
            try:
                if inp == "*":
                    return
                elif inp.isdigit() or int(inp) <= num-1:
                    pass
            except ValueError:
                print("请按规定输入")
                continue

            # try:
            url_list=[]
            url = url_list1[int(inp)-1].xpath(".//a[@data-spm='dselectbutton']/@href")
            uel_name = url_list1[int(inp)-1].xpath(".//a[@data-spm='dselectbutton']/@title")

            if url == []:

                url = url_list1[int(inp)-1].xpath(".//a[@data-spm='dtitle']/@href")
                uel_name = url_list1[int(inp) - 1].xpath(".//a[@data-spm='dtitle']/@title")
            for i in url:

                if i.startswith("http") and i not in url_list:
                    # print(i)
                    url_list.append(i)
            # #第一段视频页数
            # page = url_list1[int(inp)-1].xpath(".//div[@class='mod-tab-wrap num-tab-wrap']//div//div[3]/ul/li[1]/a/text()")[0].split("-")[1].strip()
            # #总页数
            # user_page = url_list1[int(inp)-1].xpath(".//div[@class='mod-tab-wrap num-tab-wrap']//div//div[3]/ul/li[2]/a/text()")[0].split("-")[1].strip()
            # #第一段视频
            # selections = url_list1[int(inp)-1].xpath(".//ul[@class='mod-play-list play-list-num  tab-panel tab-1']/li[position()<"+str(int(page)+2)+"]/a/@href")
            # #第二段视频
            # selections2 = url_list1[int(inp)-1].xpath(".//ul[@class='mod-play-list play-list-num  tab-panel tab-2']/li/a/@href")
            # #所有视频集数
            # url_list=selections+selections2
            if len(url_list)-1 <= 0:
                print("为您找到一集，正在跳转")
                user_num = 1
            else:
                user_num = input("请输入要选择的集数： 1 - %d \n"%(len(url_list)-1))
            self.getMovie(url_list[int(user_num)-1])
            # except:
            #     print("系统错误，正在跳回上一层")
            #     continue
                # url = url_list1[int(inp) - 1].xpath(".//a[@data-spm='dselectbutton']/@href")
                # selections = url_list1[int(inp)-1].xpath("./ul[@class='mod-play-list play-list-num  tab-panel tab-1']/li/a/text()")
                # # print(len(url_list1[int(inp)-1].xpath(".//a/@href")))
                # if selections ==[]:
                #     # print(2222222222222,inp)
                #     selections = urllist[int(inp)-1].xpath(".//a[@data-spm='dtitle']/@href")[0]
                #     # print(urllist[int(inp)-1])
                # print(url)

    def getMovie(self,url_list):
        print(1111111111111111111)
        sys.argv=["you_get","-o","./",url_list]
        you_get.main()
        print(url_list)






if __name__ == '__main__':
    while 1:
        name=input("请输入要电影名称")
        name = parse.quote(name)
        page = 1
        name = parse.unquote(name)
        while 1:
            url="https://so.youku.com/search_video/q_"+str(name)+"?spm=a2h0k.11417342.pageturning.dnextpage&_t=1565786081594&aaid=7c2a5c9f7c0117fc93c12fbbfe69a387&pg="+str(page)

            GetList(url).getList()
            print(page)
            page +=1
