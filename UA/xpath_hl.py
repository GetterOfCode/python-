import fake_useragent
import requests
from lxml import etree
if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/hongloumeng.html'
    headers = {
        'User-Agent': fake_useragent.UserAgent().random

    }
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    tree = etree.HTML(response.text)
    li_list = tree.xpath("//div[@class='book-mulu']/ul/li")
    fp = open('./hongloumeng.txt','a',encoding='utf-8')
    count = 1
    for li in li_list:
        title_content = li.xpath("./a/text()")[0]
        content_url = 'http://www.shicimingju.com' + li.xpath("./a/@href")[0]
        content_res = requests.get(content_url,headers = headers)
        content_res.encoding = "utf-8"
        content_tree = etree.HTML(content_res.text)
        content = content_tree.xpath(".//div[@class='chapter_content']/text()")[0]
        fp.write(title_content+'\n'+content)
        count += 1
        if count >= 10:
            break
    fp.close()

