import time

import os

from multiprocessing import Process, current_process


def squared(number):
    """it squares a number"""

    return number*number


number_list = range(1, 1000)

processes = []



start_time = time.time()
for i in number_list:
    process = Process(target=squared, args=(i,))
    processes.append(process)
    process.start()
elapsed_time = time.time() - start_time

print(elapsed_time)




