import tracemalloc
from datetime import datetime
import matplotlib.pyplot as plt
import string
import random as r
import algos

def get_fixed_text(needle_size, position):
    needle = 'a'.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(needle_size))
    hay = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(position)) + needle
    return (hay, needle)


def get_random_text(needle_size, position):
    needle = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(needle_size))
    hay = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(position))
    return (hay, needle)


x = []  # Needle length
standard = []
rabin = []
bauer = []
res_kmp = []


def get_time(func, hay, needle):
    start = datetime.now()
    func(hay, needle)
    return float(str(datetime.now() - start).split(':')[2])


def get_memory(func, hay, needle):
    last = tracemalloc.get_tracemalloc_memory()
    tracemalloc.start()
    func(hay, needle)
    return tracemalloc.get_tracemalloc_memory() - last


def benchmark(func, hay, needle, isTime):
    runner = get_memory
    if isTime:
        runner = get_time
    return runner(func, hay, needle)


if __name__ == '__main__':
    for i in range(7, 20):
        (hay, needle) = get_fixed_text(r.randint(2 ** (i - 7), 2 ** (i - 3)), 100000)
        isTime = False
        standard.append(benchmark(algos.standard_search, hay, needle, isTime))
        rabin.append(benchmark(algos.rabin_karp, hay, needle, isTime))
        bauer.append(benchmark(algos.bauer_moore, hay, needle, isTime))
        res_kmp.append(benchmark(algos.kmp, hay, needle, isTime))
        x.append(i)

ax1 = plt.figure(figsize=(12, 7)).add_subplot(111)

plt.plot(x, standard, 'b*', alpha=0.7, label="Standard", mew=2, ms=10)
plt.plot(x, rabin, 'g^', alpha=0.7, label="Rabin Karp", mew=2, ms=10)
plt.plot(x, bauer, 'rs', alpha=0.7, label="Bauer Moore", mew=2, ms=10)
plt.plot(x, res_kmp, 'cD', alpha=0.7, label="KMP", mew=2, ms=10)

plt.legend()
ax1.set_title(u'Time By Needle Length')
plt.xlabel(u'Needle length [2^n]', fontsize=12)
plt.ylabel(u'Time [ms]', fontsize=12)
plt.grid(True)
plt.show()
