def insertion_sort(array):
    shifts = 0
    # start from index 1 as index 0 considered sorted
    for p in range(1,len(array)):
        print("---- next p ----")    
        value = array[p]
        pos = p	
        # go through sorted part to find the index
        # where value is smaller than current value
        while pos > 0 and array[pos-1] > value:
            # shift previous greater values to right
            # to make space in the array
            array[pos] = array[pos-1]
            pos = pos-1	
            shifts = shifts+1
        # when sorted items are no longer greater
        # that is new place for current value
        print("value",value,"sorted pos",pos)
        array[pos] = value
        print(array)
                
    print("shifts:",str(shifts))

#data = [6, 5, 4, 3, 2, 1 ]
#print(data)
#insertion_sort(data)

another_data = [6, 1, 5, 2, 4, 3 ]
print(another_data)
insertion_sort(another_data)
