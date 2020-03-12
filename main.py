import time
from spiders.spider import GetUserInfo


if __name__ == '__main__':
    start_time = time.time()
    # 指定uid范围
    user = GetUserInfo(38166622, 38166723)
    user.run()
    print(f'花费时间：{time.time() - start_time:.2f}s')
