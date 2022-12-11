from function import *

num = 1

while True:

    for page in range(1, 26):
        response = get_response(f'http://api.bilibili.com/x/web-interface/popular?ps=20&pn={page}')
        response_json = json.loads(response.text)
        for info in response_json['data']['list']:
            add_mid_to_db(info['owner']['mid'],
                          info['owner']['name'],
                          f"hot - {info['aid']}")
        random_time_sleep(1, 1)
    print(f"第{num}轮爬取完成，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    count_time = 0
    num += 1
