import requests

import hashlib

m=hashlib.md5()
m.update("你好".encode())
print(m.hexdigest())




# def a():
#     # url="http://api.xfsub.com/index.php?url=https://v.youku.com/v_show/id_XNDI4ODc3ODcxMg==.html"
#     url="https://valipl-vip.cp31.ott.cibntv.net/67756D6080932713CFC02204E/03000600005D3B0F287783105CF07D3E6854B1-02A9-44A2-9560-3C385A3E7373-00050.ts?ccode=0502&duration=7253&expire=18000&psid=e0aae851ed7a3bd1103d4e77f5973144&ups_client_netip=72ec8a7c&ups_ts=1565871133&ups_userid=&utid=ual7FRyQogYCAQHK%2BxpHmucN&vid=XNDI4ODc3ODcxMg%3D%3D&sm=1&operate_type=1&bc=2&vkey=A3c163203ce54fba38059fdbaefb3e5e9&x_pcdn_cons=1565957538-63314-0-2e444c47fb1c5728255a06a382dc8b6e"
#     cookies={
#         ""
#     }
#     res=requests.get(url).text
#
#     print(res)
#
#
#
# if __name__ == '__main__':
#     a()