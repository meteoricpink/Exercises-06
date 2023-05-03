# Exercise 6

# 1
def power(a, b):
    if a <= 0 or b <= 0:
        return -1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

# Example
print(power(2, 5))
print(power(3, 3))
print(power(0, 5))

# 2
def binary_search(numbers, num, left, right):
    # Perform binary search to find a target element in a sorted list of integers

    # Base case: if left > right, the search range is empty, so the element is not in the list
    if left > right:
        return -1

    # Find the middle index of the search range
    mid = (left + right) // 2

    # Base case: if the middle element is the target element, return its index
    if numbers[mid] == num:
        return mid

    # Recursive case: if the middle element is less than the target element, search in the right half of the list
    elif numbers[mid] < num:
        return binary_search(numbers, num, mid+1, right)

    # Recursive case: if the middle element is greater than the target element, search in the left half of the list
    else:
        return binary_search(numbers, num, left, mid-1)

# Example
numbers = [2, 5, 7, 8, 10, 12, 15]
num = 8

result = binary_search(numbers, num, 0, len(numbers)-1)
print(result)

numbers = [2, 5, 7, 10, 14, 18, 21]
target = 15

result = binary_search(numbers, target, 0, len(numbers)-1)
print(result)





