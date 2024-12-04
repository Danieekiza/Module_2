# for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True # флаг
for i in numbers[1:]:  # берем последовательно значения из списка кроме "1"
    for j in numbers[1:i - 1]:  # проверяме значение из списка от 2 до i не включительно
        if (i % j) == 0:  # если делится без остатка, то i составное число
            is_prime = False # False  - число составное
            break  # достаточно одного множителя для проверки
    if is_prime == False:
        not_primes.append(i)
    else:
        primes.append(i)
    is_prime = True  # возвращаем значение по-умолчанию
print('Primes:', primes)
print('Not Primes:', not_primes)
