import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed, FIRST_EXCEPTION


class MyException(Exception):
    def __init__(self, *args):
        self.args = args

def run(i):
    global total
    if i != 5 and i != 6:
        print("doing work {} start at ".format(i) + time.strftime("%H:%M:%S %Y", time.localtime()))
        time.sleep(i)
        print("work {} done at ".format(i) + time.strftime("%H:%M:%S %Y", time.localtime()))
        total += 1
        return total
    else:
        raise MyException('ip error')

total = 0
starttime = time.perf_counter()

all_task = [1,2,3,4,5,6,7,8,9,10,11,12]
with ThreadPoolExecutor(10) as executor:
    undo_task = [executor.submit(run,i) for i in all_task]
    completed, uncompleted = wait(undo_task, return_when=FIRST_EXCEPTION)
    for item in completed:
        print(item)
    print('undo:')
    for item in uncompleted:
        print(item)
        item.cancel()

elapsed = (time.perf_counter() - starttime)
print("done!time: {} ".format(elapsed))

