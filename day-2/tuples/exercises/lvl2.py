# Previous family_members tuple
family_members = ('Yamini', 'Vyshnavi', 'Kiran', 'Ravi', 'Suresh', 'Kaveri')

#1  # Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]
print("Siblings:", siblings)
print("Parents:", parents)

#2  # Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple", "Banana", "Mango")
vegetables = ("Carrot", "Broccoli", "Spinach")
animal_products = ("Milk", "Eggs", "Cheese")
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

#3  # Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

#4  # Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
n = len(food_stuff_lt)
if n % 2 == 1:
    middle_items = [food_stuff_lt[n // 2]]
else:
    middle_items = food_stuff_lt[(n // 2) - 1 : (n // 2) + 1]
print("Middle item(s):", middle_items)

#5  # Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

#6  # Delete the food_staff_tp tuple completely
del food_stuff_tp

#7  # Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print("Is 'Estonia' a nordic country?:", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is 'Iceland' a nordic country?:", is_iceland_nordic)


