def merge_sort(array):
    # stop condition
    if (len(array) > 1):
        mid = len(array) // 2
        print("array now",array)
        left_array = array[:mid]
        right_array = array[mid:]
        print("      split",left_array,"-",right_array)
        # recursive calls
        merge_sort(left_array)
        merge_sort(right_array)

        # merge and sort
        i = 0
        j = 0
        k = 0
        # while: find position for the current item,
        # which can in either left or right subarray
        # Note that subarrays are already sorted (combined results)
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i = i + 1
            else:
                array[k] = right_array[j]
                j = j + 1
            k = k + 1        
        # while: if left has items left, handle them
        while i < len(left_array):
            array[k] = left_array[i]
            i = i + 1
            k = k + 1
        # while: if right has items left, handle them
        while j < len(right_array):
            array[k] = right_array[j]
            j = j + 1
            k = k + 1
        print("      merge and sort:", array)

data = [8, 2, 6, 3, 4, 3, 3, 1 ]
print("---- initial ----")
print(data)
merge_sort(data)
print("---- result ----")
print(data)

		