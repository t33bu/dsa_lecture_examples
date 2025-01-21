def selection_sort(array):
    comps = 0
    swaps = 0
    # loop to access each element (p = pass)
    for p in range(len(array)):
        print("---- next p ----")
        print(array)
        # initialize min_index to current p,
        # so the first element is considered minimum
        min_index = p
        # go through remaining elements to find minimum index
        for r in range(p + 1, len(array)):
            comps = comps + 1
            if array[r] < array[min_index]:
                min_index = r
        # swap the elements to sort the array
        #if p != min_index: 
        print("swap:",str(array[p]),str(array[min_index]))
        array[p], array[min_index] = array[min_index], array[p]
        swaps = swaps + 1
    print("---------")
    print(array)
    print("comparisons:",str(comps))
    print("swaps:", str(swaps))
    
data = [6, 5, 4, 3, 2, 1 ]
print(data)
selection_sort(data)

