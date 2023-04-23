import requests


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    response = requests.get(url,headers = headers)
    response.encoding = 'utf8'
    page_text = response.text
    fp = open('./baidu.html','w',encoding='utf8')
    fp.write(page_text)
    fp.close()