from wsgiref import headers
import json
import fake_useragent
import requests
if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    head = {
        'User-Agent': fake_useragent.UserAgent().random
    }

    k_value = input('Please enter')
    data = {
        'kw': k_value
    }
    # 发送请求
    response = requests.post(url, data=data, headers = head)
    fileName = k_value + '.json'
    with open(fileName, 'w',encoding='utf8') as f:
        f.write(json.dumps(response.json(), ensure_ascii= False))