# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1  # Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)

#2  # Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("After adding 'Twitter':", it_companies)

#3  # Insert multiple IT companies at once to the set it_companies
it_companies.update(['Infosys', 'TCS', 'Capgemini'])
print("After adding multiple companies:", it_companies)

#4  # Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print("After removing 'IBM':", it_companies)

#5  # What is the difference between remove and discard
print("""
Difference between remove() and discard():
- remove(item): Removes the specified item, but raises a KeyError if the item does not exist in the set.
- discard(item): Removes the specified item if it exists, but does nothing (no error) if the item is not found.
""")