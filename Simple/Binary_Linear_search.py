def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps


def binary_search(arr, target):
    steps = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps


numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = int(input("Enter number to search: "))

pos1, steps1 = linear_search(numbers, target)
pos2, steps2 = binary_search(numbers, target)

print(f"Linear Search: found at index {pos1} in {steps1} steps")
print(f"Binary Search: found at index {pos2} in {steps2} steps")