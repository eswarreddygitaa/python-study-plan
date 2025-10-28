import math
import statistics
import keyword


#1  # is_prime
def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True
print("is_prime(2):", is_prime(2))
print("is_prime(15):", is_prime(15))
print("is_prime(97):", is_prime(97))


#2  # checks if all items are unique in the list
def all_unique(lst):
    return len(lst) == len(set(lst))
print("all_unique([1,2,3]):", all_unique([1,2,3]))
print("all_unique([1,2,2]):", all_unique([1,2,2]))


#3  # checks if all the items of the list are of the same data type
def all_same_data_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(x) is first_type for x in lst)
print("all_same_data_type([1,2,3]):", all_same_data_type([1,2,3]))
print("all_same_data_type([1,'2',3]):", all_same_data_type([1,'2',3]))


#4  # check if provided variable is a valid python variable name
def is_valid_variable(name):
    if not isinstance(name, str):
        return False
    return name.isidentifier() and not keyword.iskeyword(name)
print("is_valid_variable('my_var'):", is_valid_variable('my_var'))
print("is_valid_variable('2bad'):", is_valid_variable('2bad'))