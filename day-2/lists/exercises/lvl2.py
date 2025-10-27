# Given ages list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1) Sort the list and find the min and max age
ages_sorted = sorted(ages)
min_age = ages_sorted[0]
max_age = ages_sorted[-1]
print("Sorted ages:", ages_sorted)
print("Min age:", min_age)
print("Max age:", max_age)

# 2) Add the min age and the max age again to the list
ages_extended = ages.copy()
ages_extended.append(min_age)
ages_extended.append(max_age)
print("Ages after adding min and max again:", ages_extended)

ages_extended = sorted(ages_extended)
n = len(ages_extended)

# 3) Find the median age (one middle item or two middle items divided by two)
if n % 2 == 1:
    median_age = ages_extended[n // 2]
else:
    median_age = (ages_extended[n//2 - 1] + ages_extended[n//2]) / 2
print("Median age:", median_age)

# 4) Find the average age (sum of all items divided by their number )
average_age = sum(ages_extended) / n
print("Average age:", average_age)

# 5) Find the range of the ages (max - min)
range_ages = max_age - min_age
print("Range of ages:", range_ages)

# 6) Compare the value of (min - average) and (max - average), use abs() method
abs_min_avg = abs(min_age - average_age)
abs_max_avg = abs(max_age - average_age)
print("min - average:", abs_min_avg)
print("max - average:", abs_max_avg)

# --- Countries part ---
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark', 'India']

# 7) Find the middle country(ies) in the countries list
m = len(countries)
if m % 2 == 1:
    middle_countries = [countries[m // 2]]
else:
    middle_countries = countries[m//2 - 1 : m//2 + 1]
print("Countries list:", countries)
print("Middle country(ies):", middle_countries)

# 8) Divide the countries list into two equal lists if it is even if not one more country for the first half.
if m % 2 == 0:
    first_half = countries[:m//2]
    second_half = countries[m//2:]
else:
    first_half = countries[: (m//2) + 1]
    second_half = countries[(m//2) + 1 :]
print("First half:", first_half)
print("Second half:", second_half)

# 9) Unpack the first three countries and the rest as scandic countries
first, second, third, *scandic_countries = countries
print("First three unpacked:", first, second, third)
print("Scandic countries (rest):", scandic_countries)