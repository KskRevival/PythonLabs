import tracemalloc
from datetime import datetime
import matplotlib.pyplot as plt
import string
import random as r


unicode_size = 1105
key_max = 1


def standard_search(hay, needle):
    border = len(hay) - len(needle) + 1
    len_needle = len(needle)
    for i in range(border):
        if needle == hay[i:i+len_needle]:
            return i
    return -1


def full_hash(needle, key):
    global key_max
    curr_hash = 0
    for i in range(len(needle)):
        curr_hash += key_max * (ord(needle[i]) % key)
        key_max *= key
    key_max //= key
    return curr_hash


def rabin_karp(hay, needle):
    global key_max
    key = 37
    len_hay, len_needle = len(hay), len(needle)
    needle_hash = full_hash(needle, key)
    key_max = 1
    curr_hash = full_hash(hay[:len_needle], key)

    for i in range(len_needle, len_hay):
        if curr_hash == needle_hash and needle == hay[i - len_needle: i ]:
            return i - len_needle
        curr_hash = int(curr_hash // key + key_max * (ord(hay[i]) % key))

    if needle == hay[-len_needle:]:
        return len_hay - len_needle
    return -1


def create_table(needle):
    len_needle = len(needle)
    table = [len_needle for i in range(unicode_size)]

    for i in range(len_needle):
        if table[ord(needle[i])] == len_needle:
            table[ord(needle[i])] = len_needle - i

    return table


def bauer_moore(hay, needle):
    table = create_table(needle)
    len_hay = len(hay)
    len_needle = shift = needle_pos = ptr = len(needle)
    while shift <= len_hay and needle_pos > 0:
        if needle[needle_pos - 1] == hay[ptr - 1]:
            needle_pos -= 1
            ptr -= 1
        else:
            shift += table[ord(hay[ptr - 1])]
            ptr = shift
            needle_pos = len_needle
    if needle_pos <= 0:
        return ptr
    return -1


def prefix(text):
    len_text = len(text)
    prefix_table = [0]*len_text
    for i in range(1, len_text):
        curr = prefix_table[i-1]
        while curr > 0 and text[curr] != text[i]:
            curr = prefix_table[curr-1]
        if text[curr] == text[i]:
            curr = curr + 1
        prefix_table[i] = curr
    return prefix_table


def kmp(hay, needle):
    prefix_table = prefix(needle)
    curr = 0
    for i in range(len(hay)):
        while curr > 0 and needle[curr] != hay[i]:
            curr = prefix_table[curr-1]
        if needle[curr] == hay[i]:
            curr = curr + 1
        if curr == len(needle):
            return i - len(needle) + 1
    return -1


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
        standard.append(benchmark(standard_search, hay, needle, isTime))
        rabin.append(benchmark(rabin_karp, hay, needle, isTime))
        bauer.append(benchmark(bauer_moore, hay, needle, isTime))
        res_kmp.append(benchmark(kmp, hay, needle, isTime))
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
