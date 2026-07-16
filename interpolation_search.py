import random
import time


def interpolation_search(numbers, key):
    """Interpolation Search"""

    left = 0
    right = len(numbers) - 1
    comparisons = 0

    while left <= right and numbers[left] <= key <= numbers[right]:

        comparisons += 1

        if left == right:
            if numbers[left] == key:
                return left, comparisons
            return -1, comparisons

        position = left + (
            (key - numbers[left]) * (right - left)
        ) // (numbers[right] - numbers[left])

        if numbers[position] == key:
            return position, comparisons

        elif numbers[position] < key:
            left = position + 1

        else:
            right = position - 1

    return -1, comparisons


def binary_search(numbers, key):
    """Binary Search"""

    left = 0
    right = len(numbers) - 1
    comparisons = 0

    while left <= right:

        comparisons += 1
        middle = (left + right) // 2

        if numbers[middle] == key:
            return middle, comparisons

        elif numbers[middle] < key:
            left = middle + 1

        else:
            right = middle - 1

    return -1, comparisons


def compare_algorithms():

    dataset_sizes = [1000, 5000, 10000, 50000, 100000]

    print("\nPerformance Comparison")
    print("-" * 72)
    print(f"{'Size':<10}{'Interpolation(ms)':<20}{'Binary(ms)':<15}")
    print("-" * 72)

    for size in dataset_sizes:

        numbers = sorted(random.sample(range(size * 10), size))
        key = random.choice(numbers)

        start = time.perf_counter()

        for _ in range(100):
            interpolation_search(numbers, key)

        interpolation_time = (time.perf_counter() - start) / 100 * 1000

        start = time.perf_counter()

        for _ in range(100):
            binary_search(numbers, key)

        binary_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:<10}{interpolation_time:<20.4f}{binary_time:<15.4f}")


# ---------------- Main Program ---------------- #

sample_array = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

index, count = interpolation_search(sample_array, target)

print("Array :", sample_array)
print("Target:", target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")

print("Comparisons:", count)

compare_algorithms()