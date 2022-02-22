#!/usr/bin/env python3

def without_remainder(num, divider):
    return num // divider * divider

def print_to_result(pos, num):
    spaces = " " * (max(0, pos - len(str(num)) + 1))
    if num != None:
        print(f"{spaces}{num}")

def print_results(pos, num, divider):
    wo_remainder = without_remainder(num, divider)
    print_to_result(pos, num)
    print_to_result(pos, wo_remainder)

def long_division(dividend, divider):
    print(f"{dividend}|{divider}")

    str_dividend = str(dividend)
    num = 0
    size = len(str_dividend)
    pos = -1
    is_first = True

    while (pos < size - 1):
        pos += 1
        num = num * 10 + int(str_dividend[pos])

        if num // divider == 0:
            continue
        if is_first:
            spaces = " "* (max(0, len(str_dividend) - pos - 1))
            print(f"{without_remainder(num, divider)}{spaces}|{dividend // divider}")
            is_first = False
        else:
            print_results(pos, num, divider)

        num %= divider

    print_to_result(pos, num)

def main():
    print(long_division(123, 123))
    print()
    print(long_division(1, 1))
    print()
    print(long_division(15, 3))
    print()
    print(long_division(3, 15))
    print()
    print(long_division(12345, 25))
    print()
    print(long_division(1234, 1423))
    print()
    print(long_division(87654532, 1))
    print()
    print(long_division(24600, 123))
    print()
    print(long_division(4567, 1234567))
    print()
    print(long_division(246001, 123))
    print()
    print(long_division(100000, 50))
    print()
    print(long_division(123456789, 531))
    print()
    print(long_division(425934261694251, 12345678))


if __name__ == '__main__':
    main()
