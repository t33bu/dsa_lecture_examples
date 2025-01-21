def merge_sort(array):
    # stop condition
    if (len(array) > 1):
        mid = len(array) // 2
        print("current array",array)
        left_array = array[:mid]
        right_array = array[mid:]
        print("split",left_array,"-",right_array)
        # recursive calls
        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0
        # merge and sort
        # find position for the current (smallest) item
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i = i + 1
            else:
                array[k] = right_array[j]
                j = j + 1
            k = k + 1        
        # handle the rest of left array
        while i < len(left_array):
            array[k] = left_array[i]
            i = i + 1
            k = k + 1
        # handle the rest of right array
        while j < len(right_array):
            array[k] = right_array[j]
            j = j + 1
            k = k + 1
        print("merge and sort:", array)

data = [8, 2, 6, 3, 4, 3, 3, 1 ]
merge_sort(data)
		