#1  # Create an empty tuple
empty_tuple = ()

#2  # Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Yamini", "Vyshnavi")
brothers = ("Kiran", "Ravi")

#3  # Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("Siblings:", siblings)

#4  # How many siblings do you have?
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

#5  # Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Suresh", "Kaveri")
print("Family members:", family_members)
