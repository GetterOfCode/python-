import json

import fake_useragent
import requests

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': fake_useragent.UserAgent().random,
        'Cookie': 'douban-fav-remind=1; gr_user_id=9738d0fb-b9e8-4608-b7c4-06ae08f0a4e0; ll="118188"; bid=EiKteog7f-Y; __gads=ID=39c76aeba2a1a3c8-22128ce1ead600d7:T=1665279989:RT=1665279989:S=ALNI_Malcn5X3jprb4GdWWiN7CAZkLhVCA; _vwo_uuid_v2=DE3B2A81A65E9DF12D333B78381F5207C|a58c8302b8b2a17f974fa63a9f2a2d23; __yadk_uid=7X08AEZE5pdT2ZmIX1IjWn9F8ABySPGV; __utma=30149280.1444039246.1570351298.1665279989.1677568115.19; __utmc=30149280; __utmz=30149280.1677568115.19.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="268201056:PzPkoVORPfE"; ck=tPDd; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26820; __gpi=UID=00000a245149651c:T=1665279989:RT=1677568315:S=ALNI_MYtmW4clSP7e0lb9IksV7gZFhhCDQ; __utmb=30149280.10.10.1677568115; __utma=223695111.720515776.1570351298.1665279989.1677568331.6; __utmb=223695111.0.10.1677568331; __utmc=223695111; __utmz=223695111.1677568331.6.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=["","",1677568331,"https://www.douban.com/"]; _pk_ses.100001.4cf6=*; ct=y; frodotk_db="393f8a30730c52e9abbe9e915924f8bb"; _pk_id.100001.4cf6=f5684e90e104408b.1570351297.6.1677568746.1665280007.'

    }
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start':'0',
        'limit':'1'
    }
    response = requests.get(url, params = params, headers = headers)
    # print(response.text)
    fp = open('./douban.json','w',encoding='utf8')
    fp.write(json.dumps(response.json(),ensure_ascii=False))
    fp.close()