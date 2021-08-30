# Сортировка выбором
# находим наименьший элемент и вставляем его в новый массив, а из старого удаляем
# в результате надо найти минимальное значение, пробежав по всему списку это O(n)
# и так надо сделать n раз - по количеству элементов.
# Итоговая сложность O(n2). По мере уменьшения элементов в списке время вроде бы уменьшается,
# но все равно считается сложность O(n2)
def selectionSort(my_list):
    if not my_list:
        return []

    sorted_list = []

    # Здесь сложность O(n) - надо выполнить операцию поиска наименьшего элемента
    # количество раз равное количеству элементов в массиве
    while len(my_list) > 0:
        min_value = my_list[0]
        ind = 0

        # Здесь cложность тоже O(n) - бежим по всему массиву, чтобы найти наименьший
        for i in range(1, len(my_list)):
            if my_list[i] < min_value:
                min_value = my_list[i]
                ind = i
        sorted_list.append(min_value)
        my_list.pop(ind)

    return sorted_list


if __name__ == '__main__':
    result = selectionSort([7, 5, 89, 1, 6])
    print(result)
