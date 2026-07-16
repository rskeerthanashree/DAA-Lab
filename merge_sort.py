import random
import time


def merge(left_part, right_part):
    merged = []
    left = 0
    right = 0

    while left < len(left_part) and right < len(right_part):
        if left_part[left] <= right_part[right]:
            merged.append(left_part[left])
            left += 1
        else:
            merged.append(right_part[right])
            right += 1

    merged.extend(left_part[left:])
    merged.extend(right_part[right:])

    return merged


def merge_sort(numbers):

    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])

    return merge(left_half, right_half)


# ---------------- Main Program ---------------- #

sample = [42, 18, 73, 5, 91, 26, 14, 60]

print("Original Array")
print(sample)

sorted_array = merge_sort(sample)

print("\nSorted Array")
print(sorted_array)


# Performance Analysis

print("\nPerformance Analysis")
print("-" * 45)
print(f"{'Size':<10}{'Time (ms)':>15}")
print("-" * 45)

for size in [1000, 5000, 10000, 50000]:

    values = random.sample(range(size * 10), size)

    start = time.perf_counter()

    merge_sort(values)

    elapsed = (time.perf_counter() - start) * 1000

    print(f"{size:<10}{elapsed:>15.3f}")