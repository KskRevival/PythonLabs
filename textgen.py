import string
import random as r


ascii_uppercase = string.ascii_uppercase
digits = string.digits


def get_fixed_text(needle_size, position):
    needle = 'a{0}'.format(''.join(r.choice(ascii_uppercase + digits)
                                   for _ in range(needle_size)))
    hay = ''.join(r.choice(ascii_uppercase + digits)
                  for _ in range(position)) + needle
    return hay, needle


def get_random_text(needle_size, position):
    needle = ''.join(r.choice(ascii_uppercase + digits)
                     for _ in range(needle_size))
    hay = ''.join(r.choice(ascii_uppercase + digits)
                  for _ in range(position))
    return hay, needle
