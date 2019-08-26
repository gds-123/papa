# -*- coding: utf-8 -*-
import scrapy
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Referer": "https://www.amazon.cn/",
}

cookies={
    "Cookie": "x-wl-uid=1JMRYVRFcRDq/9GDaYBNbPr3Xno5ed5XkfcPFX7jUPr5VITWBlppWspZtLwu+EAD+v8bgeyiCtl8=; session-id=459-3120943-1920910; ubid-acbcn=462-5522877-4544429; lc-acbcn=zh_CN; i18n-prefs=CNY; session-token=6TsAx7Iq8WrcvFjvFeu1/f0j5pTcAtAnbTDU62O1b72ANoVWPXW6eLV/3Kz+R37t9A/zBHW6XsVr0yOStfY9uLjlVRn92A1S6fTEX1d64jzE4Ddnjyb0cnrj5puh7ihICpHxoshSHGOpMK15jdwSff7LPIKo6rMKFor+Wjxff8zpagaWZe2xFrqE/ddYQXYT; floatingBannerOnGateway=floatingBannerOnGateway; csm-hit=tb:s-8134BE1PB38682Y2AY6F|1566723864319&t:1566723866526&adb:adblk_no; session-id-time=2082787201l"
}



class YmxSpider(scrapy.Spider):
    name = 'ymx'
    # allowed_domains = ['x.com']
    # start_urls = ['http://x.com/']
    def start_requests(self):
        url ="https://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Delectronics&field-keywords=https://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Delectronics&field-keywords="
        yield scrapy.Request(url=url,headers=headers,cookies=cookies)


    def parse(self, response):
        url= response.xpath("//div[@class='sc-c-div']/a/@href").extract()
        for i in url:
            print(i)
            # yield scrapy.Request(url=i,headers=headers,cookies=cookies,callback=self.getUrlList)
    def getUrlList(self,response):
        print(response.text)
        pass