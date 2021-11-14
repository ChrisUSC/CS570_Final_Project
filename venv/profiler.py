import gc
import timeit
import psutil

# NOTE: This is not platform-independent, currently uses Windows-specific APIs.


def run_and_profile(func, *args, **kwargs):
    response = {}

    def wrapped_func():
        gc.collect()
        start_mem = psutil.Process().memory_full_info()
        response['output'] = func(*args, **kwargs)
        end_mem = psutil.Process().memory_full_info()
        response['memory'] = end_mem.peak_wset - start_mem.peak_wset

    response['time'] = timeit.timeit(wrapped_func, number=1)
    return response
