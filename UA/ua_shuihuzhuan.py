import fake_useragent
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': fake_useragent.UserAgent().random

    }
    res= requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sg.txt','a',encoding='utf-8')
    for li in li_list:
        title_content = li.text
        content_url = 'http://www.shicimingju.com' + li.a['href']
        content_res = requests.get(content_url, headers=headers)
        content_res.encoding = 'utf-8'
        content_soup = BeautifulSoup(content_res.text,'lxml')
        content = content_soup.find('div',class_ = 'chapter_content').text
        fp.write(title_content+'\n'+ content+'\n')
        break
    fp.close()
