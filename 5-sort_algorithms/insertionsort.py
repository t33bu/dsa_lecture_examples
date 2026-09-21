def insertion_sort(array):
    shifts = 0
    # start from index 1 as index 0 considered sorted
    for p in range(1,len(array)):
        print("---- pass=",p," ----")
        value = array[p]
        pos = p	
        print("cur", value, array)                
        # find the place in sorted part
        while pos > 0 and array[pos-1] > value:
            # shift previous greater values to right
            # to make space in the array
            array[pos] = array[pos-1]
            pos = pos-1	
            shifts = shifts+1
        # when sorted items are no longer greater
        # -> new place for the current value
        array[pos] = value
        print("shift", array)
    print("---- result ----")
    print(array)                
    print("shifts:",str(shifts))

data = [6, 5, 4, 3, 2, 1 ]
print("---- initial ----")
print(data)
insertion_sort(data)

#data = [6, 1, 5, 2, 4, 3 ]
#print("---- initial ----")
#print(data)
#insertion_sort(data)
