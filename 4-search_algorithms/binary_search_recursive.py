def binary_search(arr, key):
    print(f"arr is {arr}")
    if len(arr) == 0:
        return False
    mid_point = len(arr) // 2
    print(f"mid_point is {arr[mid_point]}")
    if key == arr[mid_point]:
        return True
    else:
        if key < arr[mid_point]:
            print(f"key {key} is less than {arr[mid_point]}")
            arr = arr[:mid_point]
            return binary_search(arr, key)
        else:
            print(f"key {key} is greater than {arr[mid_point]}")   
            arr = arr[mid_point+1:] 
            return binary_search(arr, key)

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 130, 140 ]
print(binary_search(my_list, 80))