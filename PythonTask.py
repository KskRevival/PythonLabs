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
    key_max /= key
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
    needle1 = needle[::-1]

    for i in range(len_needle):
        if table[ord(needle1[i])] == len_needle:
            table[ord(needle1[i])] = i

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
    needle = 'a'
    hay = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(position)) + 'a'
    return (hay, needle)


def get_random_text(needle_size, position):
    needle = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(needle_size))
    hay = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(position))
    return (hay, needle)


if __name__ == '__main__':
    #hay = input()
    #needle = input()
    (hay, needle) = get_fixed_text(10, 10000)
    print(f"Обычный: {standard_search(hay, needle)}")
    print(f"Рабин-Карп: {rabin_karp(hay, needle)}")
    print(f"Бойер-Мур: {bauer_moore(hay, needle)}")
    print(f"Кнут-Моррис-Пратт: {kmp(hay, needle)}")
    (hay, needle) = get_random_text(1, 10000)
    print(f"Обычный: {standard_search(hay, needle)}")
    print(f"Рабин-Карп: {rabin_karp(hay, needle)}")
    print(f"Бойер-Мур: {bauer_moore(hay, needle)}")
    print(f"Кнут-Моррис-Пратт: {kmp(hay, needle)}")
