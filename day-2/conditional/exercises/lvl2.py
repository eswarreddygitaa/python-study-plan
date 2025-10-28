#1  # Write a code which gives grade to students according to theirs scores:
        # 80-100, A
        # 70-89, B
        # 60-69, C
        # 50-59, D
        # 0-49, F
score = int(input("Enter your score: "))
if score >= 80 and score <= 100:
    print("A")
elif score >= 70 and score <= 89:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("D")
elif score <= 49 and score >= 0:
    print("F")
else:
    Print("Invalid score")

#2  # Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
    # December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter the month: ").capitalize()
if month in ['September', 'October', 'November']:
    season = "Autumn"
elif month in ['December', 'January', 'February']:
    season = 'Winter'
elif month in ['March', 'April', 'May']:
    season = 'Spring'
elif month in ['June', 'July', 'August']:
    season = 'Summer'
else:
    season = 'Invalid month'

print(f"The season is {season}.")

#3  # The following list contains some fruits:
        # fruits = ['banana', 'orange', 'mango', 'lemon']
        # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").lower()
if fruit in fruits:
    print('That fruit already exist in the list')
else: 
    fruits.append(fruit)
    print("Modified fruits list", fruits) 
