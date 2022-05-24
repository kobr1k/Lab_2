"""
17. Дано три цілих числа. Визначте, скільки серед них збігаються. Програма повинна вивести одне з
чисел: 3 (якщо все збігаються), 2 (якщо два збігається) або 0 (якщо все числа різні)
"""


def main(a: float, b: float, c: float):
    if a == b == c:
        return 3
    elif a != b == c or b != a == c or c != b == a:
        return 2
    elif a != b != c:
        return 0


if __name__ == '__main__':
    x1 = int(input('Enter x1: '))
    x2 = int(input('Enter x2: '))
    x3 = int(input('Enter x3: '))

    result = main(x1, x2, x3)
    print(result)