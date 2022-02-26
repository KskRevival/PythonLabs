#!/usr/bin/env python3


def long_division(dividend, divider):
  answer = ""
    quotient = dividend // divider
    rest = dividend % divider
    zero_count = 0
    indent = 0
    curr_pos = 0
    printed_pos = 0
    down_div = int(str(quotient)[curr_pos]) * divider
    curr_pos += len(str(down_div))
    up_div = int(str(dividend)[:curr_pos])
    printed_len = len(str(down_div))
    answer += str(dividend) + "|" + str(divider) + "\n"
    len_dividend = len(str(dividend))

    if dividend >= divider:
        if divider == 1:
            answer += str(str(dividend)[0]) + " " * (len_dividend - 1) \
                      + "|" + str(quotient) + "\n"
            for j in str(dividend)[1:]:
                answer += " " * curr_pos + str(j) + "\n"
                answer += " " * curr_pos + str(j) + "\n"
                curr_pos += 1
            answer += " " * (len_dividend - 1) + "0"
        else:
            answer += str(down_div) + " " * (len_dividend - len(str(down_div)))
            answer += "|" + str(quotient) + "\n"
            for i in range(len(str(quotient)) - 1):
                indent += len(str(up_div)) - len(str(up_div - down_div))
                up_div = int(str(up_div - down_div) + str(dividend)[curr_pos])
                down_div = int(str(quotient)[i + 1]) * divider
                curr_pos += 1
                len_up_div = len(str(up_div))
                len_down_div = len(str(down_div))
                if up_div > 0 and down_div > 0:
                    indent -= zero_count
                    zero_count = 0
                    answer += " " * indent + str(up_div) + "\n"
                    answer += " " * (indent + len_up_div - len_down_div)
                    answer += str(down_div) + "\n"
                    printed_pos = indent + len_up_div - len_down_div
                    printed_len = len_down_div
                elif down_div == 0:
                    zero_count += 1
                    indent += 1

            indent += len(str(up_div)) - len(str(up_div - down_div))
            if rest != 0:
                answer += " " * indent + str(rest)
            else:
                answer += " " * (printed_pos + printed_len - 1) + str(rest)
    else:
        answer += str(rest) + "|" + str(quotient)

    return answer


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
