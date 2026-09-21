# Fibonacci series: 1, 1, 2, 3, 5, 8, 13, 21, ...

def check_fibonacci(arr):
    if len(arr) < 3:
        return False
    for i in range(2, len(arr)):
        if arr[i] != arr[i-1] + arr[i-2]:
            return False
    return True

# This is a list in python    
my_array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]

print(check_fibonacci(my_array))
