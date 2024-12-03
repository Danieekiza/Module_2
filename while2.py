# while, continue, break
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0  # начальный индекс = 0
end_list = []  # список для добавления значений
while True:
    if i == len(my_list):  # если индекс сравнялся с длиной my_list - break
        break
    elif my_list[i] < 0:  # если встретили отрицательное значение - break
        break
    elif my_list[i] == 0:  # если 0, то добавляем индекс +1 и скипаем
        i = i + 1
        continue
    else:  # добавляем в end_list значение и к индексу +1
        end_list.append(my_list[i])
        i = i + 1
print(end_list)
