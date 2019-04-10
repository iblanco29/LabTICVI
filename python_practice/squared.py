import time


def squared(number):
    """it squares a number"""

    return number*number


number_list = range(1, 1000)

start_time = time.time()
for i in number_list:
    squared(i)
elapsed_time = time.time() - start_time

print(elapsed_time)




