# binary search (бинарный поиск)
# работает только для упорядоченного массива
# сложность log(n)
def binary_search(my_list, item):
    high = len(my_list) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2

        guess = my_list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == '__main__':
    result = binary_search([1, 3, 5, 7, 8, 9, 11], 9)
    print('Position is', result)
