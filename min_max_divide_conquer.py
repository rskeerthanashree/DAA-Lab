import random

comparison_counter = 0


def find_min_max(values, left, right):
    global comparison_counter

    # Only one element
    if left == right:
        return values[left], values[left]

    # Two elements
    if right == left + 1:
        comparison_counter += 1
        if values[left] < values[right]:
            return values[left], values[right]
        return values[right], values[left]

    # Divide
    middle = (left + right) // 2

    left_min, left_max = find_min_max(values, left, middle)
    right_min, right_max = find_min_max(values, middle + 1, right)

    # Combine
    comparison_counter += 1
    minimum = left_min if left_min < right_min else right_min

    comparison_counter += 1
    maximum = left_max if left_max > right_max else right_max

    return minimum, maximum


def normal_min_max(values):

    minimum = maximum = values[0]
    comparisons = 0

    for number in values[1:]:

        comparisons += 1
        if number < minimum:
            minimum = number

        comparisons += 1
        if number > maximum:
            maximum = number

    return minimum, maximum, comparisons


# ---------------- Main Program ---------------- #

numbers = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

comparison_counter = 0

minimum, maximum = find_min_max(numbers, 0, len(numbers) - 1)

dc_comparisons = comparison_counter

_, _, normal_comparisons = normal_min_max(numbers)

print("Input Array")
print(numbers)

print("\nMinimum Value :", minimum)
print("Maximum Value :", maximum)

print("\nComparisons")
print(f"Divide & Conquer : {dc_comparisons}")
print(f"Normal Method    : {normal_comparisons}")

print("\nPerformance Comparison")
print("-" * 60)
print(f"{'Size':<10}{'D&C':>10}{'Normal':>12}{'Expected':>15}")
print("-" * 60)

for size in [10, 100, 1000, 10000]:

    values = [random.randint(1, 10000) for _ in range(size)]

    comparison_counter = 0

    find_min_max(values, 0, len(values) - 1)

    divide_count = comparison_counter

    _, _, normal_count = normal_min_max(values)

    expected = (3 * size) // 2 - 2

    print(f"{size:<10}{divide_count:>10}{normal_count:>12}{expected:>15}")