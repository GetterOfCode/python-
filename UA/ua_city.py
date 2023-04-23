import fake_useragent
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': fake_useragent.UserAgent().random

    }
    response = requests.get(url, headers=headers,verify=False)
    response.encoding = "utf-8"
    tree = etree.HTML(response.text)
    li_list = tree.xpath('//div[@class="hot"]/div[@class="bottom"]/ul/li | //div[@class="all"]/div[@class="bottom"]/ul/div[2]/li')
    cityName_list = []
    for li in li_list:
        cityName_list.append(li.xpath('./a/text()')[0])
    print(cityName_list)
