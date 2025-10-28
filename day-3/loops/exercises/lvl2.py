# 1  # Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total_sum = 0
for i in range(101):
    total_sum += i
print("The sum of all numbers is", total_sum)  


# 2  # Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print("The sum of all evens is", sum_evens)  
print("The sum of all odds is", sum_odds)