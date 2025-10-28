#1  # Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [num for num in numbers if num <= 0]
print(neg_and_zero)


#2  # Flatten a list of lists of lists to a one-dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flattened)


#3  # Using list comprehension create the following list of tuples
    # [(0, 1, 0, 0, 0, 0, 0),
    # (1, 1, 1, 1, 1, 1, 1),
    # (2, 1, 2, 4, 8, 16, 32),
    # (3, 1, 3, 9, 27, 81, 243),
    # (4, 1, 4, 16, 64, 256, 1024),
    # (5, 1, 5, 25, 125, 625, 3125),
    # (6, 1, 6, 36, 216, 1296, 7776),
    # (7, 1, 7, 49, 343, 2401, 16807),
    # (8, 1, 8, 64, 512, 4096, 32768),
    # (9, 1, 9, 81, 729, 6561, 59049),
    # (10, 1, 10, 100, 1000, 10000, 100000)]
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
for t in tuple_list:
    print(t)

#4  # Flatten the countries list to a new list with uppercase and abbreviation
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries = [[country.upper(), country[:3].upper(), city.upper()] for pair in countries for (country, city) in pair]
print(formatted_countries)


#5  # Change the countries list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dicts = [{'country': country.upper(), 'city': city.upper()} for pair in countries for (country, city) in pair]
print(country_dicts)


#6  # Change list of lists to concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for pair in names for (first, last) in pair]
print(full_names)


#7  # Lambda function to solve slope or y-intercept of linear functions 
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda x, y, m: y - m * x
print("Slope between (2,3) and (4,7):", slope(2, 3, 4, 7))
m = slope(2, 3, 4, 7)
print("Y-intercept for point (2,3):", y_intercept(2, 3, m))