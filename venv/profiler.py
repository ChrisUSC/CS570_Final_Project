import platform
import gc
from sys import argv
import timeit

PLATFORM_OS = platform.system()

if PLATFORM_OS == 'Windows':
    import psutil
else:
    import resource


def get_memory_usage():
    if PLATFORM_OS == 'Windows':
        return psutil.Process().memory_full_info().peak_wset / 1024
    elif PLATFORM_OS == 'Linux':
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    else:
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024


def run_with_profiler(func, *args, **kwargs):
    response = {}

    def wrapper():
        start_mem = get_memory_usage()
        response['output'] = func(*args, **kwargs)
        end_mem = get_memory_usage()
        response['memory'] = end_mem - start_mem

    timer = timeit.Timer(stmt=wrapper, setup=lambda: gc.collect())
    response['time'] = timer.timeit(number=1)
    return response


if __name__ == '__main__':
    import sys

    def test_func(rows, cols):
        arr = [([0] * cols) for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                arr[i][j] = i * j
        return rows * cols

    size = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    response = run_with_profiler(test_func, size, size)
    print(response)
