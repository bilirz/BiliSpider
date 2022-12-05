from function import *

num = 1
while True:
    count_time = time.strftime('%Y-%m-%d %H:%M:%S')
    for up in dbf.find():
        response_stat = json.loads(get_response(f"https://api.bilibili.com/x/relation/stat?vmid={up['mid']}").text)
        # response_upstat = json.loads(get_response(f"https://api.bilibili.com/x/space/upstat?mid={up['mid']}").text)   # cookie
        doct = {
                # 'following': response_stat['data']['following'],
                'follower': response_stat['data']['follower'],
                # 'archive': response_upstat['data']['archive']['view'],    # cookie
                # 'article': response_upstat['data']['article']['view'],
                # 'likes': response_upstat['data']['likes'],
                'count_time': count_time,
                'time': time.strftime('%Y-%m-%d %H:%M:%S')
                }
        dbf.update_one({'mid': up['mid']}, {'$push': {'data': doct}})
        print(f"爬取了{up['mid']}，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
        random_time_sleep(1, 2)
    print(f"第{num}轮爬取完成，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    count_time = 0
    num += 1
