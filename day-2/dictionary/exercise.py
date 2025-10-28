#1  # Create an empty dictionary called dog
dog = {}

#2  # Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3
print("Dog dictionary:", dog)

#3  # Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Eswar Reddy",
    "last_name": "Pagadala",
    "gender": "Male",
    "age": 23,
    "marital_status": "Single",
    "skills": ["Python", "SQL"],
    "country": "India",
    "city": "Chennai",
    "address": "123 Main Street"
}

#4  # Get the length of the student dictionary
print("Length of student dictionary:", len(student))

#5  # Get the value of skills and check the data type, it should be a list
skills = student["skills"]
print("Skills:", skills)
print("Type of skills:", type(skills))

#6  # Modify the skills values by adding one or two skills
student["skills"].extend(["Power BI", "Machine Learning"])
print("Updated skills:", student["skills"])

#7  # Get the dictionary keys as a list
keys_list = list(student.keys())
print("Keys list:", keys_list)

#8  # Get the dictionary values as a list
values_list = list(student.values())
print("Values list:", values_list)

#9  # Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Dictionary as list of tuples:", student_items)

#10  # Delete one of the items in the dictionary
del student["marital_status"]

#11  # Delete one of the dictionaries
del dog