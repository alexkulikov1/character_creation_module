from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Функция."""
    if your_number <= 0:
        return
    the_end_sqrt = CalculateSquareRoot(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа.', end=' ')
    print(f'Это будет: {the_end_sqrt}')


calc(25.5)
