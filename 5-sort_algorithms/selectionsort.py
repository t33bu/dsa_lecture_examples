def selection_sort(array):
    comps = 0
    swaps = 0
    # loop to access each element (p = pass)
    for p in range(len(array)):
        print("---- pass=",p," ----")
        print(array)
        # initialize min_index to current p,
        # so the first element is considered minimum
        min_index = p
        # find minimum index by going through remaining elements
        for r in range(p + 1, len(array)):
            comps = comps + 1
            if array[r] < array[min_index]:
                min_index = r
        print("min=", array[min_index], end=" -> ")
        # optimization: if current p in the minimum,
        # no need to swap
        if p != min_index: 
            print("swap:",array[p],array[min_index])
            array[p], array[min_index] = array[min_index], array[p]
            swaps = swaps + 1
        else:
            print("no swap needed")
    print("---- result ----")
    print(array)
    print("comparisons:",comps)
    print("swaps:", swaps)

#data = [12, 2, 4, 8, 6, 10 ]
#print("---- initial ----")
#print(data)
#selection_sort(data)

data = [10, 8, 6, 4, 2 ]
print("---- initial ----")
print(data)
selection_sort(data)

