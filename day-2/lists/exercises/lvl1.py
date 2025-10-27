#1  # Declare an empty list
empty_list = []

#2  # Declare a list with more than 5 items
my_list = [10, 20, 30, 40, 50, 60, 70]

#3  # Find the length of your list
length_of_my_list = len(my_list)
print("Length of my_list:", length_of_my_list)

#4  # Get the first item, the middle item and the last item of the list
first_item = my_list[0]
middle_index = (len(my_list) - 1) // 2
middle_item = my_list[middle_index]
last_item = my_list[-1]
print("First, middle, last:", first_item, middle_item, last_item)

#5  # Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Eswar Reddy Pagadala", 23, 5.8, "No", "Chennai, India"]

#6  # Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7  # Print the list using print()
print("it_companies:", it_companies)

#8  # Print the number of companies in the list
num_companies = len(it_companies)
print("Number of companies:", num_companies)

#9  # Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[(len(it_companies)-1)//2]
last_company = it_companies[-1]
print("First, middle, last company:", first_company, middle_company, last_company)

#10  # Print the list after modifying one of the companies
it_companies[0] = "Meta"
print("After modifying first company to Meta:", it_companies)

#11  # Add an IT company to it_companies
it_companies.append("Gitaa")
print("After append Gitaa:", it_companies)

#12  # Insert an IT company in the middle of the companies list
mid_pos = len(it_companies) // 2
it_companies.insert(mid_pos, "TCS")
print("After inserting TCS in middle:", it_companies)

#13  # Change one of the it_companies names to uppercase (IBM excluded!)
for i, name in enumerate(it_companies):
    if name == "IBM":
        continue
    if name == "Google":
        it_companies[i] = name.upper()
        break
print("After changing Google to uppercase (IBM excluded):", it_companies)

#14  # Join the it_companies with a string '#;  '
joined_companies = "#;  ".join(it_companies)
print("Joined companies string:", joined_companies)

#15  # Check if a certain company exists in the it_companies list.
company_to_check = "Oracle"
exists = company_to_check in it_companies
print(f"Does '{company_to_check}' exist in it_companies?:", exists)

#16  # Sort the list using sort() method
it_companies.sort()
print("Sorted it_companies (ascending):", it_companies)

#17  # Reverse the list in descending order using reverse() method
it_companies.reverse()
print("Reversed it_companies (now descending):", it_companies)

#18  # Slice out the first 3 companies from the list
first_three = it_companies[:3]
print("First 3 companies:", first_three)

#19  # Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print("Last 3 companies:", last_three)

#20  # Slice out the middle IT company or companies from the list
n = len(it_companies)
if n % 2 == 1:
    middle_slice = [it_companies[n//2]]
else:
    middle_slice = it_companies[(n//2)-1:(n//2)+1]
print("Middle company/companies:", middle_slice)

#21  # Remove the first IT company from the list
removed_first = it_companies.pop(0)
print("Removed first company:", removed_first)
print("List now:", it_companies)

#22  # Remove the middle IT company or companies from the list
n = len(it_companies)
if n % 2 == 1:
    removed_middle = it_companies.pop(n//2)
    print("Removed middle company:", removed_middle)
else:
    removed_middle = it_companies[(n//2)-1:(n//2)+1]
    del it_companies[(n//2)-1:(n//2)+1]
    print("Removed middle companies:", removed_middle)
print("List now after removing middle:", it_companies)

#23  # Remove the last IT company from the list
removed_last = it_companies.pop(-1)
print("Removed last company:", removed_last)
print("List now:", it_companies)

#24  # Remove all IT companies from the list
it_companies.clear()
print("After clearing all companies, it_companies:", it_companies)

#25  # Destroy the IT companies list
del it_companies

#26  # Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
print("Joined list (front_end + back_end):", joined)

#27  # After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = joined.copy()
idx = full_stack.index('Redux')
full_stack.insert(idx+1, 'Python')
full_stack.insert(idx+2, 'SQL')
print("full_stack after inserting Python and SQL after Redux:", full_stack)