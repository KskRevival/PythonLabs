unicode_size = 1105
key_max = 1


def standard_search(hay, needle):
    border = len(hay) - len(needle) + 1
    len_needle = len(needle)
    for i in range(border):
        if needle == hay[i:i + len_needle]:
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
        if curr_hash == needle_hash and needle == hay[i - len_needle: i]:
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
    prefix_table = [0] * len_text
    for i in range(1, len_text):
        curr = prefix_table[i - 1]
        while curr > 0 and text[curr] != text[i]:
            curr = prefix_table[curr - 1]
        if text[curr] == text[i]:
            curr = curr + 1
        prefix_table[i] = curr
    return prefix_table


def kmp(hay, needle):
    prefix_table = prefix(needle)
    curr = 0
    for i in range(len(hay)):
        while curr > 0 and needle[curr] != hay[i]:
            curr = prefix_table[curr - 1]
        if needle[curr] == hay[i]:
            curr = curr + 1
        if curr == len(needle):
            return i - len(needle) + 1
    return -1


class AhoNode:
    ''' Вспомогательный класс для построения дерева
    '''
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None


def aho_create_forest(patterns):
    '''Создать бор - дерево паттернов
    '''
    root = AhoNode()

    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root


def aho_create_statemachine(patterns):
    '''Создать автомат Ахо-Корасика.
    Фактически создает бор и инициализирует fail-функции
    всех узлов, обходя дерево в ширину.
    '''
    # Создаем бор, инициализируем
    # непосредственных потомков корневого узла
    root = aho_create_forest(patterns)
    queue = []
    for node in root.goto.values():
        queue.append(node)
        node.fail = root

    # Инициализируем остальные узлы:
    # 1. Берем очередной узел (важно, что проход в ширину)
    # 2. Находим самую длинную суффиксную ссылку для этой вершины - это и будет fail-функция
    # 3. Если таковой не нашлось - устанавливаем fail-функцию в корневой узел
    while len(queue) > 0:
        rnode = queue.pop(0)

        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode is not None and key not in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out

    return root


def aho_find_all(s, root, callback):
    '''Находит все возможные подстроки из набора паттернов в строке.
    '''
    node = root

    for i in range(len(s)):
        while node is not None and s[i] not in node.goto:
            node = node.fail
        if node is None:
            node = root
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            callback(i - len(pattern) + 1, pattern)


def on_occurence(pos, patterns):
    print("At pos %s found pattern: %s" % (pos, patterns))

patterns = ['a', 'ab', 'abc', 'bc', 'c', 'cba']
s = "abcba"
root = aho_create_statemachine(patterns)
aho_find_all(s, root, on_occurence)
