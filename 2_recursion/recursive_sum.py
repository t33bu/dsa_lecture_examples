def recursive_sum(list):
    if len(list) == 0:  
        return 0
    else:
        num = list.pop() # remove last element
        print(num, '+', list)
        temp = num + recursive_sum(list) # return last elem + remaining list
        print('result',temp)
        return temp
    
my_numbers = [1, 3, 5, 7, 9, 11]
print(my_numbers)
recursive_sum(my_numbers)

