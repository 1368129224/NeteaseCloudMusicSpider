import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed, FIRST_EXCEPTION


class MyException(Exception):
    def __init__(self, *args):
        self.args = args

def run(i,j):
    global total
    print("doing work {} start at ".format(i) + time.strftime("%H:%M:%S %Y", time.localtime()))
    time.sleep(i)
    print("{} work {} done at ".format(j, i) + time.strftime("%H:%M:%S %Y", time.localtime()))
    total += 1
    return total

def generateJ(i):
    for j in range(len(i)):
        yield 123

total = 0
starttime = time.perf_counter()

all_task = [1,2,3,4,5,6,7,8,9,10,11,12]
j = [123 for i in range(len(all_task))]
with ThreadPoolExecutor(10) as executor:
    executor.map(run,all_task,j)

elapsed = (time.perf_counter() - starttime)
print("done!time: {} ".format(elapsed))

