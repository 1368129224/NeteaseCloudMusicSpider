import random
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed

def run(i,j):
    global total
    print("start work at " + time.strftime("%H:%M:%S %Y", time.localtime()))
    time.sleep(i)
    print("work done at " + time.strftime("%H:%M:%S %Y", time.localtime()))
    total += 1
    return total

total = 0
starttime = time.perf_counter()

times = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
with ThreadPoolExecutor() as executor:
    a = 123
    all_task = [executor.submit(run,i,a) for i in times]
    for task in as_completed(all_task):
        print(task.result())

wait(all_task, return_when=ALL_COMPLETED)

# for i in times:
#     run(i)

elapsed = (time.perf_counter() - starttime)
print("done!time: {} ".format(elapsed))

