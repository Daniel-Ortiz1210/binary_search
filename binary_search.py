def binary_search(array, n):

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == n:
            return mid
        elif array[mid] < n:
            low = mid + 1
        elif array[mid] > n:
            high = mid - 1
        else:
            return -1


array = [0, 3, 4, 5, 6, 7, 9, 10, 24, 25, 29, 30, 45, 100]

searching = binary_search(array, 45)

print(searching)


