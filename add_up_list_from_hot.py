from function import *

while True:

    for page in range(1, 26):
        response = get_response(f'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={page}')
        response_json = json.loads(response.text)
        for info in response_json['data']['list']:
            add_mid_to_db(info['owner']['mid'],
                          info['owner']['name'],
                          f"hot - {info['aid']}")
        random_time_sleep(2, 3)
    time.sleep(28800)
