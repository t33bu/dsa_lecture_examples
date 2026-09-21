"""
Best, Average, and Worst Case Analysis

For the same algorithm, the number of operations can vary depending on the input.
- Best case:    Minimum operations (lucky input)
- Average case: Expected operations (typical input)
- Worst case:   Maximum operations (unlucky input)

We usually focus on WORST CASE because:
1. It gives us a guarantee
2. It's often easier to analyze
3. It's what matters in critical systems
"""

import random
import time


# ============================================================
# LINEAR SEARCH - Classic Best/Average/Worst Example
# ============================================================

def linear_search_with_tracking(arr, target):
    """
    Linear Search with operation counting

    Best case:    t(n) = 1       - Target at first position
    Average case: t(n) = n/2     - Target at middle (on average)
    Worst case:   t(n) = n       - Target at last position or not found

    All cases: O(n) - but constants differ significantly!
    """
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons, "found"

    return -1, comparisons, "not found"


def demo_linear_search_cases():
    """Demonstrate best, average, worst cases for linear search"""
    print("\n" + "=" * 70)
    print("LINEAR SEARCH - Best/Average/Worst Case Analysis")
    print("=" * 70)

    sizes = [100, 1000, 10000]

    for n in sizes:
        arr = list(range(n))

        # Best case: target at position 0
        _, best_ops, _ = linear_search_with_tracking(arr, 0)

        # Worst case: target at last position
        _, worst_ops, _ = linear_search_with_tracking(arr, n - 1)

        # Worst case: target not found
        _, not_found_ops, _ = linear_search_with_tracking(arr, -1)

        # Average case: run many searches, compute average
        total_ops = 0
        trials = 100
        for _ in range(trials):
            target = random.randint(0, n - 1)
            _, ops, _ = linear_search_with_tracking(arr, target)
            total_ops += ops
        avg_ops = total_ops / trials

        print(f"\n  n = {n:>5}")
        print(f"  " + "-" * 50)
        print(f"  Best case (target=0):      t(n) = {best_ops:>6}  (= 1)")
        print(f"  Average case (random):     t(n) = {avg_ops:>6.0f}  (≈ n/2 = {n/2:.0f})")
        print(f"  Worst case (target=n-1):   t(n) = {worst_ops:>6}  (= n)")
        print(f"  Worst case (not found):    t(n) = {not_found_ops:>6}  (= n)")


# ============================================================
# BUBBLE SORT - Best/Worst Case Differ Significantly
# ============================================================

def bubble_sort_with_tracking(arr):
    """
    Bubble Sort with operation counting

    Best case:    t(n) = n-1         - Already sorted (with early exit)
    Average case: t(n) = n^2/2       - Random order
    Worst case:   t(n) = n(n-1)/2    - Reverse sorted

    Optimized version can detect if sorted and exit early.
    """
    result = arr.copy()
    n = len(result)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swaps += 1
                swapped = True

        # Early exit if no swaps (array is sorted)
        if not swapped:
            break

    return result, comparisons, swaps


def demo_bubble_sort_cases():
    """Demonstrate best, average, worst cases for bubble sort"""
    print("\n" + "=" * 70)
    print("BUBBLE SORT - Best/Average/Worst Case Analysis")
    print("=" * 70)

    sizes = [50, 100, 200]

    for n in sizes:
        # Best case: already sorted
        sorted_arr = list(range(n))
        _, best_comps, best_swaps = bubble_sort_with_tracking(sorted_arr)

        # Worst case: reverse sorted
        reverse_arr = list(range(n, 0, -1))
        _, worst_comps, worst_swaps = bubble_sort_with_tracking(reverse_arr)

        # Average case: random order
        random_arr = list(range(n))
        random.shuffle(random_arr)
        _, avg_comps, avg_swaps = bubble_sort_with_tracking(random_arr)

        expected_worst = n * (n - 1) // 2

        print(f"\n  n = {n}")
        print(f"  " + "-" * 60)
        print(f"  Best (sorted):    comparisons = {best_comps:>6}, swaps = {best_swaps:>6}")
        print(f"  Average (random): comparisons = {avg_comps:>6}, swaps = {avg_swaps:>6}")
        print(f"  Worst (reversed): comparisons = {worst_comps:>6}, swaps = {worst_swaps:>6}")
        print(f"  Expected worst:   n(n-1)/2 = {n}*{n-1}/2 = {expected_worst}")


# ============================================================
# QUICK SORT - Famous for Worst Case Problem
# ============================================================

def quicksort_with_tracking(arr, depth=0):
    """
    Quick Sort with operation counting

    Best case:    t(n) = n log n    - Pivot always splits evenly
    Average case: t(n) = n log n    - Random pivot selection
    Worst case:   t(n) = n^2        - Already sorted + bad pivot choice!

    The worst case is why we randomize pivot selection in practice.
    """
    global qs_comparisons, qs_max_depth

    if len(arr) <= 1:
        return arr, 0

    comparisons = 0
    qs_max_depth = max(qs_max_depth, depth)

    # Choose first element as pivot (bad choice for sorted arrays!)
    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        comparisons += 1
        qs_comparisons += 1
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    sorted_left, left_comps = quicksort_with_tracking(left, depth + 1)
    sorted_right, right_comps = quicksort_with_tracking(right, depth + 1)

    return sorted_left + [pivot] + sorted_right, comparisons + left_comps + right_comps


def quicksort_randomized(arr, depth=0):
    """Quick sort with random pivot - avoids worst case"""
    global qs_comparisons, qs_max_depth

    if len(arr) <= 1:
        return arr, 0

    comparisons = 0
    qs_max_depth = max(qs_max_depth, depth)

    # Random pivot selection - much better!
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    left = []
    right = []

    for i, x in enumerate(arr):
        if i == pivot_idx:
            continue
        comparisons += 1
        qs_comparisons += 1
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    sorted_left, left_comps = quicksort_randomized(left, depth + 1)
    sorted_right, right_comps = quicksort_randomized(right, depth + 1)

    return sorted_left + [pivot] + sorted_right, comparisons + left_comps + right_comps


# Global counters for quicksort
qs_comparisons = 0
qs_max_depth = 0


def demo_quicksort_cases():
    """Demonstrate best, average, worst cases for quicksort"""
    global qs_comparisons, qs_max_depth

    print("\n" + "=" * 70)
    print("QUICK SORT - Best/Average/Worst Case Analysis")
    print("=" * 70)
    print("\nWARNING: Naive quicksort has O(n^2) worst case on sorted input!")

    sizes = [50, 100, 200]

    for n in sizes:
        import math

        # Worst case: sorted array with first-element pivot
        qs_comparisons = 0
        qs_max_depth = 0
        sorted_arr = list(range(n))
        quicksort_with_tracking(sorted_arr.copy())
        worst_comps = qs_comparisons
        worst_depth = qs_max_depth

        # Average case: random array
        qs_comparisons = 0
        qs_max_depth = 0
        random_arr = list(range(n))
        random.shuffle(random_arr)
        quicksort_with_tracking(random_arr.copy())
        avg_comps = qs_comparisons
        avg_depth = qs_max_depth

        # With randomized pivot (always good)
        qs_comparisons = 0
        qs_max_depth = 0
        quicksort_randomized(sorted_arr.copy())
        random_pivot_comps = qs_comparisons
        random_pivot_depth = qs_max_depth

        expected_good = n * math.log2(n)
        expected_bad = n * (n - 1) // 2

        print(f"\n  n = {n}")
        print(f"  " + "-" * 60)
        print(f"  Worst (sorted, naive):     comps = {worst_comps:>6}, depth = {worst_depth}")
        print(f"  Average (random, naive):   comps = {avg_comps:>6}, depth = {avg_depth}")
        print(f"  Sorted + random pivot:     comps = {random_pivot_comps:>6}, depth = {random_pivot_depth}")
        print(f"  Expected O(n log n):       {expected_good:.0f}")
        print(f"  Expected O(n^2):           {expected_bad}")


# ============================================================
# BINARY SEARCH - Only Has One Case (Worst)
# ============================================================

def binary_search_with_tracking(arr, target):
    """
    Binary Search - All cases are O(log n)

    Best case:    t(n) = 1       - Target at middle
    Average case: t(n) = log n   - Typical search
    Worst case:   t(n) = log n   - Target at end or not found

    Binary search is special: best and worst differ by constant only!
    """
    comparisons = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, comparisons, "found at middle"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons, "not found"


def demo_binary_search_cases():
    """Demonstrate cases for binary search"""
    print("\n" + "=" * 70)
    print("BINARY SEARCH - Best/Average/Worst Case Analysis")
    print("=" * 70)
    print("\nBinary search is special: all cases are O(log n)!")

    import math

    sizes = [100, 1000, 10000, 100000]

    for n in sizes:
        arr = list(range(n))

        # Best case: target at exact middle
        mid_target = n // 2
        _, best_comps, _ = binary_search_with_tracking(arr, mid_target)

        # Worst case: target at end
        _, worst_comps, _ = binary_search_with_tracking(arr, n - 1)

        # Worst case: not found
        _, not_found_comps, _ = binary_search_with_tracking(arr, -1)

        expected = math.ceil(math.log2(n + 1))

        print(f"\n  n = {n:>6}")
        print(f"  " + "-" * 50)
        print(f"  Best (middle):      t(n) = {best_comps:>2} comparisons")
        print(f"  Worst (last):       t(n) = {worst_comps:>2} comparisons")
        print(f"  Worst (not found):  t(n) = {not_found_comps:>2} comparisons")
        print(f"  Expected log2(n):   {expected} (ceil of {math.log2(n):.1f})")


# ============================================================
# INSERTION SORT - Good Best Case
# ============================================================

def insertion_sort_with_tracking(arr):
    """
    Insertion Sort with operation counting

    Best case:    t(n) = n-1     - Already sorted (just comparisons)
    Average case: t(n) = n^2/4   - Random order
    Worst case:   t(n) = n^2/2   - Reverse sorted

    Insertion sort is GREAT for nearly-sorted data!
    """
    result = arr.copy()
    n = len(result)
    comparisons = 0
    shifts = 0

    for i in range(1, n):
        key = result[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if result[j] > key:
                result[j + 1] = result[j]
                shifts += 1
                j -= 1
            else:
                break

        result[j + 1] = key

    return result, comparisons, shifts


def demo_insertion_sort_cases():
    """Demonstrate cases for insertion sort"""
    print("\n" + "=" * 70)
    print("INSERTION SORT - Best/Average/Worst Case Analysis")
    print("=" * 70)
    print("\nInsertion sort is excellent for nearly-sorted data!")

    sizes = [50, 100, 200]

    for n in sizes:
        # Best case: already sorted
        sorted_arr = list(range(n))
        _, best_comps, best_shifts = insertion_sort_with_tracking(sorted_arr)

        # Worst case: reverse sorted
        reverse_arr = list(range(n, 0, -1))
        _, worst_comps, worst_shifts = insertion_sort_with_tracking(reverse_arr)

        # Average case: random
        random_arr = list(range(n))
        random.shuffle(random_arr)
        _, avg_comps, avg_shifts = insertion_sort_with_tracking(random_arr)

        # Nearly sorted: only a few elements out of place
        nearly_sorted = list(range(n))
        # Swap 5% of elements
        for _ in range(n // 20):
            i, j = random.randint(0, n-1), random.randint(0, n-1)
            nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
        _, nearly_comps, nearly_shifts = insertion_sort_with_tracking(nearly_sorted)

        print(f"\n  n = {n}")
        print(f"  " + "-" * 60)
        print(f"  Best (sorted):       comps = {best_comps:>6}, shifts = {best_shifts:>6}")
        print(f"  Nearly sorted (5%):  comps = {nearly_comps:>6}, shifts = {nearly_shifts:>6}")
        print(f"  Average (random):    comps = {avg_comps:>6}, shifts = {avg_shifts:>6}")
        print(f"  Worst (reversed):    comps = {worst_comps:>6}, shifts = {worst_shifts:>6}")


# ============================================================
# SUMMARY TABLE
# ============================================================

def print_summary():
    """Print summary of best/average/worst cases"""
    print("\n" + "=" * 70)
    print("SUMMARY: Best / Average / Worst Case Comparison")
    print("=" * 70)
    print("""
    Algorithm        Best Case    Average Case    Worst Case
    ----------------------------------------------------------------
    Linear Search    O(1)         O(n)            O(n)
    Binary Search    O(1)         O(log n)        O(log n)
    Bubble Sort      O(n)*        O(n^2)          O(n^2)
    Insertion Sort   O(n)         O(n^2)          O(n^2)
    Quick Sort       O(n log n)   O(n log n)      O(n^2) !!
    Merge Sort       O(n log n)   O(n log n)      O(n log n)
    Heap Sort        O(n log n)   O(n log n)      O(n log n)

    * Bubble sort O(n) best case requires early-exit optimization

    Key Insights:
    ----------------------------------------------------------------
    1. Linear vs Binary Search:
       - Linear: Best=O(1), Worst=O(n) - huge difference!
       - Binary: Best=O(1), Worst=O(log n) - small difference

    2. Quick Sort's Weakness:
       - O(n^2) worst case on sorted input with bad pivot
       - Solution: randomize pivot selection!

    3. Insertion Sort's Strength:
       - O(n) for nearly-sorted data
       - Often used as final step in hybrid sorts

    4. When to use what:
       - Nearly sorted data: Insertion Sort
       - Need guaranteed O(n log n): Merge Sort or Heap Sort
       - Average case matters most: Quick Sort (randomized)
    """)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    random.seed(42)  # For reproducibility

    demo_linear_search_cases()
    demo_binary_search_cases()
    demo_bubble_sort_cases()
    demo_insertion_sort_cases()
    demo_quicksort_cases()
    print_summary()
