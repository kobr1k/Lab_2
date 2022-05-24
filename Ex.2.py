"""
2. Дано три цілих числа. Знайти кількість додатних чисел в початковому наборі.
"""


def main(x1, x2, x3):
    number = [x1, x2, x3]
    n = 0
    for numbers in number:
        if numbers > 0:
            n += 1
    return n


if __name__ == '__main__':
    num_1 = int(input('x1 = '))
    num_2 = int(input('x2 = '))
    num_3 = int(input('x3 = '))

    result = main(num_1, num_2, num_3)
    print(result)

