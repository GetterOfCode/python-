import os

import fake_useragent
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'http://pic.netbian.com/e/search/result/?searchid=2670'
    headers = {
        'User-Agent':fake_useragent.UserAgent().random
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'

    tree = etree.HTML(response.text)
    li_list = tree.xpath('//div[@class ="slist"]/ul[@class = "clearfix"]/li')
    if not os.path.exists('./picLib'):
        os.mkdir('./picLib')
    for li in li_list:
        jpg_name = ''.join(li.xpath('./a/b/text()'))

        jpg_url = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        jpd_res = requests.get(jpg_url,headers=headers)
        jpd_res.encoding = 'gbk'
        with open('./picLib/'+jpg_name+'.jpg','wb') as fp:
            fp.write(jpd_res.content)

