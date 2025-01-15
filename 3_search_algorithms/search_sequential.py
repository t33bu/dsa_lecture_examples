def sequential_search(list, value):
    for v in list:
        print(v, end=" ")
        if v == value:
            return True
    return False

my_list = [20, 50, 80, 60, 70, 10, 30, 40 ]
print(sequential_search(my_list, 62))
