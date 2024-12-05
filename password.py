# dop_homework
def password(n):
    if n in range(3, 21):  # n от 3 до 20
        dict_ = {n: ''}
        c = ''
        for j in range(1, 21):  # Пары чисел подбираются от 1 до 20 для текущего числа.
            for k in range(j + 1, 21):  # Пары чисел подбираются от 1 до 20 для текущего числа.
                if n % (j + k) == 0:
                    c += str(j) + str(k)

        dict_.update({n: c})

        return *dict_.keys(), *dict_.values()  # выводим только значения
    else:
        return n, 'не в списке'


n, pswrd = password(int(input('Введите число из первого поля: ')))

print(f'{n} - {pswrd}')  # вывод точно как в примере задачи
