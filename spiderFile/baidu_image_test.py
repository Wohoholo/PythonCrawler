import requests
import re

url = 'http://image.baidu.com/search/index'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://image.baidu.com/search/index?ct=&z=&tn=baiduimage&ipn=r&word=%E5%A3%81%E7%BA%B8%20%E5%8D%A1%E9%80%9A%E5%8A%A8%E6%BC%AB%20%E6%B5%B7%E8%B4%BC%E7%8E%8B&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=&lm=-1&st=-1&fr=&fmq=1526269427171_R&ic=0&se=&sme=&width=1920&height=1080&face=0'
}

def get_html(url, headers):
    data = {
        'cl': '2',
        'ct': '201326592',
        'face': '0',
        'fp': 'result',
        'gsm': '200001e',
        'ic': '0',
        'ie': 'utf-8',
        'ipn': 'rj',
        'istype': '2',
        'lm': '-1',
        'nc': '1',
        'oe': 'utf-8',
        'pn': '30',
        'queryword': '海贼王',
        'rn': '30',
        'st': '-1',
        'tn': 'resultjson_com',
        'word': '壁纸 卡通动漫 海贼王'
    }

    page = requests.get(url, data, headers=headers).text
    return page


def get_img(page, headers):

    reg = re.compile('http://.*?\.jpg')
    imglist1 = re.findall(reg, page)
    imglist2 = imglist1[0: len(imglist1): 3]

    x = 0
    for imgurl in imglist2:

        bin = requests.get(imgurl, headers=headers).content

        with open('img/%s.jpg' % x, 'wb') as f:
            f.write(bin)
            x += 1

if __name__ == '__main__':
    page = get_html(url, headers)
    get_img(page, headers)