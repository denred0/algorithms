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
    while (my_list) > 0:
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


# Быстрая сортировка
# базовый случай это пустой массив или массив из 1 элемента
# выбираем опорный элемент и все значения меньше него перемещаем влево, а все значения больше вправо
# потом применяем быструю сортировку для левой и правой части
def quicksort(my_list):
    if len(my_list) < 2:
        return my_list

    pivot = my_list[len(my_list) // 2]  # опроным элементом выбираем средний элемент
    my_list.pop(len(my_list) // 2)

    less = [i for i in my_list if i <= pivot]
    greater = [i for i in my_list if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


# пузырьковая сортировка
def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


# сортировка слиянием
def mergeSort(my_list):
    print("Splitting ", my_list)
    if len(my_list) > 1:
        mid = len(my_list) // 2
        lefthalf = my_list[:mid]
        righthalf = my_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                my_list[k] = lefthalf[i]
                i = i + 1
            else:
                my_list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            my_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            my_list[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", my_list)


if __name__ == '__main__':
    result = mergeSort([7, 5, 89, 1, 6])
    print(result)
