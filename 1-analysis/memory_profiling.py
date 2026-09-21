"""
Memory Profiling - Actual Memory Usage in Python

This module demonstrates how to measure actual memory consumption
using sys.getsizeof() and tracemalloc.

Key concepts:
- s(n) gives theoretical space complexity
- Actual bytes depend on data types and Python overhead
"""

import sys
import tracemalloc


# ============================================================
# BASIC MEMORY MEASUREMENT
# ============================================================

def show_basic_sizes():
    """Show memory sizes of basic Python types"""
    print("=" * 70)
    print("BASIC PYTHON TYPE SIZES")
    print("=" * 70)

    # Basic types
    print("\n1. PRIMITIVE TYPES:")
    print("-" * 50)

    items = [
        ("None", None),
        ("bool (True)", True),
        ("bool (False)", False),
        ("int (0)", 0),
        ("int (1)", 1),
        ("int (100)", 100),
        ("int (10^10)", 10**10),
        ("int (10^100)", 10**100),
        ("float (0.0)", 0.0),
        ("float (3.14159)", 3.14159),
        ("complex (1+2j)", 1+2j),
    ]

    for name, value in items:
        print(f"  {name:25} = {sys.getsizeof(value):>6} bytes")

    print("\n2. STRING SIZES:")
    print("-" * 50)

    strings = [
        ("empty string ''", ""),
        ("'a' (1 char)", "a"),
        ("'hello' (5 chars)", "hello"),
        ("'a' * 10", "a" * 10),
        ("'a' * 100", "a" * 100),
        ("'a' * 1000", "a" * 1000),
    ]

    for name, value in strings:
        print(f"  {name:25} = {sys.getsizeof(value):>6} bytes")

    print("\n  Note: String overhead ~50 bytes, then ~1 byte per char")


def show_container_sizes():
    """Show memory sizes of container types"""
    print("\n" + "=" * 70)
    print("CONTAINER TYPE SIZES")
    print("=" * 70)

    print("\n1. LIST SIZES (container only, not elements):")
    print("-" * 50)

    for n in [0, 1, 10, 100, 1000]:
        lst = list(range(n))
        size = sys.getsizeof(lst)
        print(f"  list with {n:>4} elements = {size:>6} bytes (container)")

    print("\n2. TUPLE SIZES:")
    print("-" * 50)

    for n in [0, 1, 10, 100, 1000]:
        tup = tuple(range(n))
        size = sys.getsizeof(tup)
        print(f"  tuple with {n:>4} elements = {size:>6} bytes")

    print("\n3. DICT SIZES (container only):")
    print("-" * 50)

    for n in [0, 1, 10, 100, 1000]:
        d = {i: i for i in range(n)}
        size = sys.getsizeof(d)
        print(f"  dict with {n:>4} entries = {size:>6} bytes (container)")

    print("\n4. SET SIZES:")
    print("-" * 50)

    for n in [0, 1, 10, 100, 1000]:
        s = set(range(n))
        size = sys.getsizeof(s)
        print(f"  set with {n:>4} elements = {size:>6} bytes")


# ============================================================
# DEEP MEMORY MEASUREMENT
# ============================================================

def get_deep_size(obj, seen=None):
    """
    Calculate total memory including nested objects.

    sys.getsizeof() only counts the container, not the contents!
    This function recursively counts everything.
    """
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)
    size = sys.getsizeof(obj)

    if isinstance(obj, dict):
        size += sum(get_deep_size(k, seen) + get_deep_size(v, seen)
                   for k, v in obj.items())
    elif isinstance(obj, (list, tuple, set, frozenset)):
        size += sum(get_deep_size(i, seen) for i in obj)

    return size


def show_deep_vs_shallow():
    """Compare shallow vs deep memory measurement"""
    print("\n" + "=" * 70)
    print("SHALLOW vs DEEP MEMORY MEASUREMENT")
    print("=" * 70)

    print("\n1. LIST OF INTEGERS:")
    print("-" * 50)

    for n in [10, 100, 1000]:
        lst = list(range(n))
        shallow = sys.getsizeof(lst)
        deep = get_deep_size(lst)
        print(f"  n = {n:>4}: shallow = {shallow:>6} bytes, deep = {deep:>8} bytes")

    print("\n2. LIST OF STRINGS:")
    print("-" * 50)

    for n in [10, 100, 1000]:
        lst = [f"string_{i}" for i in range(n)]
        shallow = sys.getsizeof(lst)
        deep = get_deep_size(lst)
        print(f"  n = {n:>4}: shallow = {shallow:>6} bytes, deep = {deep:>8} bytes")

    print("\n3. NESTED LISTS (2D matrix):")
    print("-" * 50)

    for n in [5, 10, 20]:
        matrix = [[i * j for j in range(n)] for i in range(n)]
        shallow = sys.getsizeof(matrix)
        deep = get_deep_size(matrix)
        print(f"  {n}x{n:>2}: shallow = {shallow:>6} bytes, deep = {deep:>8} bytes")

    print("\n  Note: shallow only counts the outer list!")


# ============================================================
# TRACEMALLOC - RUNTIME MEMORY TRACKING
# ============================================================

def demo_tracemalloc_basic():
    """Demonstrate tracemalloc for runtime memory tracking"""
    print("\n" + "=" * 70)
    print("TRACEMALLOC - Runtime Memory Tracking")
    print("=" * 70)

    print("\n1. TRACKING LIST ALLOCATION:")
    print("-" * 50)

    for n in [1000, 10000, 100000]:
        tracemalloc.start()

        # Allocate memory
        data = list(range(n))

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"  n = {n:>6}: current = {current:>10,} bytes, peak = {peak:>10,} bytes")

        del data  # Clean up

    print("\n2. TRACKING DICT ALLOCATION:")
    print("-" * 50)

    for n in [1000, 10000, 100000]:
        tracemalloc.start()

        data = {i: f"value_{i}" for i in range(n)}

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"  n = {n:>6}: current = {current:>10,} bytes, peak = {peak:>10,} bytes")

        del data


def demo_algorithm_memory():
    """Compare memory usage of different algorithms"""
    print("\n" + "=" * 70)
    print("ALGORITHM MEMORY COMPARISON")
    print("=" * 70)

    n = 10000

    print(f"\nSorting {n} integers:\n")
    print("-" * 50)

    # In-place sort (modifies original)
    tracemalloc.start()
    data1 = list(range(n, 0, -1))  # Reverse order
    data1.sort()  # In-place, O(1) extra space (theoretically)
    current1, peak1 = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # sorted() creates new list
    tracemalloc.start()
    data2 = list(range(n, 0, -1))
    result = sorted(data2)  # Creates new list, O(n) extra space
    current2, peak2 = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"  list.sort() (in-place):  peak = {peak1:>10,} bytes")
    print(f"  sorted() (new list):     peak = {peak2:>10,} bytes")
    print(f"  Difference:              {peak2 - peak1:>10,} bytes")

    del data1, data2, result


# ============================================================
# SPACE COMPLEXITY VERIFICATION
# ============================================================

def verify_space_complexity():
    """Verify theoretical space complexity with actual measurements"""
    print("\n" + "=" * 70)
    print("VERIFYING SPACE COMPLEXITY")
    print("=" * 70)

    print("\n1. O(1) - CONSTANT SPACE:")
    print("-" * 50)
    print("   Algorithm: Sum all elements (only uses accumulator)")

    for n in [100, 1000, 10000, 100000]:
        tracemalloc.start()

        # O(1) space - just counting
        data = range(n)  # range is O(1) space!
        total = 0
        for x in data:
            total += x

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"   n = {n:>6}: peak memory = {peak:>8,} bytes (should be ~constant)")

    print("\n2. O(n) - LINEAR SPACE:")
    print("-" * 50)
    print("   Algorithm: Create copy of list")

    for n in [100, 1000, 10000, 100000]:
        tracemalloc.start()

        original = list(range(n))
        copy = original.copy()  # O(n) space

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"   n = {n:>6}: peak memory = {peak:>8,} bytes (should grow ~linearly)")

        del original, copy

    print("\n3. O(n^2) - QUADRATIC SPACE:")
    print("-" * 50)
    print("   Algorithm: Create n x n matrix")

    for n in [10, 50, 100, 200]:
        tracemalloc.start()

        matrix = [[0 for _ in range(n)] for _ in range(n)]  # n^2 elements

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"   n = {n:>3}: peak memory = {peak:>10,} bytes (n^2 = {n*n})")

        del matrix


# ============================================================
# MEMORY-EFFICIENT ALTERNATIVES
# ============================================================

def demo_memory_efficient():
    """Show memory-efficient alternatives"""
    print("\n" + "=" * 70)
    print("MEMORY-EFFICIENT ALTERNATIVES")
    print("=" * 70)

    n = 1000000  # 1 million

    print(f"\n1. RANGE vs LIST for {n:,} integers:")
    print("-" * 50)

    # range is O(1) space
    r = range(n)
    print(f"   range({n:,}):      {sys.getsizeof(r):>10,} bytes  O(1)")

    # list is O(n) space
    tracemalloc.start()
    lst = list(range(n))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"   list(range({n:,})): {peak:>10,} bytes  O(n)")
    del lst

    print(f"\n2. GENERATOR vs LIST:")
    print("-" * 50)

    # Generator expression - O(1) space
    gen = (x * 2 for x in range(n))
    print(f"   generator:        {sys.getsizeof(gen):>10,} bytes  O(1)")

    # List comprehension - O(n) space
    tracemalloc.start()
    lst = [x * 2 for x in range(n)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"   list comprehension: {peak:>10,} bytes  O(n)")
    del lst, gen

    print(f"\n3. STRING CONCATENATION:")
    print("-" * 50)

    n = 10000

    # Bad: string += string (creates new string each time!)
    tracemalloc.start()
    result = ""
    for i in range(n):
        result += "a"  # O(n^2) total operations, lots of temp strings
    current_bad, peak_bad = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    del result

    # Good: join (one allocation)
    tracemalloc.start()
    result = "".join("a" for _ in range(n))  # O(n)
    current_good, peak_good = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    del result

    print(f"   += in loop:       peak = {peak_bad:>10,} bytes")
    print(f"   ''.join():        peak = {peak_good:>10,} bytes")


# ============================================================
# MEMORY SUMMARY TABLE
# ============================================================

def print_summary():
    """Print summary of memory considerations"""
    print("\n" + "=" * 70)
    print("MEMORY PROFILING SUMMARY")
    print("=" * 70)
    print("""
    Key Insights:
    ----------------------------------------------------------------
    1. sys.getsizeof() - Measures only the container, not contents
       - Use get_deep_size() for total memory including nested objects

    2. tracemalloc - Tracks memory allocation at runtime
       - Useful for comparing algorithms
       - Shows current and peak memory usage

    3. Python Overhead:
       - Empty list: ~56 bytes
       - Empty dict: ~64 bytes
       - Empty string: ~49 bytes
       - Each int: ~28 bytes (small ints are cached)

    4. Memory-Efficient Patterns:
       - Use range() instead of list(range()) when iterating
       - Use generators instead of list comprehensions
       - Use ''.join() instead of += for strings
       - Modify in-place when possible (list.sort() vs sorted())

    5. Space Complexity Verification:
       - O(1): Memory stays constant as n grows
       - O(n): Memory grows proportionally with n
       - O(n^2): Memory grows with square of n

    Common Memory Sizes:
    ----------------------------------------------------------------
    Type                    Approximate Size
    ----------------------------------------------------------------
    int (small)             28 bytes
    float                   24 bytes
    empty string            49 bytes
    empty list              56 bytes
    empty dict              64 bytes
    empty set               216 bytes

    list overhead           56 bytes + 8 bytes per element (pointers)
    dict overhead           64 bytes + ~50 bytes per key-value pair

    Note: Actual sizes vary by Python version and platform!
    """)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("MEMORY PROFILING IN PYTHON")
    print("=" * 70)

    show_basic_sizes()
    show_container_sizes()
    show_deep_vs_shallow()
    demo_tracemalloc_basic()
    demo_algorithm_memory()
    verify_space_complexity()
    demo_memory_efficient()
    print_summary()
