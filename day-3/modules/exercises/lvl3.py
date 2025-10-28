import random

#1   # Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled
original_list = [1, 2, 3, 4, 5, 6, 7]
print("Original list:", original_list)
print("Shuffled list:", shuffle_list(original_list))


#2   # Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    numbers = random.sample(range(0, 10), 7)
    return numbers
print(unique_random_numbers())