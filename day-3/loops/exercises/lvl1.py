#1  # Iterate 0 to 10 using for loop, do the same using while loop.
print("Using for loop (0 to 10):")
for i in range(11):
    print(i, end=" ")

print("\nUsing while loop (0 to 10):")
i = 0
while i <= 10:
    print(i, end=" ")
    i += 1


#2  # Iterate 10 to 0 using for loop, do the same using while loop.
print("\nUsing for loop (10 to 0):")
for i in range(10, -1, -1):
    print(i, end=" ")

print("\nUsing while loop (10 to 0):")
i = 10
while i >= 0:
    print(i, end=" ")
    i -= 1


#3  # Write a loop that makes seven calls to print(), so we get the following triangle:
    #
    ##
    ###
    ####
    #####
    ######
    #######
print("\nTriangle pattern:")
for i in range(1, 8):
    print("#" * i)


#4  # Use nested loops to create the following 8x8 pattern of '#'
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
print("\n8x8 pattern of #:")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()  # New line after each row


#5  # Print the multiplication pattern: n x n = n²
    # 0 x 0 = 0
    # 1 x 1 = 1
    # 2 x 2 = 4
    # 3 x 3 = 9
    # 4 x 4 = 16
    # 5 x 5 = 25
    # 6 x 6 = 36
    # 7 x 7 = 49
    # 8 x 8 = 64
    # 9 x 9 = 81
    # 10 x 10 = 100
print("\nMultiplication pattern (n x n = n²):")
for i in range(11):
    print(f"{i} x {i} = {i * i}")


#6  # Iterate through the list ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] and print items
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lang in languages:
    print(lang)


#7  # Use for loop to iterate from 0 to 100 and print only even numbers
print("\nEven numbers from 0 to 100:")
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=" ")


#8  # Use for loop to iterate from 0 to 100 and print only odd numbers
print("\n\nOdd numbers from 0 to 100:")
for i in range(0, 101):
    if i % 2 != 0:
        print(i, end=" ")