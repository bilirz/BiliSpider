import re

from bs4 import BeautifulSoup

from function import *

while True:
    response_bs4 = BeautifulSoup(get_response('https://zeroroku.com/bilibili/rank/fans/desc', is_proxy=False).text, 'lxml')
    for i in range(2, 102):
        try:
            a = response_bs4.select(f'#__next > div.container.m-a.max-w-5xl.text-sm.p-2 > div > div.r-panel.p-2.overflow-x-scroll.md\:overflow-clip.bg-background-2.border-border-1.r-panel-border > div:nth-child({i}) > div.flex-1 > a')[0]
            mid = re.sub('[^0-9]', '', a.get('href'))
            add_mid_to_db(int(mid), a.text, 'Jannchie')
        except IndexError:
            print(f'没有第{i-1}个')
    random_time_sleep(1, 1)

    response_bs4 = BeautifulSoup(get_response('https://zeroroku.com/bilibili/rank/rate1/desc', is_proxy=False).text, 'lxml')
    for i in range(2, 102):
        try:
            a = response_bs4.select(f'#__next > div.container.m-a.max-w-5xl.text-sm.p-2 > div > div.r-panel.p-2.overflow-x-scroll.md\:overflow-clip.bg-background-2.border-border-1.r-panel-border > div:nth-child({i}) > div.flex-1 > a')[0]
            mid = re.sub('[^0-9]', '', a.get('href'))
            add_mid_to_db(int(mid), a.text, 'Jannchie')
        except IndexError:
            print(f'没有第{i-1}个')
    random_time_sleep(1, 1)

    response_bs4 = BeautifulSoup(get_response('https://zeroroku.com/bilibili/rank/rate1/asc', is_proxy=False).text, 'lxml')
    for i in range(2, 102):
        try:
            a = response_bs4.select(f'#__next > div.container.m-a.max-w-5xl.text-sm.p-2 > div > div.r-panel.p-2.overflow-x-scroll.md\:overflow-clip.bg-background-2.border-border-1.r-panel-border > div:nth-child({i}) > div.flex-1 > a')[0]
            mid = re.sub('[^0-9]', '', a.get('href'))
            add_mid_to_db(int(mid), a.text, 'Jannchie')
        except IndexError:
            print(f'没有第{i-1}个')
    random_time_sleep(1, 1)

    response_bs4 = BeautifulSoup(get_response('https://zeroroku.com/bilibili/rank/rate7/desc', is_proxy=False).text, 'lxml')
    for i in range(2, 102):
        try:
            a = response_bs4.select(f'#__next > div.container.m-a.max-w-5xl.text-sm.p-2 > div > div.r-panel.p-2.overflow-x-scroll.md\:overflow-clip.bg-background-2.border-border-1.r-panel-border > div:nth-child({i}) > div.flex-1 > a')[0]
            mid = re.sub('[^0-9]', '', a.get('href'))
            add_mid_to_db(int(mid), a.text, 'Jannchie')
        except IndexError:
            print(f'没有第{i-1}个')
    random_time_sleep(1, 1)

    response_bs4 = BeautifulSoup(get_response('https://zeroroku.com/bilibili/rank/rate7/asc', is_proxy=False).text, 'lxml')
    for i in range(2, 102):
        try:
            a = response_bs4.select(f'#__next > div.container.m-a.max-w-5xl.text-sm.p-2 > div > div.r-panel.p-2.overflow-x-scroll.md\:overflow-clip.bg-background-2.border-border-1.r-panel-border > div:nth-child({i}) > div.flex-1 > a')[0]
            mid = re.sub('[^0-9]', '', a.get('href'))
            add_mid_to_db(int(mid), a.text, 'Jannchie')
        except IndexError:
            print(f'没有第{i-1}个')
    random_time_sleep(1, 1)

    response_json = json.loads(get_response('https://api.zeroroku.com/bilibili/live/rank?m=60', is_proxy=False).text)
    for i in response_json:
        add_mid_to_db(int(i['mid']), i['name'], 'Jannchie')
    random_time_sleep(1, 1)

    response_json = json.loads(get_response('https://api.zeroroku.com/bilibili/live/rank?m=1440', is_proxy=False).text)
    for i in response_json:
        add_mid_to_db(int(i['mid']), i['name'], 'Jannchie')
    random_time_sleep(1, 1)

    response_json = json.loads(get_response('https://api.zeroroku.com/bilibili/live/rank?m=4320', is_proxy=False).text)
    for i in response_json:
        add_mid_to_db(int(i['mid']), i['name'], 'Jannchie')
    time.sleep(60)