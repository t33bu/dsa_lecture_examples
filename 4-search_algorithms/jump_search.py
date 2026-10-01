from math import floor, sqrt

def jump_search(arr, key):
    n = len(arr)
    step  = floor(sqrt(n))
    prev  = 0
    print(f"Searching for {key} in {arr}")
    print(f"Using steps of size {step}")

    while arr[min(step, n) - 1] < key:   # jump forward
        print(f"Jumping from index {prev} to {min(step, n) - 1}")
        prev = step
        step = step + floor(sqrt(n))
        if prev >= n: 
            return -1
    while arr[prev] < key:               # linear scan in block
        print(f"Linear scan: index {prev} has {arr[prev]}")
        prev = prev + 1
        if prev == min(step, n): 
            return -1
				
    if arr[prev] == key: 
        print(f"Linear scan: index {prev} has {arr[prev]}")
        return prev    
	
    return False
		
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 ]
print(jump_search(my_list, 90))