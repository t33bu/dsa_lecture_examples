from math import sqrt

def jump_search(arr, key):
    n = len(arr)
    step = int(sqrt(n))
    i = 0
    print(f"Searching for {key} in {arr}")
    print(f"Using steps of size {step}")

    # Jump ahead
    while i < n and arr[i] < key:
        print(f"Jumping from index {i} to {min(i + step, n) - 1}")
        i += step

    # Linear search in previous block
    start = max(0, i - step)
    print(f"Linear search in block [{start}, {min(i + 1, n) - 1}]")
    for j in range(start, min(i + 1, n)):
        print(f"Checking index {j} with value {arr[j]}")
        if arr[j] == key:
            return j

    return -1
		
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 ]
print(jump_search(my_list, 90))