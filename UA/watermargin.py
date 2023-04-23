import fake_useragent
import requests
from bs4 import BeautifulSoup
import lxml

if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/sanguo.html'
    head = {
        'User-Agent': fake_useragent.UserAgent().random
    }
    response = requests.get(url, headers=head)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    titles = soup.select('.book_mulu')
    print(titles)

    # for title in titles:
    #     print(title.text)

    #
    # for title in titles:
    #     # print(title.text)
    #     title_text = title.text
    #     content_url = "http://www.ixpsge.com"+title['href']
    #     content_resp = requests.get(content_url, headers=head)
    #     content_resp.encoding = 'utf-8'
    #     content_soup = BeautifulSoup(content_resp.text,'lxml')
    #     content_text = content_soup.find('div',id='chaptercontent').text
    #     with open('./水浒.txt','a',encoding='utf-8') as fp:
    #         fp.write(title_text+'\n')
    #         fp.write(content_text+'\n')
