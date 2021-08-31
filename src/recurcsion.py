# простейшая рекурсия
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def recursion_sum(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + recursion_sum(my_list[1:])


def recursion_counts(my_list):
    if len(my_list) == 1:
        return 1
    else:
        return 1 + recursion_counts(my_list[1:])


def recursion_max_value(my_list):
    if len(my_list) == 2:
        return my_list[0] if my_list[0] > my_list[1] else my_list[1]
    submax = recursion_max_value(my_list[1:])
    return my_list[0] if my_list[0] > submax else submax


# бинарный поиск через стратегию разделяй и властвуй
# базовый случай это массив с одним элементом
def binary_search(my_list, search_value):
    if len(my_list) == 1:
        if my_list[0] == search_value:
            return print('1')
        else:
            return print('0')

    low = 0
    high = len(my_list) - 1
    mid = (low + high) // 2

    if search_value > my_list[mid]:
        return binary_search(my_list[mid + 1:], search_value)
    else:
        return binary_search(my_list[:mid - 1], search_value)


if __name__ == '__main__':
    # print(fact(3))

    # print(recursion_sum([1, 2, 3, 4, 5, 80]))

    # print(recursion_counts([1, 2, 3, 4, 5, 80, 4]))

    # print(recursion_max_value([9, 2, 3, 7]))

    binary_search([1, 3], 3)
