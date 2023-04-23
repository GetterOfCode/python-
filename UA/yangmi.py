from wsgiref import headers

import fake_useragent
import requests

if __name__ == '__main__':
    url = 'http://www.sogou.com/web'
    head = {
        'User-Agent': fake_useragent.UserAgent().random

    }
    p_values = input('Please enter:')
    params = {
        'query':p_values
    }
    response = requests.get(url, params=params,headers= head)
    fileName = p_values + '.html'
    with open(fileName, 'w',encoding='utf8') as f:
        f.write(response.text)