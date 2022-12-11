import re

from bs4 import BeautifulSoup

from function import *

cv_list = []

while True:
    response_index = get_response(
        'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&host_mid=300021061&timezone_offset=-480',
        is_proxy=False)
    response_json = json.loads(response_index.text)
    for cv in response_json['data']['items']:
        cv_list.append(cv['basic']['rid_str'])

    response = get_response(f'https://www.bilibili.com/read/cv{cv_list[0]}', is_proxy=False)
    response_bs4 = BeautifulSoup(response.text, 'lxml')

    for i in range(5, 12):
        a = response_bs4.select(f'#read-article-holder > p:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 7):
        a = response_bs4.select(f'#read-article-holder > ul:nth-child(15) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 7):
        a = response_bs4.select(f'#read-article-holder > ul:nth-child(17) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 61):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(30) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 61):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(35) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 61):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(40) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 21):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(43) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 21):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(46) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 21):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(50) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 21):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(53) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 21):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(56) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 11):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(60) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    for i in range(1, 11):
        a = response_bs4.select(f'#read-article-holder > ol:nth-child(64) > li:nth-child({i}) > a')[0]
        mid = re.sub('[^0-9]', '', a.get('href'))
        add_mid_to_db(int(mid), a.text, 'LePtC')

    cv_list = []
    time.sleep(60)
