import math

#1  # Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
print("Sum of 4 and 5:", add_two_numbers(4, 5))


#2  # Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    return math.pi * radius * radius
print("Area of circle with radius 5:", area_of_circle(5))


#3  # Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "All inputs must be numbers!"
        total += num
    return total
print("Sum of numbers:", add_all_nums(2, 4, 5, 6))
print("Invalid input test:", add_all_nums(2, 'x', 5))


#4  # Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
print("25°C in Fahrenheit:", convert_celsius_to_fahrenheit(25))


#5  # Write a function called check_season, it takes a month parameter and returns the season.
def check_season(month):
    month = month.capitalize()
    if month in ['September', 'October', 'November']:
        return "Autumn"
    elif month in ['December', 'January', 'February']:
        return "Winter"
    elif month in ['March', 'April', 'May']:
        return "Spring"
    elif month in ['June', 'July', 'August']:
        return "Summer"
    else:
        return "Invalid month"
print("Season in March:", check_season("March"))


#6  # Write a function called calculate_slope which returns the slope of a linear equation y = mx + c.
def calculate_slope(x1=0, y1=0, x2=1, y2=1):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)
print("Slope between points (2,3) and (5,7):", calculate_slope(2, 3, 5, 7))


#7  # Quadratic equation: ax² + bx + c = 0. Write a function which calculates the solution set.
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2-4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return "No real roots"
print("Solutions of x² + 5x + 6 = 0:", solve_quadratic_eqn(1, 5, 6))


#8  # Declare a function named print_list. It takes a list as parameter and prints each element.
def print_list(items):
    for item in items:
        print(item)
print("\nList items:")
print_list(["Python", "SQL", "AI"])


#9  # Declare a function named reverse_list. It takes a list as parameter and returns it reversed using loops.
def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst = [item] + reversed_lst
    return reversed_lst
print("\nReversed [1,2,3,4,5]:", reverse_list([1, 2, 3, 4, 5]))
print("Reversed ['A','B','C']:", reverse_list(["A", "B", "C"]))


#10  # Declare a function named capitalize_list_items. It takes a list and returns capitalized items.
def capitalize_list_items(items):
    return [item.upper() for item in items]
print("\nCapitalized list:", capitalize_list_items(["apple", "banana", "cherry"]))


#11  # Declare a function named add_item. It takes a list and an item, returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print("\nAdd 'Meat' to food_staff:", add_item(food_staff.copy(), 'Meat'))
numbers = [2, 3, 7, 9]
print("Add 5 to numbers:", add_item(numbers.copy(), 5))


#12  # Declare a function named remove_item. It takes a list and an item, returns the list with the item removed.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print("\nRemove 'Mango' from food_staff:", remove_item(food_staff.copy(), 'Mango'))
numbers = [2, 3, 7, 9]
print("Remove 3 from numbers:", remove_item(numbers.copy(), 3))


#13  # Declare a function named sum_of_numbers. It takes a number n and adds all numbers from 1 to n.
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print("\nSum of numbers up to 5:", sum_of_numbers(50))


#14  # Declare a function named sum_of_odds. It takes a number n and adds all odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total
print("\nSum of odd numbers up to 10:", sum_of_odds(10))


#15  # Declare a function named sum_of_even. It takes a number n and adds all even numbers in that range.
def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total
print("Sum of even numbers up to 10:", sum_of_even(10))