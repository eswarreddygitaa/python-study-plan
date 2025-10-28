# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    mid_index = len(skills) // 2
    print("\nMiddle skill:", skills[mid_index])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if set(person['skills']) == {'JavaScript', 'React'}:
    print("He is a front end developer.")
elif {'Node', 'Python', 'MongoDB'}.issubset(person['skills']):
    print("He is a backend developer.")
elif {'React', 'Node', 'MongoDB'}.issubset(person['skills']):
    print("He is a fullstack developer.")
else:
    print("Unknown title.")

# If the person is married and if he lives in Finland, print the information in the following format:
    # Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. "f"He is married.")

