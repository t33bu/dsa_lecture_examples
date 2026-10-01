def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    print(f"Searching for {key} in {arr}")
    # data set indices [low....high]

    while low <= high:
        # get middle point
        mid = (low + high) // 2
        print(f"low: {low}, high: {high}, mid: {mid}, arr[mid]: {arr[mid]}")
        # check if key found
        if arr[mid] == key:
            return mid
        # discard lower half
        elif arr[mid] < key:
            low = mid + 1
        # discard upper half
        else:
            high = mid - 1

    return -1

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 ]
print(binary_search_iterative(my_list, 80))