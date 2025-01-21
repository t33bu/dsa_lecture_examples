def bubble_sort(array):
    swaps = 0
    comps = 0
    # loop to access each element (p = pass)
    for p in range(len(array)):    
        print("---- next p ----")
        # loop to compare elements (j = index of element)
        # -p skips the last element in each pass
        # as its in correct place in the list
        for j in range(0, len(array) -p -1):
            print(array)            
            # compare two adjacent elements
            # swap if needed
            comps = comps + 1
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps = swaps+1
        print(array)
    print("comparisons:",str(comps))
    print("swaps:",str(swaps))
        
#data = [12, 2, 4, 8, 6, 10 ]
#bubble_sort(data)

worst_case_data = [10, 8, 6, 4, 2 ]
bubble_sort(worst_case_data)

