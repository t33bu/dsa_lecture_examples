"""
Complexity Growth Visualization

Creates graphs showing how different complexity classes grow.
Requires matplotlib: pip install matplotlib
"""

import math

try:
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("matplotlib not installed. Install with: pip install matplotlib")
    print("Falling back to text-based visualization.\n")


# ============================================================
# COMPLEXITY FUNCTIONS
# ============================================================

def constant(n):
    """O(1) - Constant"""
    return 1


def logarithmic(n):
    """O(log n) - Logarithmic"""
    return math.log2(n) if n > 0 else 0


def linear(n):
    """O(n) - Linear"""
    return n


def linearithmic(n):
    """O(n log n) - Log-linear"""
    return n * math.log2(n) if n > 0 else 0


def quadratic(n):
    """O(n^2) - Quadratic"""
    return n * n


def cubic(n):
    """O(n^3) - Cubic"""
    return n * n * n


def exponential(n):
    """O(2^n) - Exponential"""
    return 2 ** n


def factorial(n):
    """O(n!) - Factorial"""
    return math.factorial(int(n))


# ============================================================
# MATPLOTLIB VISUALIZATION
# ============================================================

def plot_common_complexities():
    """Plot O(1), O(log n), O(n), O(n log n), O(n^2)"""
    if not HAS_MATPLOTLIB:
        return

    n_values = list(range(1, 101))

    plt.figure(figsize=(12, 8))

    # Calculate values
    const_vals = [constant(n) for n in n_values]
    log_vals = [logarithmic(n) for n in n_values]
    linear_vals = [linear(n) for n in n_values]
    nlogn_vals = [linearithmic(n) for n in n_values]
    quad_vals = [quadratic(n) for n in n_values]

    # Plot
    plt.plot(n_values, const_vals, 'g-', linewidth=2, label='O(1) - Constant')
    plt.plot(n_values, log_vals, 'b-', linewidth=2, label='O(log n) - Logarithmic')
    plt.plot(n_values, linear_vals, 'c-', linewidth=2, label='O(n) - Linear')
    plt.plot(n_values, nlogn_vals, 'y-', linewidth=2, label='O(n log n) - Log-linear')
    plt.plot(n_values, quad_vals, 'r-', linewidth=2, label='O(n²) - Quadratic')

    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Operations', fontsize=12)
    plt.title('Common Time Complexities (n = 1 to 100)', fontsize=14)
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 100)
    plt.ylim(0, 10000)

    plt.tight_layout()
    plt.savefig('complexity_common.png', dpi=150)
    plt.show()
    print("Saved: complexity_common.png")


def plot_polynomial_complexities():
    """Plot O(n), O(n^2), O(n^3) to show polynomial growth"""
    if not HAS_MATPLOTLIB:
        return

    n_values = list(range(1, 51))

    plt.figure(figsize=(12, 8))

    linear_vals = [linear(n) for n in n_values]
    quad_vals = [quadratic(n) for n in n_values]
    cubic_vals = [cubic(n) for n in n_values]

    plt.plot(n_values, linear_vals, 'g-', linewidth=2, label='O(n) - Linear')
    plt.plot(n_values, quad_vals, 'b-', linewidth=2, label='O(n²) - Quadratic')
    plt.plot(n_values, cubic_vals, 'r-', linewidth=2, label='O(n³) - Cubic')

    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Operations', fontsize=12)
    plt.title('Polynomial Complexities (n = 1 to 50)', fontsize=14)
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('complexity_polynomial.png', dpi=150)
    plt.show()
    print("Saved: complexity_polynomial.png")


def plot_exponential_factorial():
    """Plot O(2^n) and O(n!) to show explosive growth"""
    if not HAS_MATPLOTLIB:
        return

    n_values = list(range(1, 13))  # Only up to 12!

    plt.figure(figsize=(12, 8))

    quad_vals = [quadratic(n) for n in n_values]
    exp_vals = [exponential(n) for n in n_values]
    fact_vals = [factorial(n) for n in n_values]

    plt.plot(n_values, quad_vals, 'g-', linewidth=2, marker='o', label='O(n²) - Quadratic')
    plt.plot(n_values, exp_vals, 'b-', linewidth=2, marker='s', label='O(2ⁿ) - Exponential')
    plt.plot(n_values, fact_vals, 'r-', linewidth=2, marker='^', label='O(n!) - Factorial')

    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Operations (log scale)', fontsize=12)
    plt.title('Exponential & Factorial Growth (n = 1 to 12)', fontsize=14)
    plt.legend(loc='upper left', fontsize=10)
    plt.yscale('log')  # Log scale to see all curves
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('complexity_exponential.png', dpi=150)
    plt.show()
    print("Saved: complexity_exponential.png")


def plot_comparison_small():
    """Compare all complexities for small n"""
    if not HAS_MATPLOTLIB:
        return

    n_values = list(range(1, 21))

    plt.figure(figsize=(14, 10))

    # Calculate all values
    data = {
        'O(1)': [1 for _ in n_values],
        'O(log n)': [logarithmic(n) for n in n_values],
        'O(n)': [linear(n) for n in n_values],
        'O(n log n)': [linearithmic(n) for n in n_values],
        'O(n²)': [quadratic(n) for n in n_values],
        'O(2ⁿ)': [min(exponential(n), 1e6) for n in n_values],
    }

    colors = ['green', 'blue', 'cyan', 'yellow', 'orange', 'red']

    for (label, values), color in zip(data.items(), colors):
        plt.plot(n_values, values, linewidth=2, marker='o', markersize=4,
                 label=label, color=color)

    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Operations', fontsize=12)
    plt.title('All Complexity Classes Compared (n = 1 to 20)', fontsize=14)
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.yscale('log')

    plt.tight_layout()
    plt.savefig('complexity_comparison.png', dpi=150)
    plt.show()
    print("Saved: complexity_comparison.png")


def plot_sorting_algorithms():
    """Compare sorting algorithm complexities"""
    if not HAS_MATPLOTLIB:
        return

    n_values = list(range(1, 101))

    plt.figure(figsize=(12, 8))

    # Sorting complexities
    bubble_worst = [n * n for n in n_values]  # O(n^2)
    bubble_best = [n for n in n_values]  # O(n) with early exit
    merge = [n * math.log2(n) if n > 0 else 0 for n in n_values]  # O(n log n)
    quick_avg = [n * math.log2(n) if n > 0 else 0 for n in n_values]  # O(n log n)
    quick_worst = [n * n for n in n_values]  # O(n^2)

    plt.plot(n_values, bubble_best, 'g--', linewidth=2, label='Bubble Sort (best) - O(n)')
    plt.plot(n_values, merge, 'b-', linewidth=2, label='Merge Sort - O(n log n)')
    plt.plot(n_values, quick_avg, 'c-', linewidth=2, label='Quick Sort (avg) - O(n log n)')
    plt.plot(n_values, bubble_worst, 'r-', linewidth=2, label='Bubble Sort (worst) - O(n²)')
    plt.plot(n_values, quick_worst, 'm--', linewidth=2, label='Quick Sort (worst) - O(n²)')

    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Operations', fontsize=12)
    plt.title('Sorting Algorithm Complexities', fontsize=14)
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 100)
    plt.ylim(0, 5000)

    plt.tight_layout()
    plt.savefig('complexity_sorting.png', dpi=150)
    plt.show()
    print("Saved: complexity_sorting.png")


# ============================================================
# TEXT-BASED VISUALIZATION (Fallback)
# ============================================================

def text_visualization():
    """ASCII art visualization when matplotlib is not available"""
    print("=" * 70)
    print("TEXT-BASED COMPLEXITY VISUALIZATION")
    print("=" * 70)

    print("\n1. COMPLEXITY VALUES AT DIFFERENT n:")
    print("-" * 70)
    print(f"{'n':>6} | {'O(1)':>8} | {'O(log n)':>8} | {'O(n)':>8} | {'O(n log n)':>10} | {'O(n²)':>10}")
    print("-" * 70)

    for n in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        c = constant(n)
        log = logarithmic(n)
        lin = linear(n)
        nlogn = linearithmic(n)
        quad = quadratic(n)
        print(f"{n:>6} | {c:>8.0f} | {log:>8.1f} | {lin:>8} | {nlogn:>10.0f} | {quad:>10}")

    print("\n2. GROWTH VISUALIZATION (n = 1 to 50):")
    print("-" * 70)

    # ASCII bar chart
    max_width = 50
    complexities = [
        ("O(1)", 1, "█"),
        ("O(log n)", math.log2(50), "█"),
        ("O(n)", 50, "█"),
        ("O(n log n)", 50 * math.log2(50), "█"),
        ("O(n²)", 2500, "█"),
    ]

    max_val = max(c[1] for c in complexities)

    for name, value, char in complexities:
        bar_len = int((value / max_val) * max_width)
        bar = char * bar_len
        print(f"{name:>12}: {bar} ({value:.0f})")

    print("\n3. EXPONENTIAL/FACTORIAL GROWTH:")
    print("-" * 70)
    print(f"{'n':>4} | {'O(n²)':>12} | {'O(2^n)':>15} | {'O(n!)':>20}")
    print("-" * 70)

    for n in range(1, 13):
        q = quadratic(n)
        e = exponential(n)
        f = factorial(n)
        print(f"{n:>4} | {q:>12} | {e:>15} | {f:>20,}")

    print("\n4. WHY O(n!) IS IMPRACTICAL:")
    print("-" * 70)
    print("If each operation takes 1 microsecond:")
    print()

    times = [
        (10, factorial(10), "microseconds"),
        (12, factorial(12), "microseconds"),
        (15, factorial(15), "microseconds"),
        (20, factorial(20), "microseconds"),
    ]

    for n, ops, _ in times:
        if ops < 1000:
            time_str = f"{ops} microseconds"
        elif ops < 1000000:
            time_str = f"{ops/1000:.1f} milliseconds"
        elif ops < 1000000000:
            time_str = f"{ops/1000000:.1f} seconds"
        elif ops < 60 * 1000000000:
            time_str = f"{ops/1000000000:.1f} seconds"
        elif ops < 3600 * 1000000000:
            time_str = f"{ops/(60*1000000000):.1f} minutes"
        elif ops < 86400 * 1000000000:
            time_str = f"{ops/(3600*1000000000):.1f} hours"
        elif ops < 365 * 86400 * 1000000000:
            time_str = f"{ops/(86400*1000000000):.1f} days"
        else:
            time_str = f"{ops/(365*86400*1000000000):.1e} years"

        print(f"  n = {n:>2}: {n}! = {ops:>25,} operations = {time_str}")


def create_comparison_table():
    """Create a detailed comparison table"""
    print("\n" + "=" * 70)
    print("COMPLEXITY COMPARISON TABLE")
    print("=" * 70)

    print("""
    How long to process n items? (assuming 1 billion ops/second)

    n        O(log n)    O(n)       O(n log n)    O(n²)        O(2^n)
    -----------------------------------------------------------------------
    10       3 ns        10 ns      33 ns         100 ns       1 μs
    100      7 ns        100 ns     664 ns        10 μs        10^17 years
    1,000    10 ns       1 μs       10 μs         1 ms         ∞
    10,000   13 ns       10 μs      133 μs        100 ms       ∞
    100,000  17 ns       100 μs     1.7 ms        10 sec       ∞
    1M       20 ns       1 ms       20 ms         17 min       ∞

    Legend: ns=nanosecond, μs=microsecond, ms=millisecond, ∞=impractical

    Key Takeaways:
    -----------------------------------------------------------------------
    1. O(log n) barely grows - excellent for any size
    2. O(n) scales linearly - good for most applications
    3. O(n log n) - standard for sorting, handles millions
    4. O(n²) - starts struggling at 10,000+ items
    5. O(2^n) - impractical beyond ~30 items
    6. O(n!) - impractical beyond ~12 items
    """)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("COMPLEXITY GROWTH VISUALIZATION")
    print("=" * 70)

    if HAS_MATPLOTLIB:
        print("\nGenerating graphs with matplotlib...")
        print("Each graph will be displayed and saved as PNG.\n")

        plot_common_complexities()
        plot_polynomial_complexities()
        plot_exponential_factorial()
        plot_comparison_small()
        plot_sorting_algorithms()

        print("\nAll graphs saved!")
    else:
        text_visualization()

    create_comparison_table()
