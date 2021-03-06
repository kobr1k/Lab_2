"""
7. Одиниці маси пронумеровані в такий спосіб: 1 - кілограм, 2 - міліграм, 3 - грам, 4 - тонна, 5 -
центнер. Дано номер одиниці маси (ціле число в діапазоні 1-5) і маса тіла в цих одиницях (дійсне
число). Знайти масу тіла в кілограмах.
"""


def main(mass_, value_):
    calc = {
        1: [mass_, ' кілограм'],
        2: [mass_ * 10000, ' міліграм'],
        3: [mass_ * 1000, ' грам'],
        4: [mass_ / 1000, ' тонн'],
        5: [mass_ / 100, ' центнер']
    }
    ret = calc.get(value_, 'Error')
    output = ''.join([str(i) for i in ret])
    return output


if __name__ == '__main__':
    mass = float(input(f'Введіть массу:\n-'))
    print('Введіть одиницю масси:\n'
          '1 - кілограм,\n'
          '2 - міліграм,\n'
          '3 - грам,\n'
          '4 - тонна,\n'
          '5 - центнер.'
          )
    value = int(input('-'))
    result = main(mass, value)
    print(result)
