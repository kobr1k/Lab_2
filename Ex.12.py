"""
12. Дано чотири цілих числа, одне з яких відмінно від трьох інших, рівних між собою. Вивести
порядковий номер цього числа.
"""


def main(num_1: int, num_2: int, num_3: int, num_4: int):
    if num_1 != (num_2 == num_3 == num_4):
        return 1
    if num_2 != (num_1 == num_3 == num_4):
        return 2
    if num_3 != (num_1 == num_2 == num_4):
        return 3
    if num_4 != (num_1 == num_2 == num_3):
        return 4


if __name__ == '__main__':
    n_1 = int(input(f'Введіть чотири цілих числа:\nx1 = '))
    n_2 = int(input(f'x2 = '))
    n_3 = int(input(f'x3 = '))
    n_4 = int(input(f'x4 = '))

    result = main(n_1, n_2, n_3, n_4)
    print(result)