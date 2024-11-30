# if_elif_else
first = input('Введите первое (целое) число: ')
second = input('Введите второе (целое) число: ')
third = input('Введите третье (целое) число: ')
if first == second == third:
    count = 3
elif first == second or second == third or first == third:
    count = 2
else:
    count = 0
print('Совпадений:',count)
