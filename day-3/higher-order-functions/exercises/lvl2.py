from functools import reduce

# Data setup
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Estonia', 'Ethiopia']
names = ['Asabeneh', 'Lidiya', 'John', 'Paul']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#1  # Use map to create a new list by changing each country to uppercase
countries_upper = list(map(lambda c: c.upper(), countries))
print(countries_upper)


#2  # Use map to create a new list by changing each number to its square
squared_numbers = list(map(lambda n: n ** 2, numbers))
print(squared_numbers)


#3  # Use map to change each name to uppercase
names_upper = list(map(lambda n: n.upper(), names))
print(names_upper)


#4  # Use filter to filter out countries containing 'land'
countries_with_land = list(filter(lambda c: 'land' in c.lower(), countries))
print(countries_with_land)


#5  # Use filter to filter out countries having exactly six characters
countries_six_chars = list(filter(lambda c: len(c) == 6, countries))
print(countries_six_chars)


#6  # Use filter to filter out countries containing six letters and more
countries_six_or_more = list(filter(lambda c: len(c) >= 6, countries))
print(countries_six_or_more)


#7  # Use filter to filter out countries starting with an 'E'
countries_start_E = list(filter(lambda c: c.startswith('E'), countries))
print(countries_start_E)


#8  # Chain two or more list iterators (map + filter + reduce)
# Example: Square all even numbers and sum them
result = reduce(
    lambda acc, val: acc + val,
    filter(lambda x: x % 2 == 0, map(lambda n: n ** 2, numbers))
)
print(result)


#9  # Declare a function called get_string_lists which takes a list and returns only string items
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

# Example mixed list
mixed_list = ['Hello', 10, True, 'Python', 25.5, 'AI']
string_items = get_string_lists(mixed_list)
print(string_items)


#10  # Use reduce to sum all numbers in the numbers list
sum_all = reduce(lambda acc, val: acc + val, numbers)
print("#10 Sum of all numbers using reduce:")
print(sum_all)