from wsgiref import headers

import fake_useragent
import lxml
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    fp = open('test.html', 'r',encoding ='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup.p)
    # print(soup.html)
    # print(soup.head)
    # print(soup.title)
    # print(soup.a)
    # print(soup.find('a',title = 'qin').text)
    # print(soup.select('a'))
    # print(soup.select('.tang>ul>li'))
    # print(soup.select('.song>p'))
    print(soup.select('.tang>ul li'))
    fp.close()