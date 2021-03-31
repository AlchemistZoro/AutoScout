import requests
from bs4 import BeautifulSoup
import json as json
def find_url(num):
    print('开始爬取页面数量')
    left = 0
    mid = 80000
    right = 160000  # 这三个数据定义的目的是
    p = mid
    for k in range(0, 50000):
        time.sleep(0.2)
        dis = right - left
        r = requests.get(
            'https://api.bilibili.com/x/web-interface/newlist?&rid={}&type=0&pn={}&ps=50&jsonp=jsonp'.format(num, p))
        r.encoding = r.apparent_encoding
        data = json.loads(r.text)
        # print(left, mid, right)
        if len(data['data']['archives']):  # 判断第P页是否有数据
            right = right
            left = mid
            p = int((right + mid) / 2)
            mid = p  
        else:
            left = left
            right = mid
            p = int((left + mid) / 2)
            mid = p
        if len(data['data']['archives']) and dis < 2:  # 第P页有数据且“头尾”只差1，结束判断，得到页码
            print('aid:{},页数:{},数量:{}'.format(num, p, p * 50))
            break
    print('页面数量爬取结束')
    print('--开始生成URL池--')
    Url_Pool = []
    for m in range(0, p):
        url = "https://api.bilibili.com/x/web-interface/newlist?&rid={}&type=0&pn={}&ps=50&jsonp=jsonp".format(
            num, m)
        Url_Pool.append(url)
    print('--URL池生成结束--')
    return Url_Pool

num=1
p=1
r = requests.get('https://api.bilibili.com/x/web-interface/newlist?&rid={}&type=0&pn={}&ps=50&jsonp=jsonp'.format(num, p))
r.encoding = r.apparent_encoding
data = json.loads(r.text)

for k in range(0, len(data['data']['archives'])):
    aid = data['data']['archives'][k]['aid']
    title = data['data']['archives'][k]['title'].replace('"', '').replace("'", '')
    title = eval(repr(title).replace('\\', ''))
    duration = data['data']['archives'][k]['duration']
    up_id = data['data']['archives'][k]['owner']['mid']
    up_name = data['data']['archives'][k]['owner']['name']
    pubdate = data['data']['archives'][k]['pubdate']
    coin = data['data']['archives'][k]['stat']['coin']
    dan = data['data']['archives'][k]['stat']['danmaku']
    star = data['data']['archives'][k]['stat']['favorite']
    his_rank = data['data']['archives'][k]['stat']['his_rank']
    like = data['data']['archives'][k]['stat']['like']
    reply = data['data']['archives'][k]['stat']['reply']
    share = data['data']['archives'][k]['stat']['share']
    view = data['data']['archives'][k]['stat']['view']
    category = data['data']['archives'][k]['tname']
    key_words = data['data']['archives'][k]['dynamic'].replace('"', '').replace("'", '')

# with open('data.json', 'w',encoding='utf-8') as f:
#     f.write(json.dumps(data,ensure_ascii=False))

print()
