import json
import random
import time

import pymongo
import requests

mongo = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
dbf = mongo['bilibili']['UP02']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
}


def random_proxies():
    response = json.loads(requests.get('http://127.0.0.1:5000/proxies/http').text)

    return random.choice(response['proxies'])


def add_mid_to_db(mid: int, name: str, reason: str):
    doct = {'mid': int(mid),
            'name': str(name),
            'reason': str(reason),
            'first_time': time.strftime('%Y-%m-%d %H:%M:%S'),
            'data': [{
                'follower': 0,
                'count_time': time.strftime('%Y-%m-%d %H:%M:%S'),
                'time': time.strftime('%Y-%m-%d %H:%M:%S')
            }]
            }
    if dbf.find_one({'mid': mid}) is None:
        # print(doct)
        dbf.insert_one(doct)
        print(f"爬取了{mid}列表，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print_reason = dbf.find_one({'mid': mid})['reason']
        print(f"重复了{mid}，来自于{print_reason}，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")


def get_response(url: str, is_proxy=True):
    response = ''
    if is_proxy is True:
        response = requests.get(url, headers=headers, proxies={'https': random_proxies()})
    elif is_proxy is False:
        response = requests.get(url, headers=headers)
    return response


def random_time_sleep(num1: int = 1, num2: int = 2):
    time.sleep(random.randint(num1, num2))
