from function import *

num = 1

while True:
    rids = [0, 168, 1, 3, 129, 4, 36, 188, 234, 223, 160, 211, 217, 119, 155, 5, 1]
    types = ['origin', 'rookie']
    for rid in rids:
        response = get_response(f'https://api.bilibili.com/x/web-interface/ranking/v2?rid={rid}&type=all')
        response_json = json.loads(response.text)
        for info in response_json['data']['list']:
            add_mid_to_db(info['owner']['mid'],
                          info['owner']['name'],
                          f"{rid} - {info['aid']}")
        random_time_sleep(2, 3)

    for typ in types:
        response = get_response(f'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type={typ}')
        response_json = json.loads(response.text)
        for info in response_json['data']['list']:
            add_mid_to_db(info['owner']['mid'],
                          info['owner']['name'],
                          f"{rid} - {info['aid']}")
        random_time_sleep(2, 3)
    print(f"第{num}轮爬取完成，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    count_time = 0
    num += 1
