countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Estonia', 'Ethiopia']
names = ['Asabeneh', 'Lidiya', 'John', 'Paul']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1  # Explain the difference between map, filter, and reduce
"""
map(function, iterable) -> returns an iterator where the function is applied to every item in the iterable.
    - keeps the same number of items as input (one output per input).
    - use when you want to transform every element.

filter(function, iterable) -> returns an iterator of items for which function(item) is truthy.
    - may return fewer items than input.
    - use when you want to select / keep items that meet a condition.

reduce(function, iterable[, initializer]) -> returns a single value by cumulatively applying function to items.
    - function takes two arguments (accumulator, current).
    - use when you want to fold / aggregate items into one result (sum, product, max, etc.).
"""


# 2  # Explain the difference between higher order function, closure and decorator
"""
Higher-order function (HOF):
    - A function that takes another function as an argument and/or returns a function.
    - Examples: map, filter, functions that accept callback functions, or a factory that returns a function.

Closure:
    - A nested function that remembers (closes over) variables from its enclosing scope even after that scope finished executing.
    - Useful to keep state without using globals or object attributes.

Decorator:
    - A callable (usually a function) that takes a function and returns a new function with extended/wrapped behavior.
    - Decorators typically use closures to capture the original function and return a wrapper.
"""


from functools import reduce

# 3  # Define a callable (function) to reuse with map, filter, reduce
numbers = [1, 2, 3, 4, 5] 

# Map
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print("Map", list(numbers_squared))   

# filter 
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, numbers)
print("Filter", list(even_numbers))     

# reduce
numbers_str = ['1', '2', '3', '4', '5'] 
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print("Reduce", total)   


# 4  # Use for loop to print each country in the countries list.
for country in countries:
    print(country)


# 5  # Use for to print each name in the names list.
for name in names:
    print(name)


# 6  # Use for to print each number in the numbers list.
for number in numbers:
    print(number)