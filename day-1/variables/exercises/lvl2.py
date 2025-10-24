first_name, last_name, age, is_true, height = "Eswar Reddy", "pagadala", 23, False, 5.82

#1  # Check the data type of all your variables using type() built-in function
print(f"Data Type of {first_name}:", type(first_name))
print(f"Data Type of {age}:", type(age))
print(f"Data Type of {is_true}:", type(is_true))
print(f"Data Type of {height}:", type(height))

#2  # Using the len() built-in function, find the length of your first name
print(f"Length of {first_name}:", len(first_name))

#3  # Compare the length of your first name and your last name
if len(first_name)>len(last_name):
    print("First name is longer than Last name")
else:
    print("Last name is longer than First name")

#4  # Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#5  # Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

#6  # Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)

#7  # Multiply num_two and num_one and assign the value to a variable product
product = num_one*num_two
print(product)

#8  # Divide num_one by num_two and assign the value to a variable division
division = num_two / num_one
print(division)

#9  # Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print(remainder)

#10  # Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_two**num_one
print(exp)

#11  # Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

#12  # The radius of a circle is 30 meters.
#12.1  # Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math

r = 30
area_of_circle = math.pi * (r**2)
print("area of a circle:", area_of_circle)

#12.2  # Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * (r**2)

#12.3 # Take radius as user input and calculate the area.
radius = int(input("Enter radius of circle:"))
area_of_circle = math.pi * (radius**2)
print("area of a circle:", area_of_circle)

#13  # Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter country: ")
age = int(input("Enter your age: "))


#14  # Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help('keywords'))