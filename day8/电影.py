import requests

def getmovie():
    num = 1000000
    while 1:
        print(1111111111111)
        url = "https://wuji.zhulong-zuida.com/20190710/1588_60982288/800k/hls/cb04e7e4b1b" + str(num)[1:] + ".ts"
        res= requests.get(url=url).content
        with open("1.MP4","ab+")as r:
            r.write(res)
            print("已加入%s条"%str(num)[-1])
        num += 1



if __name__ == '__main__':
    getmovie()