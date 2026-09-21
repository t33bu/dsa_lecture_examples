"""
Space Complexity Analysis using s(n)

s(n) represents the memory/space needed to run an algorithm
as a function of input size n.

Space complexity includes:
1. Input space - memory for input data
2. Auxiliary space - extra memory used by the algorithm

We typically focus on AUXILIARY space (extra space beyond input).
"""

import sys


# ============================================================
# O(1) - CONSTANT SPACE
# ============================================================

def find_max_constant_space(arr):
    """
    Find maximum element - Constant Space

    s(n) Analysis - counting variables:
    - max_val: 1 variable
    - i (loop): 1 variable
    - No extra arrays created

    s(n) = 1 + 1 = 2 = O(1) - Constant
    (Space doesn't grow with input size)
    """
    max_val = arr[0]      # 1 variable
    for i in range(len(arr)):  # 1 loop variable
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


def sum_elements_constant_space(arr):
    """
    Sum all elements - Constant Space

    s(n) Analysis - counting variables:
    - total: 1 variable
    - num (loop): 1 variable

    s(n) = 1 + 1 = 2 = O(1) - Constant
    """
    total = 0
    for num in arr:
        total += num
    return total


def swap_variables(a, b):
    """
    Swap two variables - Constant Space

    s(n) Analysis - counting variables:
    - temp: 1 variable
    - a, b already exist (input)

    s(n) = 1 = O(1) - Constant
    """
    temp = a
    a = b
    b = temp
    return a, b


def reverse_in_place(arr):
    """
    Reverse array in place - Constant Space

    s(n) Analysis - counting variables:
    - left: 1 variable
    - right: 1 variable
    - No new array created - modifies original

    s(n) = 1 + 1 = 2 = O(1) - Constant
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def bubble_sort_in_place(arr):
    """
    Bubble sort in place - Constant Space

    s(n) Analysis - counting variables:
    - n: 1 variable
    - i (outer loop): 1 variable
    - j (inner loop): 1 variable
    - Swaps done in place, no extra array

    s(n) = 1 + 1 + 1 = 3 = O(1) - Constant
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# ============================================================
# O(n) - LINEAR SPACE
# ============================================================

def create_copy(arr):
    """
    Create a copy of array - Linear Space

    s(n) Analysis - counting elements:
    - copy array: n elements
    - item (loop variable): 1 variable

    s(n) = n + 1 = O(n) - Linear
    """
    copy = []
    for item in arr:
        copy.append(item)
    return copy


def reverse_new_array(arr):
    """
    Reverse array into new array - Linear Space

    s(n) Analysis - counting elements:
    - reversed_arr: n elements
    - i (loop variable): 1 variable

    s(n) = n + 1 = O(n) - Linear
    """
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr


def merge_sort_space(arr):
    """
    Merge sort - Linear Space

    s(n) Analysis - counting elements:
    - Temporary arrays during merging: n elements total
    - Recursion call stack depth: log n frames
    - Each frame stores: ~4 variables

    s(n) = n + 4*log(n) = O(n) - Linear
    (n dominates as n grows large)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_space(arr[:mid])   # Creates new array
    right = merge_sort_space(arr[mid:])  # Creates new array

    return _merge_arrays(left, right)


def _merge_arrays(left, right):
    """Helper: merge two sorted arrays"""
    result = []  # Extra space
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def count_frequency(arr):
    """
    Count frequency of each element - Linear Space

    s(n) Analysis - counting elements:
    - freq dictionary: up to n key-value pairs (worst case: all unique)
    - item (loop variable): 1 variable

    s(n) = n + 1 = O(n) - Linear (worst case)
    Best case (all same): s(n) = 1 + 1 = 2 = O(1)
    """
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq


def fibonacci_with_memo(n):
    """
    Fibonacci with memoization - Linear Space

    s(n) Analysis - counting elements:
    - memo dictionary: n+1 entries (fib(0) to fib(n))
    - Recursion stack: up to n frames (before memoization kicks in)
    - Each frame: ~2 variables

    s(n) = (n + 1) + 2 = n + 3 = O(n) - Linear
    """
    memo = {0: 0, 1: 1}

    def fib(k):
        if k not in memo:
            memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    return fib(n), memo


# ============================================================
# O(log n) - LOGARITHMIC SPACE
# ============================================================

def binary_search_recursive(arr, target, left=None, right=None):
    """
    Binary search recursive - Logarithmic Space

    s(n) Analysis - counting stack frames:
    - Search space halves each time -> log n recursive calls
    - Each call stores on stack: arr ref, target, left, right, mid
    - Variables per frame: 5

    s(n) = 5 * log(n) = O(log n) - Logarithmic
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_iterative(arr, target):
    """
    Binary search iterative - Constant Space

    s(n) Analysis - counting variables:
    - left: 1 variable
    - right: 1 variable
    - mid: 1 variable
    - No recursion = no call stack growth

    s(n) = 1 + 1 + 1 = 3 = O(1) - Constant
    (Compare to recursive version which is O(log n))
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ============================================================
# O(n^2) - QUADRATIC SPACE
# ============================================================

def create_2d_matrix(n):
    """
    Create n x n matrix - Quadratic Space

    s(n) Analysis - counting elements:
    - matrix: n rows
    - Each row: n elements
    - Loop variables (i, j): 2 variables

    s(n) = n * n + 2 = n^2 + 2 = O(n^2) - Quadratic
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix


def create_adjacency_matrix(n):
    """
    Create adjacency matrix for graph - Quadratic Space

    s(n) Analysis - counting elements:
    - adj_matrix: n rows * n columns
    - Represents connections between n nodes

    s(n) = n * n = n^2 = O(n^2) - Quadratic
    """
    adj_matrix = [[0] * n for _ in range(n)]
    return adj_matrix


def all_pairs_distances(arr):
    """
    Store distances between all pairs - Quadratic Space

    s(n) Analysis - counting elements:
    - distances matrix: n rows * n columns = n^2 elements
    - Loop variables (i, j): 2 variables

    s(n) = n^2 + 2 = O(n^2) - Quadratic
    """
    n = len(arr)
    distances = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            distances[i][j] = abs(arr[i] - arr[j])

    return distances


# ============================================================
# O(n^3) - CUBIC SPACE
# ============================================================

def create_3d_matrix(n):
    """
    Create n x n x n 3D matrix - Cubic Space

    s(n) Analysis - counting elements:
    - matrix_3d: n layers
    - Each layer: n rows
    - Each row: n elements
    - Loop variables (i, j, k): 3 variables

    s(n) = n * n * n + 3 = n^3 + 3 = O(n^3) - Cubic

    Real-world example: 3D voxel grid for games/medical imaging
    """
    matrix_3d = []
    for i in range(n):
        layer = []
        for j in range(n):
            row = []
            for k in range(n):
                row.append(0)
            layer.append(row)
        matrix_3d.append(layer)
    return matrix_3d


def all_triplet_sums(arr):
    """
    Store sums of all possible triplets - Cubic Space

    s(n) Analysis - counting elements:
    - triplet_sums: n * n * n = n^3 elements
    - Loop variables (i, j, k): 3 variables
    - n variable: 1 variable

    s(n) = n^3 + 3 + 1 = n^3 + 4 = O(n^3) - Cubic
    """
    n = len(arr)
    triplet_sums = [[[0] * n for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                triplet_sums[i][j][k] = arr[i] + arr[j] + arr[k]

    return triplet_sums


def floyd_warshall_all_paths(n):
    """
    Store shortest paths through each intermediate node - Cubic Space

    s(n) Analysis - counting elements:
    - all_distances: (n+1) matrices, each n x n
    - Total: (n+1) * n * n = n^3 + n^2 elements
    - Loop variables + temp arrays: ~10 variables

    s(n) = n^3 + n^2 + 10 = O(n^3) - Cubic

    Note: Optimized version uses O(n^2) by overwriting,
    but storing all steps requires O(n^3)
    """
    # Initialize: all_distances[k][i][j] = shortest path from i to j
    # using only nodes 0..k as intermediates
    INF = float('inf')

    # Store distance matrix at each step k
    all_distances = []

    # Initial distances (direct edges only)
    import random
    random.seed(42)
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j in range(n):
            if i != j and random.random() < 0.3:  # 30% chance of edge
                dist[i][j] = random.randint(1, 10)

    all_distances.append([row[:] for row in dist])  # Store copy

    # Floyd-Warshall: store matrix after each k
    for k in range(n):
        new_dist = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        dist = new_dist
        all_distances.append([row[:] for row in dist])  # Store copy

    return all_distances


def voxel_grid_3d(n):
    """
    3D Voxel Grid - Cubic Space

    s(n) Analysis - counting elements:
    - voxels: n layers * n rows * n columns = n^3 voxels
    - Loop variables (x, y, z): 3 variables

    s(n) = n^3 + 3 = O(n^3) - Cubic

    Example: 100x100x100 CT scan = 1,000,000 voxels
    Real-world: Medical imaging, 3D games, scientific simulations
    """
    # Each voxel stores intensity value (0-255 for medical imaging)
    voxels = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

    # Fill with sample data (gradient)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                # Simple gradient based on position
                voxels[x][y][z] = (x + y + z) % 256

    return voxels


# ============================================================
# DEMONSTRATION
# ============================================================

def measure_size(obj, name="object"):
    """Estimate memory size of an object"""
    size = sys.getsizeof(obj)
    if isinstance(obj, list):
        size += sum(sys.getsizeof(item) for item in obj)
        if obj and isinstance(obj[0], list):  # 2D list
            for row in obj:
                size += sum(sys.getsizeof(item) for item in row)
    elif isinstance(obj, dict):
        size += sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in obj.items())
    return size


if __name__ == "__main__":
    print("=" * 60)
    print("SPACE COMPLEXITY ANALYSIS: s(n) Examples")
    print("=" * 60)

    sizes = [10, 100, 1000]

    # -----------------------------------------------------------
    # O(1) - CONSTANT SPACE
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(1) - CONSTANT SPACE")
    print("=" * 60)

    print("\n1. FIND MAX IN PLACE - s(n) = 1 + 1 = 2 = O(1)")
    print("-" * 40)
    print("   Variables: max_val(1) + i(1) = 2")
    for n in sizes:
        arr = list(range(n))
        result = find_max_constant_space(arr)
        print(f"   n = {n:>5}  ->  s(n) = 2 (constant, doesn't grow)")

    print("\n2. SUM ELEMENTS - s(n) = 1 + 1 = 2 = O(1)")
    print("-" * 40)
    print("   Variables: total(1) + num(1) = 2")
    for n in sizes:
        arr = list(range(n))
        result = sum_elements_constant_space(arr)
        print(f"   n = {n:>5}  ->  s(n) = 2 (constant)")

    print("\n3. REVERSE IN PLACE - s(n) = 1 + 1 = 2 = O(1)")
    print("-" * 40)
    print("   Variables: left(1) + right(1) = 2")
    for n in sizes:
        arr = list(range(n))
        reverse_in_place(arr)
        print(f"   n = {n:>5}  ->  s(n) = 2 (constant)")

    print("\n4. BUBBLE SORT IN PLACE - s(n) = 1 + 1 + 1 = 3 = O(1)")
    print("-" * 40)
    print("   Variables: n(1) + i(1) + j(1) = 3")
    for n in [10, 50, 100]:
        arr = list(range(n, 0, -1))
        bubble_sort_in_place(arr)
        print(f"   n = {n:>5}  ->  s(n) = 3 (constant)")

    # -----------------------------------------------------------
    # O(log n) - LOGARITHMIC SPACE
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(log n) - LOGARITHMIC SPACE")
    print("=" * 60)

    print("\n5. BINARY SEARCH RECURSIVE - s(n) = 5 * log(n) = O(log n)")
    print("-" * 40)
    print("   Stack frames: log(n), each with 5 variables")
    import math
    for n in sizes:
        arr = list(range(n))
        result = binary_search_recursive(arr, n - 1)
        stack_depth = math.ceil(math.log2(n + 1))
        total_space = 5 * stack_depth
        print(f"   n = {n:>5}  ->  s(n) = 5 * {stack_depth} = {total_space} vars")

    print("\n   Compare: BINARY SEARCH ITERATIVE - s(n) = 1+1+1 = 3 = O(1)")
    print("-" * 40)
    print("   Variables: left(1) + right(1) + mid(1) = 3")
    for n in sizes:
        arr = list(range(n))
        result = binary_search_iterative(arr, n - 1)
        print(f"   n = {n:>5}  ->  s(n) = 3 (constant, no recursion)")

    # -----------------------------------------------------------
    # O(n) - LINEAR SPACE
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(n) - LINEAR SPACE")
    print("=" * 60)

    print("\n6. CREATE COPY - s(n) = n + 1 = O(n)")
    print("-" * 40)
    print("   Elements: copy array(n) + loop var(1)")
    for n in sizes:
        arr = list(range(n))
        copy = create_copy(arr)
        print(f"   n = {n:>5}  ->  s(n) = {n} + 1 = {n + 1}")

    print("\n7. REVERSE TO NEW ARRAY - s(n) = n + 1 = O(n)")
    print("-" * 40)
    print("   Elements: reversed array(n) + loop var(1)")
    for n in sizes:
        arr = list(range(n))
        rev = reverse_new_array(arr)
        print(f"   n = {n:>5}  ->  s(n) = {n} + 1 = {n + 1}")

    print("\n8. COUNT FREQUENCY (HashMap) - s(n) = n + 1 = O(n)")
    print("-" * 40)
    print("   Elements: dictionary(n keys) + loop var(1)")
    for n in sizes:
        arr = list(range(n))  # All unique
        freq = count_frequency(arr)
        print(f"   n = {n:>5}  ->  s(n) = {len(freq)} + 1 = {len(freq) + 1}")

    print("\n9. FIBONACCI WITH MEMOIZATION - s(n) = (n+1) + 2 = n + 3 = O(n)")
    print("-" * 40)
    print("   Elements: memo dict(n+1 entries) + recursion vars(2)")
    for n in [10, 20, 30]:
        result, memo = fibonacci_with_memo(n)
        print(f"   n = {n:>5}  ->  s(n) = {len(memo)} + 2 = {len(memo) + 2}")

    # -----------------------------------------------------------
    # O(n^2) - QUADRATIC SPACE
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(n^2) - QUADRATIC SPACE")
    print("=" * 60)

    print("\n10. CREATE n x n MATRIX - s(n) = n*n + 2 = n^2 + 2 = O(n^2)")
    print("-" * 40)
    print("    Elements: matrix(n*n) + loop vars(2)")
    for n in [10, 50, 100]:
        matrix = create_2d_matrix(n)
        total_elements = n * n
        print(f"    n = {n:>3}  ->  s(n) = {n}*{n} + 2 = {total_elements + 2}")

    print("\n11. ADJACENCY MATRIX (Graph) - s(n) = n * n = n^2 = O(n^2)")
    print("-" * 40)
    print("    Elements: n rows * n columns")
    for n in [10, 50, 100]:
        adj = create_adjacency_matrix(n)
        total_elements = n * n
        print(f"    n = {n:>3} nodes  ->  s(n) = {n} * {n} = {total_elements}")

    print("\n12. ALL PAIRS DISTANCES - s(n) = n^2 + 2 = O(n^2)")
    print("-" * 40)
    print("    Elements: matrix(n^2) + loop vars i,j(2)")
    for n in [10, 50, 100]:
        arr = list(range(n))
        distances = all_pairs_distances(arr)
        total_pairs = n * n
        print(f"    n = {n:>3}  ->  s(n) = {n}^2 + 2 = {total_pairs + 2}")

    # -----------------------------------------------------------
    # O(n^3) - CUBIC SPACE
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("O(n^3) - CUBIC SPACE")
    print("=" * 60)

    print("\n13. CREATE 3D MATRIX - s(n) = n*n*n + 3 = n^3 + 3 = O(n^3)")
    print("-" * 40)
    print("    Elements: matrix(n*n*n) + loop vars i,j,k(3)")
    for n in [5, 10, 20]:
        matrix_3d = create_3d_matrix(n)
        total_elements = n * n * n
        print(f"    n = {n:>2}  ->  s(n) = {n}*{n}*{n} + 3 = {total_elements + 3}")

    print("\n14. ALL TRIPLET SUMS - s(n) = n^3 + 4 = O(n^3)")
    print("-" * 40)
    print("    Elements: triplets(n^3) + vars n,i,j,k(4)")
    for n in [5, 10, 15]:
        arr = list(range(n))
        triplets = all_triplet_sums(arr)
        total_triplets = n * n * n
        print(f"    n = {n:>2}  ->  s(n) = {n}^3 + 4 = {total_triplets + 4}")

    print("\n15. 3D VOXEL GRID - s(n) = n^3 + 3 = O(n^3)")
    print("-" * 40)
    print("    Elements: voxels(n^3) + loop vars x,y,z(3)")
    for n in [10, 20, 50]:
        voxels = voxel_grid_3d(n)
        total_voxels = n * n * n
        print(f"    n = {n:>2}  ->  s(n) = {n}^3 + 3 = {total_voxels + 3}")

    print("\n16. FLOYD-WARSHALL ALL STEPS - s(n) = n^3 + n^2 + 10 = O(n^3)")
    print("-" * 40)
    print("    Elements: (n+1) matrices of n^2 + temp vars(~10)")
    for n in [5, 10, 15]:
        all_dist = floyd_warshall_all_paths(n)
        total_storage = len(all_dist) * n * n
        print(f"    n = {n:>2}  ->  s(n) = {len(all_dist)}*{n}^2 + 10 = {total_storage + 10}")

    print("\n    WARNING: Cubic space grows VERY fast!")
    print("    " + "-" * 40)
    for n in [10, 50, 100]:
        print(f"    n = {n:>3}  ->  n^3 + 3 = {n**3} + 3 = {n**3 + 3:>12,}")

    # -----------------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------------
    print("\n" + "=" * 60)
    print("SUMMARY: Space Complexity Comparison")
    print("=" * 60)
    print("""
    Complexity   Complete s(n)            n=10           n=100
    ----------------------------------------------------------------
    O(1)         s(n) = 2                 2              2
    O(log n)     s(n) = 5*log(n)          5*4 = 20       5*7 = 35
    O(n)         s(n) = n + 1             10 + 1 = 11    100 + 1 = 101
    O(n^2)       s(n) = n^2 + 2           100 + 2        10,000 + 2
    O(n^3)       s(n) = n^3 + 3           1,000 + 3      1,000,000 + 3

    Key insight: Constants become negligible as n grows!

    Why we simplify:
    -------------------------------------------------------
    - n=100: n^2 + 2 = 10,002  (the +2 is 0.02% of total)
    - n=1000: n^2 + 2 = 1,000,002  (the +2 is 0.0002%)
    - Big-O focuses on the DOMINANT term that matters at scale

    Practical implications:
    -------------------------------------------------------
    - O(1):    Can process ANY size data (if you have time)
    - O(n):    Limited by available RAM
    - O(n^2):  100 items = ~10,000 cells
               1000 items = ~1 million cells
    - O(n^3):  100 items = 1 million cells
               1000 items = 1 BILLION cells (will crash!)

    Real-world O(n^3) examples:
    -------------------------------------------------------
    - 3D video games: voxel worlds (Minecraft uses chunks)
    - Medical imaging: CT scans (512x512x100 = 26 million voxels)
    - Scientific simulations: 3D fluid dynamics
    - Graph algorithms: storing all intermediate states

    Trade-off: O(n^3) algorithms often need optimization
    or chunking to handle real-world data sizes.
    """)
