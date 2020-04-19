
def count_time(func, data_collection, times = 1000000):
    import time
    start_time = time.time()
    for i in range(times):
        for data in func:
            func(data)
    return time.time() - start_time


