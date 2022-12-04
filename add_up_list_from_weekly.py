from function import *

for page in range(1, 194):
    response = get_response(f'https://api.bilibili.com/x/web-interface/popular/series/one?number={page}')
    response_json = json.loads(response.text)
    for info in response_json['data']['list']:
        add_mid_to_db(info['owner']['mid'],
                      info['owner']['name'],
                      f"week - {response_json['data']['config']['number']} - {info['aid']}")
    random_time_sleep(1, 2)
