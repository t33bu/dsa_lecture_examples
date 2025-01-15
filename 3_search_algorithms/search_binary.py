def binary_search(list, value):
    print("list=", list)
    if len(list) == 0:
        return False
    mid_point = len(list) // 2
    print("next mid_point=", list[mid_point]) 
    if value == list[mid_point]:
        return True
    else:
        if value < list[mid_point]:
            list = list[:mid_point]
            return binary_search(list, value)
        else:
            list = list[mid_point+1:] 
            return binary_search(list, value)

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 ]
print(binary_search(my_list, 135))