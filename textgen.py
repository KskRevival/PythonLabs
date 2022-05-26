import string
import random as r


def get_fixed_text(needle_size, position):
    needle = 'a{0}'.format(''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(needle_size)))
    hay = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(position)) + needle
    return hay, needle


def get_random_text(needle_size, position):
    needle = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(needle_size))
    hay = ''.join(r.choice(string.ascii_uppercase + string.digits) for _ in range(position))
    return hay, needle
