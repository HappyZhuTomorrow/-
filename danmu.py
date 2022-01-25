import requests
import json

from requests.api import head
import time
class danmu():
    def __init__(self):
        self.cookie = {
            "cookie": "innersign=0; buvid3=18B91EC6-BA60-554B-C700-E8649FECC6B296120infoc; b_lsid=A824D348_17E2A8B8D82; bsource=search_google; _uuid=9AF296C7-ED65-F254-492A-5EEA481CD84895882infoc; buvid_fp=BB51ABD4-7CBD-4151-7FED-0B523B753AF978576infoc; fingerprint=9dcf5fef392c35e38333d3f7a3f48633; buvid_fp_plain=BB51ABD4-7CBD-4151-7FED-0B523B753AF978576infoc; SESSDATA=fc9eb699%2C1656943321%2C3d873%2A11; bili_jct=5f5b40546510965ff50057ecc3720f67; DedeUserID=380058213; DedeUserID__ckMd5=606a83eea588e3b0; sid=i95ze512; i-wanna-go-back=-1; b_ut=5; _dfcaptcha=76e3f065594e8ac91f73c44514692fb8; PVID=1; LIVE_BUVID=AUTO6316413913576960"
        }
        self.head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }
        self.url = 'https://api.live.bilibili.com/msg/send'
    
    def send(self,room_id,content):
        # data = {
        #     "bubble": "0",
        #     "msg": "test123456",
        #     "color": "16777215",
        #     "mode": "1",
        #     "fontsize": "25",
        #     "rnd": "1641391353",
        #     "roomid": "23866710",
        #     "csrf": "5f5b40546510965ff50057ecc3720f67",
        #     "csrf_token": "5f5b40546510965ff50057ecc3720f67"
        # }
        data = {
            
            "msg": content,
            "color": "16777215",
            "fontsize": "25",
           "rnd": "1641391353",
            "roomid": room_id,
            "csrf": "5f5b40546510965ff50057ecc3720f67",
            "csrf_token": "5f5b40546510965ff50057ecc3720f67"
            
        }
        r = requests.post(self.url,cookies=self.cookie,data=data,headers=self.head)
        # r_json = json.loads(r.text)
        # print(json.dumps(r_json,sort_keys=True,indent=4,ensure_ascii=False))
    def get_roomid(self,uid):
        url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(uid)
        
        r = requests.get(url,headers=self.head)
        r_json = json.loads(r.text)
        room_id = r_json['data']['live_room']['roomid']
        # print(json.dumps(r_json,sort_keys=True,indent=4,ensure_ascii=False))
        return room_id
        # print(room_id)
    

    ##获取指定小说，开始独轮车
    def get_novel(self,bookid):
        pass
if __name__ == '__main__':
    # danmu().send(23866710)
    # print(int(32/20))
    room_id = danmu().get_roomid(2036047839)
    while True:
        danmu().send(room_id,'主播没退役，只是没人要')
        time.sleep(6)
    # lines = open('./D.txt',encoding='utf-8').readlines()
    # while True:
    #     for line in lines:
    #         strlen = len(line)
    #         for i in range(int(strlen/20)+1):
    #             # print((i+1)*20-1)
    #             start = (i)*20
    #             end = (i+1)*20-1
    #             # print(start)
    #             # print(end)
    #             # print(line[start:end])
    #             danmu().send(room_id,line[(i)*20:(i+1)*20-1].strip('\n'))
    #             time.sleep(6)