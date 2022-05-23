import datetime
import tracemalloc


def get_time(func, hay, needle):
    start = datetime.now()
    func(hay, needle)
    return float(str(datetime.now() - start).split(':')[2])


def get_memory(func, hay, needle):
    last = tracemalloc.get_tracemalloc_memory()
    tracemalloc.start()
    func(hay, needle)
    return tracemalloc.get_tracemalloc_memory() - last


def test(func, hay, needle, isTime):
    runner = get_memory
    if isTime:
        runner = get_time
    return runner(func, hay, needle)
