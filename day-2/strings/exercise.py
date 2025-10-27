#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to 'Thirty Days Of Python'
a, b, c, d = 'Thirty', 'Days', 'Of', 'Python'
result1 = ' '.join([a, b, c, d])
print(result1)

#2 Concatenate the string 'Coding', 'For', 'All' to 'Coding For All'
x, y, z = 'Coding', 'For', 'All'
result2 = ' '.join([x, y, z])
print(result2)

#3 Declare variable company and assign "Coding For All"
company = "Coding For All"

#4 Print the variable company
print(company)

#5 Print the length of the company string
print("Length =", len(company))

#6 Convert all characters to uppercase
print(company.upper())

#7 Convert all characters to lowercase
print(company.lower())

#8 Use capitalize(), title(), swapcase()
print("(capitalize):", company.capitalize())
print("(title):", company.title())
print("(swapcase):", company.swapcase())

#9 Slice out the first word of "Coding For All"
first_word = company.split()[0]
print("First word =", first_word)

#10 Check if "Coding" exists in "Coding For All"
contains_coding = "Coding" in company
print(contains_coding)

#11 Replace 'Coding' with 'Python'
new_company = company.replace("Coding", "Python")
print(new_company)

#12 Replace "Everyone" with "All" in "Python for Everyone"
text = "Python for Everyone"
print(text.replace("Everyone", "All"))

#13 Split "Coding For All" using space
print(company.split())

#14 Split "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" by comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

#15 Character at index 0
print(company[0])

#16 Last index of string
print(len(company) - 1)

#17 Character at index 10
print(company[10])

#18 Acronym for 'Python For Everyone'
phrase1 = "Python For Everyone"
acronym1 = ''.join(word[0].upper() for word in phrase1.split())
print(acronym1)

#19 Acronym for 'Coding For All'
phrase2 = "Coding For All"
acronym2 = ''.join(word[0].upper() for word in phrase2.split())
print(acronym2)

#20 Index of first occurrence of 'C'
print(company.index('C'))

#21 Index of first occurrence of 'F'
print(company.index('F'))

#22 Last occurrence of 'l' in 'Coding For All People'
text2 = "Coding For All People"
print(text2.rfind('l'))

#23 First occurrence of 'because' in sentence
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find('because'))

#24 Last occurrence of 'because'
print(sentence.rindex('because'))

#25 Slice out 'because because because'
start = sentence.find('because')
end = start + len('because because because')
print(sentence[start:end])

#26 Find position of first 'because' (again)
print(sentence.find('because'))

#27 Slice out phrase 'because because because' (again)
print(sentence[start:end])

#28 Does 'Coding For All' start with 'Coding'?
print(company.startswith("Coding"))

#29 Does 'Coding For All' end with 'coding'?
print(company.endswith("coding"))

#30 Remove left and right spaces
extra_space = "   Coding For All      "
print(extra_space.strip())

#31 Check valid identifiers
print("(30DaysOfPython):", "30DaysOfPython".isidentifier())
print("(thirty_days_of_python):", "thirty_days_of_python".isidentifier())

#32 Join Python library names with hash (#)
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libs = ' # '.join(libs)
print(joined_libs)

#33 Use newline escape sequence to print sentences
line1 = "I am enjoying this challenge."
line2 = "I just wonder what is next."
print(line1 + "\n" + line2)

#34 Use a tab escape sequence to write the following lines
print("Name\t: Asabeneh")
print("Age\t: 250")
print("Country\t: Finland")
print("City\t: Helsinki")

#35 Use string formatting to display:
# The area of a circle with radius 10 is 314
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f}".format(radius, area))

#36 String formatting for arithmetic operations
a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))