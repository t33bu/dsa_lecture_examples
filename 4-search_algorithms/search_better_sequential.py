def better_seq_search(list, value):
    for v in list:
        print(v, end=" ")
        if v == value:
            return True
        if v > value:
            print("Value is greater!")   
            return False
    return False

my_list = [10, 20, 30, 40, 50, 60, 70, 80 ]
print(better_seq_search(my_list, 82))

