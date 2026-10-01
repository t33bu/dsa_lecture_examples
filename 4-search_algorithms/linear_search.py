def linear_search(arr, key):
    print(f"Searching for {key} in {arr}")
    for v in arr:
        print(f"value is {v}")
        if v == key:
            return True
    return False

my_list = [20, 50, 80, 60, 70, 10, 30, 40 ]
print(linear_search(my_list, 30))
