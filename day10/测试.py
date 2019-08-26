import requests



res= requests.get(url="http://www.nxrc.com.cn/resume/resume_list/page/50.htm")
print(res.text)