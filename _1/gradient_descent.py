# f(x) = x^2+2x+2


def derivative(x: float) -> float:
    return 2 * x + 2


def gradient(x: float, step: float = 0.01):
    while True:
        old_x = x
        der = derivative(old_x)
        x = old_x - step * der
        if (x - old_x) < 0.00000000000001:
            break

    print(f'Минимум: {x}')


def res():
    x = float(input('Введите X: '))
    gradient(x)


res()
