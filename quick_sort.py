import random
import time


def partition(values, start, end):
    pivot = values[end]
    smaller_index = start - 1

    for current in range(start, end):
        if values[current] <= pivot:
            smaller_index += 1
            values[smaller_index], values[current] = values[current], values[smaller_index]

    values[smaller_index + 1], values[end] = values[end], values[smaller_index + 1]
    return smaller_index + 1


def quick_sort(values, start, end):
    if start < end:
        pivot_index = partition(values, start, end)

        quick_sort(values, start, pivot_index - 1)
        quick_sort(values, pivot_index + 1, end)


# ---------------- Main Program ---------------- #

sample = [42, 18, 73, 5, 91, 26, 14, 60]

print("Original Array")
print(sample)

quick_sort(sample, 0, len(sample) - 1)

print("\nSorted Array")
print(sample)


print("\nPerformance Analysis")
print("-" * 45)
print(f"{'Size':<10}{'Time (ms)':>15}")
print("-" * 45)

for size in [1000, 5000, 10000, 50000]:

    numbers = random.sample(range(size * 10), size)

    start_time = time.perf_counter()

    quick_sort(numbers, 0, len(numbers) - 1)

    elapsed = (time.perf_counter() - start_time) * 1000

    print(f"{size:<10}{elapsed:>15.3f}")