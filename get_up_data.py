from function import *

num = 1
while True:
    count_time = time.strftime('%Y-%m-%d %H:%M:%S')
    for up in dbf.find():
        try:
            response_stat = json.loads(get_response(f"http://api.bilibili.com/x/relation/stat?vmid={up['mid']}").text)
            doct = {
                'follower': response_stat['data']['follower'],
                'count_time': count_time,
                'time': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            dbf.update_one({'mid': up['mid']}, {'$push': {'data': doct}})
            print(f"爬取了{up['mid']}，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
            random_time_sleep(1, 1)
        except:
            mongo['bilibili']['UP02_error'].update_one({'mid': up['mid'], 'time': count_time})
    print(f"第{num}轮爬取完成，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    count_time = 0
    num += 1
