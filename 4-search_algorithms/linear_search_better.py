def linear_search_better(arr, key):
    print(f"Searching for {key} in {arr}")
    for v in arr:
        print(f"value is {v}")
        if v == key:
            return True
        if v > key:
            print(f"Value {v} greater than {key}, stopping")   
            return False
    return False

my_list = [10, 20, 30, 40, 50, 60, 70, 80 ]
print(linear_search_better(my_list, 60))

