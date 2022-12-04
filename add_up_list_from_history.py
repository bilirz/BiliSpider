from function import *

response = get_response('https://api.bilibili.com/x/web-interface/popular/precious?page_size=100&page=1')
response_json = json.loads(response.text)
for info in response_json['data']['list']:
    add_mid_to_db(info['owner']['mid'],
                  info['owner']['name'],
                  f"history - {info['aid']}")
