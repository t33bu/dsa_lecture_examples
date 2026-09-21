"""
Algorithm Analysis using t(n) - Resource Complexity Function

t(n) represents the resources (time/operations) needed to run an algorithm
as a function of input size n.
"""

def linear_search(arr, target):
    """
    Linear Search Algorithm

    t(n) Analysis - counting basic operations:
    - Loop iterations: up to n comparisons
    - Each iteration: 1 comparison operation

    Complete t(n):
    - Best case:  t(n) = 1              (found at index 0)
    - Worst case: t(n) = n              (found at last or not found)
    - Average:    t(n) = n/2            (found at middle on average)

    t(n) = n = O(n) - Linear time complexity
    """
    operations = 0

    for i in range(len(arr)):
        operations += 1  # Count each comparison
        if arr[i] == target:
            return i, operations

    return -1, operations


def sum_of_elements(arr):
    """
    Sum all elements in array

    t(n) Analysis:
    - Assignment:      1 operation
    - Loop iterations: n operations
    - Additions:       n operations
    - Return:          1 operation

    t(n) = 1 + n + n + 1 = 2n + 2

    Simplified: t(n) = O(n) - Linear
    """
    operations = 0

    total = 0
    operations += 1  # Assignment

    for num in arr:
        total += num
        operations += 2  # Loop check + addition

    operations += 1  # Return
    return total, operations


def nested_loop_example(n):
    """
    Nested Loop - Quadratic complexity

    t(n) Analysis - counting operations:
    - Outer loop runs: n times
    - Inner loop runs: n times for each outer iteration
    - Each inner iteration: 1 operation (count += 1)

    Complete t(n):
    t(n) = n * n = n^2 = O(n^2) - Quadratic
    """
    operations = 0
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1
            operations += 1

    return count, operations


def binary_search(arr, target):
    """
    Binary Search Algorithm (requires sorted array)

    t(n) Analysis - counting operations:
    - Each iteration: 1 comparison + midpoint calculation
    - Search space halves each time: n -> n/2 -> n/4 -> ... -> 1
    - After k iterations: n/2^k elements remain
    - Search ends when: n/2^k = 1, solving: k = log2(n)

    Complete t(n):
    t(n) = log2(n) comparisons = O(log n) - Logarithmic
    """
    operations = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        operations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, operations
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, operations


# ============================================================
# O(n log n) - LOG-LINEAR TIME EXAMPLES
# ============================================================

# Global counter for recursive functions
operation_counter = 0


def merge_sort(arr):
    """
    Merge Sort Algorithm - Divide and Conquer

    t(n) Analysis - counting operations:
    - Divide: Split array in half -> log2(n) levels of recursion
    - Conquer: At each level, merge all n elements total
    - Each merge comparison: 1 operation

    Complete t(n):
    t(n) = n operations/level * log2(n) levels = n * log2(n)
    t(n) = n * log2(n) = O(n log n) - Log-linear

    Visual breakdown for n=8:
    Level 0: [8 elements]           -> 8 operations to merge
    Level 1: [4] [4]                -> 8 operations to merge
    Level 2: [2] [2] [2] [2]        -> 8 operations to merge
    Total levels: log2(8) = 3
    Total: 8 * 3 = 24 operations
    """
    global operation_counter
    operation_counter = 0
    result = _merge_sort_recursive(arr.copy())
    return result, operation_counter


def _merge_sort_recursive(arr):
    """Helper function for merge sort"""
    global operation_counter

    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = _merge_sort_recursive(arr[:mid])
    right = _merge_sort_recursive(arr[mid:])

    # Merge
    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted arrays"""
    global operation_counter
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        operation_counter += 1  # Comparison
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    while i < len(left):
        operation_counter += 1
        result.append(left[i])
        i += 1

    while j < len(right):
        operation_counter += 1
        result.append(right[j])
        j += 1

    return result


def log_linear_loop(n):
    """
    Simple n log n pattern - outer loop * halving inner loop

    t(n) Analysis - counting operations:
    - Outer loop: runs n times
    - Inner loop: n -> n/2 -> n/4 -> ... -> 1 = log2(n) + 1 iterations
    - Each inner iteration: 1 operation

    Complete t(n):
    t(n) = n * (log2(n) + 1) = n*log2(n) + n = O(n log n) - Log-linear
    """
    operations = 0

    for i in range(n):           # O(n) - runs n times
        j = n
        while j > 0:             # O(log n) - halves each iteration
            operations += 1
            j = j // 2

    return operations


def halving_work_per_level(n):
    """
    Another n log n pattern demonstration

    t(n) Analysis - counting operations:
    - Outer while loop: n -> n/2 -> n/4 -> ... -> 1 = log2(n) + 1 levels
    - Inner for loop: n operations at each level

    Complete t(n):
    t(n) = n * (log2(n) + 1) = n*log2(n) + n = O(n log n)
    """
    operations = 0
    size = n

    while size > 0:              # O(log n) levels
        for i in range(n):       # O(n) work at each level
            operations += 1
        size = size // 2

    return operations


# ============================================================
# ADDITIONAL SIMPLE EXAMPLES
# ============================================================

def get_first_element(arr):
    """
    Access first element - Constant Time

    t(n) Analysis - counting operations:
    - Array index access arr[0]: 1 operation
    - Does not depend on array size n

    Complete t(n):
    t(n) = 1 = O(1) - Constant
    """
    operations = 1
    if len(arr) > 0:
        return arr[0], operations
    return None, operations


def get_element_at_index(arr, index):
    """
    Access element at any index - Constant Time

    t(n) Analysis - counting operations:
    - Array index lookup arr[index]: 1 operation
    - Same time whether array has 10 or 10 million elements

    Complete t(n):
    t(n) = 1 = O(1) - Constant
    """
    operations = 1
    return arr[index], operations


def find_maximum(arr):
    """
    Find the largest element in array

    t(n) Analysis - counting operations:
    - Initialize max_val: 1 operation
    - Loop through n-1 elements: n-1 iterations
    - Each comparison: 1 operation

    Complete t(n):
    t(n) = 1 + (n-1) = n = O(n) - Linear
    """
    operations = 1  # Initialize max_val
    max_val = arr[0]

    for i in range(1, len(arr)):
        operations += 1  # Comparison
        if arr[i] > max_val:
            max_val = arr[i]

    return max_val, operations


def count_occurrences(arr, target):
    """
    Count how many times target appears

    t(n) Analysis - counting operations:
    - Initialize counter: 1 operation
    - Loop through all n elements: n iterations
    - Each comparison: 1 operation

    Complete t(n):
    t(n) = 1 + n = n + 1 = O(n) - Linear
    """
    operations = 1  # Initialize count
    count = 0

    for item in arr:
        operations += 1  # Comparison
        if item == target:
            count += 1

    return count, operations


def is_sorted(arr):
    """
    Check if array is sorted in ascending order

    t(n) Analysis - counting operations:
    - Loop through n-1 adjacent pairs
    - Each comparison: 1 operation

    Complete t(n):
    - Best case:  t(n) = 1     (first pair not sorted, return early)
    - Worst case: t(n) = n - 1 (fully sorted, check all pairs)

    t(n) = n - 1 = O(n) - Linear
    """
    operations = 0

    for i in range(len(arr) - 1):
        operations += 1
        if arr[i] > arr[i + 1]:
            return False, operations

    return True, operations


def reverse_array(arr):
    """
    Reverse array in place

    t(n) Analysis - counting operations:
    - Loop runs until left meets right: n/2 iterations
    - Each swap: 1 operation

    Complete t(n):
    t(n) = n/2 = O(n) - Linear
    (n/2 grows linearly with n)
    """
    operations = 0
    result = arr.copy()
    left, right = 0, len(result) - 1

    while left < right:
        operations += 1
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return result, operations


def bubble_sort(arr):
    """
    Bubble Sort - Simple sorting algorithm

    t(n) Analysis - counting operations:
    - Outer loop: n iterations
    - Inner loop: (n-1) + (n-2) + ... + 1 comparisons
    - Sum formula: 1+2+...+(n-1) = (n-1)*n/2

    Complete t(n):
    t(n) = (n-1) + (n-2) + ... + 1 = n(n-1)/2 = (n^2 - n)/2
    t(n) = (n^2)/2 - n/2 = O(n^2) - Quadratic
    """
    operations = 0
    result = arr.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            operations += 1  # Comparison
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result, operations


def triangular_loop(n):
    """
    Triangular nested loop pattern

    t(n) Analysis - counting operations:
    - Outer loop: n iterations (i = 0 to n-1)
    - Inner loop: 1, 2, 3, ... n iterations
    - Sum: 1 + 2 + 3 + ... + n

    Complete t(n):
    t(n) = 1 + 2 + 3 + ... + n = n(n+1)/2 = (n^2 + n)/2
    t(n) = (n^2)/2 + n/2 = O(n^2) - Quadratic
    """
    operations = 0

    for i in range(n):
        for j in range(i + 1):
            operations += 1

    return operations


def print_pairs(arr):
    """
    Print all unique pairs in array

    t(n) Analysis - counting operations:
    - First element pairs with: n-1 others
    - Second element pairs with: n-2 others
    - ...and so on until last element

    Complete t(n):
    t(n) = (n-1) + (n-2) + ... + 1 = n(n-1)/2 = (n^2 - n)/2
    t(n) = (n^2)/2 - n/2 = O(n^2) - Quadratic
    """
    operations = 0
    pairs = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            operations += 1
            pairs.append((arr[i], arr[j]))

    return pairs, operations


def three_nested_loops(n):
    """
    Triple nested loop - Cubic complexity

    t(n) Analysis - counting operations:
    - Outer loop: n iterations
    - Middle loop: n iterations for each outer
    - Inner loop: n iterations for each middle
    - Each innermost: 1 operation

    Complete t(n):
    t(n) = n * n * n = n^3 = O(n^3) - Cubic
    """
    operations = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                operations += 1

    return operations


def simple_addition(a, b):
    """
    Add two numbers - Constant Time

    t(n) Analysis - counting operations:
    - One addition operation: a + b

    Complete t(n):
    t(n) = 1 = O(1) - Constant
    (Does not depend on input size)
    """
    operations = 1
    return a + b, operations


def factorial_iterative(n):
    """
    Calculate n! iteratively

    t(n) Analysis - counting operations:
    - Loop runs from 1 to n: n iterations
    - Each iteration: 1 multiplication

    Complete t(n):
    t(n) = n multiplications = n = O(n) - Linear
    """
    operations = 0
    result = 1

    for i in range(1, n + 1):
        operations += 1
        result *= i

    return result, operations


# ============================================================
# O(n!) - FACTORIAL TIME EXAMPLES
# ============================================================

def traveling_salesman_bruteforce(distances):
    """
    Traveling Salesman Problem (TSP) - Brute Force Solution

    Problem: Find the shortest route that visits all cities exactly once
    and returns to the starting city.

    t(n) Analysis - counting operations:
    - Number of permutations of n-1 cities: (n-1)!
    - For each permutation: n distance additions + 1 comparison
    - Total: (n-1)! * (n + 1) operations

    Complete t(n):
    t(n) = (n-1)! * (n + 1) = (n-1)! * n + (n-1)! = O(n!) - Factorial

    Growth of n!:
    - 5! = 120
    - 10! = 3,628,800
    - 15! = 1,307,674,368,000
    - 20! = 2,432,902,008,176,640,000

    This grows EXTREMELY fast - even 20 cities is practically unsolvable!
    """
    from itertools import permutations

    n = len(distances)
    operations = 0
    min_distance = float('inf')
    best_route = None

    # Generate all permutations of cities (except starting city 0)
    cities = list(range(1, n))

    for perm in permutations(cities):
        # Build complete route: 0 -> perm -> 0
        route = (0,) + perm + (0,)

        # Calculate total distance for this route
        total_distance = 0
        for i in range(len(route) - 1):
            operations += 1  # Count each distance lookup/addition
            total_distance += distances[route[i]][route[i + 1]]

        # Check if this is the best route
        operations += 1  # Comparison
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route

    return best_route, min_distance, operations


def generate_all_permutations(arr):
    """
    Generate all permutations of an array

    t(n) Analysis - counting operations:
    - Total permutations: n!
    - Recursive calls to generate: approximately n! * n
    - Work per call: constant

    Complete t(n):
    t(n) = n! * c (where c is constant work per permutation)
    t(n) = O(n!) - Factorial

    Example: [1,2,3] has 3! = 6 permutations:
    [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
    """
    operations = 0
    result = []

    def permute(current, remaining):
        nonlocal operations
        operations += 1

        if len(remaining) == 0:
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            permute(current, new_remaining)
            current.pop()

    permute([], arr)
    return result, operations


def generate_all_subsets(arr):
    """
    Generate all subsets (power set) of an array

    t(n) Analysis - counting operations:
    - Outer loop: 2^n iterations (one per subset)
    - Inner loop: n iterations (check each bit)
    - Each iteration: 1 operation

    Complete t(n):
    t(n) = 2^n * (1 + n) = 2^n + n*2^n = (n+1) * 2^n = O(2^n) - Exponential

    Example: [1,2,3] has 2^3 = 8 subsets:
    [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
    """
    operations = 0
    result = []
    n = len(arr)

    # Use binary counting: each number 0 to 2^n-1 represents a subset
    for i in range(2 ** n):
        operations += 1
        subset = []
        for j in range(n):
            operations += 1
            if i & (1 << j):  # Check if j-th bit is set
                subset.append(arr[j])
        result.append(subset)

    return result, operations


def fibonacci_recursive(n):
    """
    Fibonacci using naive recursion - Exponential time

    t(n) Analysis - counting operations:
    - Each call makes 2 recursive calls: fib(n-1) + fib(n-2)
    - Creates a binary tree of calls
    - Total calls: approximately 2^n (actually ~1.618^n, golden ratio)

    Complete t(n):
    t(n) = t(n-1) + t(n-2) + 1 (recurrence relation)
    t(n) approximately = 2^n = O(2^n) - Exponential

    Note: This is very inefficient! Use dynamic programming for O(n).
    """
    operations = [0]  # Use list to allow modification in nested function

    def fib(k):
        operations[0] += 1
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    result = fib(n)
    return result, operations[0]


# === DEMONSTRATION ===
if __name__ == "__main__":
    import random
    import math

    print("=" * 60)
    print("ALGORITHM ANALYSIS: t(n) Resource Function Examples")
    print("=" * 60)

    # Test with different input sizes
    sizes = [10, 100, 1000, 10000]
    small_sizes = [10, 50, 100, 200]

    # -----------------------------------------------------------
    # O(1) - CONSTANT TIME EXAMPLES
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(1) - CONSTANT TIME")
    print("=" * 60)

    print("\n1. GET FIRST ELEMENT - t(n) = 1 = O(1)")
    print("-" * 40)
    for n in sizes:
        arr = list(range(n))
        _, ops = get_first_element(arr)
        print(f"   n = {n:>5}  ->  t(n) = {ops} operation (always 1)")

    print("\n2. ARRAY INDEX ACCESS - t(n) = 1 = O(1)")
    print("-" * 40)
    for n in sizes:
        arr = list(range(n))
        _, ops = get_element_at_index(arr, n // 2)
        print(f"   n = {n:>5}  ->  t(n) = {ops} operation (always 1)")

    print("\n3. SIMPLE ADDITION - t(n) = 1 = O(1)")
    print("-" * 40)
    for n in sizes:
        _, ops = simple_addition(n, n)
        print(f"   n = {n:>5}  ->  t(n) = {ops} operation (always 1)")

    # -----------------------------------------------------------
    # O(log n) - LOGARITHMIC TIME EXAMPLES
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(log n) - LOGARITHMIC TIME")
    print("=" * 60)

    print("\n4. BINARY SEARCH - t(n) = log2(n) = O(log n)")
    print("-" * 40)
    print("   Halves search space each iteration")
    for n in sizes:
        arr = list(range(n))
        target = n - 1
        _, ops = binary_search(arr, target)
        print(f"   n = {n:>5}  ->  t(n) = {ops:>2} comparisons  (log2({n}) = {math.log2(n):.1f})")

    # -----------------------------------------------------------
    # O(n log n) - LOG-LINEAR TIME EXAMPLES
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(n log n) - LOG-LINEAR TIME")
    print("=" * 60)

    print("\n5. MERGE SORT - t(n) = n * log2(n) = O(n log n)")
    print("-" * 40)
    print("   n operations per level * log2(n) levels")
    for n in sizes:
        arr = list(range(n, 0, -1))  # Reversed array
        _, ops = merge_sort(arr)
        expected = n * math.log2(n)
        print(f"   n = {n:>5}  ->  t(n) = {ops:>6}  ({n}*{math.log2(n):.0f} = {expected:.0f})")

    print("\n6. LOG-LINEAR LOOP - t(n) = n*(log2(n)+1) = O(n log n)")
    print("-" * 40)
    print("   n outer iterations * (log2(n)+1) inner iterations")
    for n in [10, 100, 500, 1000]:
        ops = log_linear_loop(n)
        log_part = math.floor(math.log2(n)) + 1
        expected = n * log_part
        print(f"   n = {n:>5}  ->  t(n) = {ops:>6}  ({n}*{log_part} = {expected})")

    print("\n7. HALVING WORK PER LEVEL - t(n) = n*(log2(n)+1) = O(n log n)")
    print("-" * 40)
    print("   n work per level * (log2(n)+1) levels")
    for n in [10, 100, 500, 1000]:
        ops = halving_work_per_level(n)
        log_part = math.floor(math.log2(n)) + 1
        expected = n * log_part
        print(f"   n = {n:>5}  ->  t(n) = {ops:>6}  ({n}*{log_part} = {expected})")

    # -----------------------------------------------------------
    # O(n) - LINEAR TIME EXAMPLES
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(n) - LINEAR TIME")
    print("=" * 60)

    print("\n8. LINEAR SEARCH (worst) - t(n) = n = O(n)")
    print("-" * 40)
    print("   n comparisons (element at last position)")
    for n in sizes:
        arr = list(range(n))
        target = n - 1  # Worst case: last element
        _, ops = linear_search(arr, target)
        print(f"   n = {n:>5}  ->  t(n) = {ops:>5}")

    print("\n9. SUM OF ELEMENTS - t(n) = 1 + 2n + 1 = 2n + 2 = O(n)")
    print("-" * 40)
    print("   init(1) + loop(2n) + return(1)")
    for n in sizes:
        arr = list(range(n))
        _, ops = sum_of_elements(arr)
        expected = 2 * n + 2
        print(f"   n = {n:>5}  ->  t(n) = {ops:>5}  (2*{n}+2 = {expected})")

    print("\n10. FIND MAXIMUM - t(n) = 1 + (n-1) = n = O(n)")
    print("-" * 40)
    print("   init(1) + comparisons(n-1)")
    for n in sizes:
        arr = list(range(n))
        _, ops = find_maximum(arr)
        print(f"   n = {n:>5}  ->  t(n) = {ops:>5}  (1+{n-1} = {n})")

    print("\n11. COUNT OCCURRENCES - t(n) = 1 + n = n + 1 = O(n)")
    print("-" * 40)
    print("   init(1) + comparisons(n)")
    for n in sizes:
        arr = [1] * n  # All same elements
        _, ops = count_occurrences(arr, 1)
        print(f"   n = {n:>5}  ->  t(n) = {ops:>5}  (1+{n} = {n+1})")

    print("\n12. CHECK IF SORTED - t(n) = n - 1 = O(n)")
    print("-" * 40)
    print("   n-1 adjacent pair comparisons")
    for n in sizes:
        arr = list(range(n))  # Already sorted
        _, ops = is_sorted(arr)
        print(f"   n = {n:>5}  ->  t(n) = {ops:>5}  ({n}-1 = {n-1})")

    print("\n13. REVERSE ARRAY - t(n) = n/2 = O(n)")
    print("-" * 40)
    print("   n/2 swaps (left and right pointers meet)")
    for n in sizes:
        arr = list(range(n))
        _, ops = reverse_array(arr)
        print(f"   n = {n:>5}  ->  t(n) = {ops:>5}  ({n}/2 = {n//2})")

    print("\n14. FACTORIAL - t(n) = n = O(n)")
    print("-" * 40)
    print("   n multiplications (1*2*3*...*n)")
    for n in [5, 10, 15, 20]:
        _, ops = factorial_iterative(n)
        print(f"   n = {n:>5}  ->  t(n) = {ops:>5}")

    # -----------------------------------------------------------
    # O(n^2) - QUADRATIC TIME EXAMPLES
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(n^2) - QUADRATIC TIME")
    print("=" * 60)

    print("\n15. NESTED LOOPS - t(n) = n * n = n^2 = O(n^2)")
    print("-" * 40)
    print("    n outer * n inner iterations")
    for n in small_sizes:
        _, ops = nested_loop_example(n)
        print(f"    n = {n:>3}  ->  t(n) = {ops:>5}  ({n}*{n} = {n**2})")

    print("\n16. BUBBLE SORT - t(n) = (n-1)+(n-2)+...+1 = n(n-1)/2 = O(n^2)")
    print("-" * 40)
    print("    Sum of arithmetic series: (n^2-n)/2")
    for n in small_sizes:
        arr = list(range(n, 0, -1))  # Worst case: reversed
        _, ops = bubble_sort(arr)
        expected = n * (n - 1) // 2
        print(f"    n = {n:>3}  ->  t(n) = {ops:>5}  ({n}*{n-1}/2 = {expected})")

    print("\n17. TRIANGULAR LOOP - t(n) = 1+2+3+...+n = n(n+1)/2 = O(n^2)")
    print("-" * 40)
    print("    Sum formula: (n^2+n)/2")
    for n in small_sizes:
        ops = triangular_loop(n)
        expected = n * (n + 1) // 2
        print(f"    n = {n:>3}  ->  t(n) = {ops:>5}  ({n}*{n+1}/2 = {expected})")

    print("\n18. PRINT ALL PAIRS - t(n) = (n-1)+(n-2)+...+1 = n(n-1)/2 = O(n^2)")
    print("-" * 40)
    print("    Unique pairs: (n^2-n)/2")
    for n in small_sizes:
        arr = list(range(n))
        _, ops = print_pairs(arr)
        expected = n * (n - 1) // 2
        print(f"    n = {n:>3}  ->  t(n) = {ops:>5}  ({n}*{n-1}/2 = {expected})")

    # -----------------------------------------------------------
    # O(n^3) - CUBIC TIME EXAMPLES
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(n^3) - CUBIC TIME")
    print("=" * 60)

    print("\n19. THREE NESTED LOOPS - t(n) = n * n * n = n^3 = O(n^3)")
    print("-" * 40)
    print("    n outer * n middle * n inner iterations")
    for n in [5, 10, 20, 30]:
        ops = three_nested_loops(n)
        print(f"    n = {n:>3}  ->  t(n) = {ops:>6}  ({n}*{n}*{n} = {n**3})")

    # -----------------------------------------------------------
    # O(2^n) - EXPONENTIAL TIME EXAMPLES
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(2^n) - EXPONENTIAL TIME")
    print("=" * 60)

    print("\n20. GENERATE ALL SUBSETS - t(n) = 2^n * (n+1) = (n+1)*2^n = O(2^n)")
    print("-" * 40)
    print("    2^n subsets, each checking n bits")
    for n in [5, 10, 15, 20]:
        arr = list(range(n))
        _, ops = generate_all_subsets(arr)
        expected = (n + 1) * (2 ** n)
        print(f"    n = {n:>2}  ->  t(n) = {ops:>8}  (({n}+1)*2^{n} = {expected})")

    print("\n21. FIBONACCI RECURSIVE - t(n) = ~2^n = O(2^n)")
    print("-" * 40)
    print("    Each call branches into 2 recursive calls")
    for n in [5, 10, 15, 20, 25]:
        _, ops = fibonacci_recursive(n)
        approx = 2 ** n
        print(f"    n = {n:>2}  ->  t(n) = {ops:>8}  (approx 2^{n} = {approx})")

    # -----------------------------------------------------------
    # O(n!) - FACTORIAL TIME EXAMPLES
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(n!) - FACTORIAL TIME (WARNING: GROWS EXTREMELY FAST!)")
    print("=" * 60)

    print("\n22. GENERATE ALL PERMUTATIONS - t(n) = ~n! * c = O(n!)")
    print("-" * 40)
    print("    n! permutations, each with constant work")
    for n in [3, 5, 7, 8]:
        arr = list(range(n))
        _, ops = generate_all_permutations(arr)
        expected = math.factorial(n)
        print(f"    n = {n}  ->  t(n) = {ops:>6}  ({n}! = {expected})")

    print("\n23. TRAVELING SALESMAN - t(n) = (n-1)!*(n+1) = O(n!)")
    print("-" * 40)
    print("    (n-1)! routes, each computing n distances + 1 comparison")
    print()

    # Create sample distance matrices for different city counts
    for n in [4, 5, 6, 7, 8]:
        # Create a simple distance matrix (symmetric)
        import random
        random.seed(42)  # For reproducibility
        distances = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dist = random.randint(10, 100)
                distances[i][j] = dist
                distances[j][i] = dist

        route, min_dist, ops = traveling_salesman_bruteforce(distances)
        perms = math.factorial(n - 1)
        print(f"    n = {n} cities  ->  t(n) = {ops:>6}  ({n-1}!*({n}+1) = {perms*(n+1)})")

    print("\n    WARNING: Factorial grows EXTREMELY fast!")
    print("    " + "-" * 40)
    for n in [5, 10, 15, 20]:
        print(f"    {n}! = {n}*{n-1}*...*1 = {math.factorial(n):,}")

    # -----------------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("SUMMARY: Complete t(n) Formulas & Growth Comparison")
    print("=" * 60)
    print("""
    Complexity   Complete t(n)              t(10)          t(20)
    -----------------------------------------------------------------
    O(1)         t(n) = 1                   1              1
    O(log n)     t(n) = log2(n)             3.3            4.3
    O(n)         t(n) = n                   10             20
    O(n)         t(n) = 2n + 2              22             42
    O(n log n)   t(n) = n * log2(n)         33             86
    O(n^2)       t(n) = n^2                 100            400
    O(n^2)       t(n) = n(n-1)/2            45             190
    O(n^3)       t(n) = n^3                 1,000          8,000
    O(2^n)       t(n) = 2^n                 1,024          1,048,576
    O(n!)        t(n) = n!                  3,628,800      2.4 * 10^18

    Why we simplify to Big-O:
    -----------------------------------------------------------------
    - t(n) = 2n + 2: at n=1000, the "+2" is only 0.2% of total
    - t(n) = n(n-1)/2: same growth as n^2, just half the constant
    - Big-O captures the DOMINANT term that matters at scale

    Key insight: Algorithm choice matters enormously at scale!

    Real-world implications:
    ---------------------------------------------------------------
    - O(n log n): Can handle millions of items (sorting)
    - O(n^2):     Slows down around 10,000+ items
    - O(2^n):     Impractical beyond ~30-40 items
    - O(n!):      Impractical beyond ~10-12 items

    This is why the Traveling Salesman Problem is so famous -
    there's no known polynomial-time solution for finding the
    optimal route! For 20 cities, brute force needs 2.4 quintillion
    operations.
    """)
