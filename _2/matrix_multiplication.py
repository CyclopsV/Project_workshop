def set_matrix():
    matrix = []
    i = 1
    len_row = 0
    while True:
        row = input(f'Введите {i} строку: ').strip().split(' ')
        if row[0].lower() == 'z':
            raise Exception('Ввод матрицы отменен')
        elif row[0].lower() == 'n':
            break
        if len_row == 0:
            len_row = len(row)
        else:
            if len(row) != len_row:
                raise Exception('Введенный ряд не соответсвует размеру предыдущего')
        for j in range(len(row)):
            row[j] = int(row[j])
        matrix.append(row)
        i += 1
    return matrix


def matrix_multiplication(first, second):
    if len(first[0]) != len(second):
        raise Exception(f'Невозможно умножить матрицы (A: {len(first[0])}X{len(first)}; B: {len(second[0])}X{len(second)})')
    matrix = []
    for i in range(len(first)):
        row_matrix = []
        for j in range(len(second[0])):
            summ = 0
            for k in range(len(first)):
                mul = first[i][k] * second[k][j]
                summ = summ + mul
            row_matrix.append(summ)
        matrix.append(row_matrix)
    return matrix


def start():
    print('Вводите числа через пробел\nДля отменны ввода z. Для перехода к следующему шагу n.')
    print('Ввод первой матрицы')
    first_matrix = set_matrix()
    print('Ввод второй матрицы')
    second_matrix = set_matrix()
    print('\nПервая матрица:')
    for i in first_matrix:
        print(i)
    print('\nВторая матрица:')
    for i in second_matrix:
        print(i)
    res = matrix_multiplication(first_matrix, second_matrix)
    print('\nРезультат:')
    for i in res:
        print(i)


start()
