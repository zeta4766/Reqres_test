import time


def measure_execution_time(func):
    start_time = time.perf_counter()
    func()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time
