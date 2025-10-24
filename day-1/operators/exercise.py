#1  # Declare your age as integer variable
age = 23

#2  # Declare your height as a float variable
height = 5.82

#3  # Declare a variable that store a complex number
complex_var = 3 + 4j

#4  # Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    # Enter base: 20
    # Enter height: 10
    # The area of the triangle is 100
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is ", int(area))

#5  # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    # Enter side a: 5
    # Enter side b: 4
    # Enter side c: 3
    # The perimeter of the triangle is 12
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a+b+c
print("The perimeter of the triangle is ", int(perimeter))

#6  # Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
l = int(input("Enter length: "))
w = int(input("Enter width: "))
area = l * w
perimeter = 2 * (l * w)
print("The area of the rectangle is ", int(area))
print("The perimeter of the rectangle is ", int(perimeter))

#7  # Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
radius = int(input("Enter radius of a circle: "))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print("area of circle is " int(area))
print("circumference of circle is " int(circumference))

#8  # Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_task8 = 2
y_intercept = -2
x_intercept = -y_intercept / slope_task8
print(f"The slope is: {slope_task8}")
print(f"The y-intercept is: {y_intercept}")
print(f"The x-intercept is: {x_intercept}")

#9  # Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_task9 = (y2 - y1) / (x2 - x1)
print(f"The slope is: {slope_task9}")
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidean distance is: {distance}")

#10  # Compare the slopes in tasks 8 and 9.
if slope_task8 == slope_task9:
    print(f"The slopes are equal.")
else:
    print(f"The slopes are not equal.")

#11  # Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
def calculate_y(x):
  return x**2 + 6*x + 9
x_for_y_is_zero = 0
for x in range(-5, 2): 
  y = calculate_y(x)
  print(f"When x = {x}, y = {y}")
  if y == 0:
    x_for_y_is_zero = x

y_at_root = calculate_y(x_for_y_is_zero)

print("The x value where y is 0 is:")
print(f"x = {x_for_y_is_zero}")

#12  # Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len("python")
len_dragon = len("dragon")
print(f"The length of python is {len_python}")
print(f"The length of dragon is {len_dragon}")
falsy_comparison = len("python") > len("dragon")

print(f"Is the length of 'python' greater than 'dragon'? {falsy_comparison}")

#13  # Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#14  # I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

#15  # There is no 'on' in both dragon and python
print('on' not in 'dragon' or 'on' not in 'python')

#16  # Find the length of the text python and convert the value to float and convert it to string
length = len('python')
print(str(float(length)))

#17  # Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input("Enter a number: "))
if (num % 2 == 0):
  print("Even number")

#18  # Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

#19  # Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#20  # Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

#21  # Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
    # Enter hours: 40
    # Enter rate per hour: 28
    # Your weekly earning is 1120
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is", int(hours * rate))

#22  # Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    # Enter number of years you have lived: 100
    # You have lived for 3153600000 seconds.
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

#23  # Write a Python script that displays the following table
    # 1 1 1 1 1
    # 2 1 2 4 8
    # 3 1 3 9 27
    # 4 1 4 16 64
    # 5 1 5 25 125
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
