import math
import statistics
import keyword

# Declare a function named evens_and_odds. 
# It takes a positive integer n and counts evens and odds in the range 0..n inclusive.
def evens_and_odds(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    evens = (n // 2) + 1  # includes 0
    odds = (n + 1) - evens
    return evens, odds
ev, od = evens_and_odds(100)
print(f"The number of odds are {od}.")
print(f"The number of evens are {ev}.\n")


#1  # Call your function factorial, it takes a whole number as parameter and returns factorial
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("factorial is only defined for integers.")
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print("5! =", factorial(5))   
print("0! =", factorial(0))   


#2  # Call your function is_empty, it takes a parameter and checks if it is empty or not
def is_empty(x):
    if x is None:
        return True
    try:
        return len(x) == 0
    except TypeError:
        return False
print("is_empty([]):", is_empty([]))
print("is_empty(''):", is_empty(""))
print("is_empty(None):", is_empty(None))
print("is_empty(5):", is_empty(5))


#3  # calculate_mean
def calculate_mean(numbers):
    if not numbers:
        raise ValueError("numbers list is empty")
    nums = [float(x) for x in numbers]
    return sum(nums) / len(nums)

#4  # calculate_median
def calculate_median(numbers):
    if not numbers:
        raise ValueError("numbers list is empty")
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2

#5  # calculate_mode (returns list of mode(s) to handle multimodal lists)
def calculate_mode(numbers):
    if not numbers:
        raise ValueError("numbers list is empty")
    freq = {}
    for x in numbers:
        freq[x] = freq.get(x, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]

# Examples
nums = [2, 4, 4, 4, 5, 5, 7, 9]
print("mean:", calculate_mean(nums))
print("median:", calculate_median(nums))
print("mode:", calculate_mode(nums))
