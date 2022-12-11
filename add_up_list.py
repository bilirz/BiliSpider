from function import *

mids = []

for mid in mids:
    response = get_response(f'http://api.bilibili.com/x/space/acc/info?mid={mid}')
    response_json = json.loads(response.text)
    add_mid_to_db(response_json['data']['mid'], response_json['data']['name'], 'add')
    random_time_sleep(1, 1)