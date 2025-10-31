import re

#1  # Write a pattern which identifies if a string is a valid python variable
    # is_valid_variable('first_name') # True
    # is_valid_variable('first-name') # False
    # is_valid_variable('1first_name') # False
    # is_valid_variable('firstname') # True
def is_valid_variable(var):
    pattern = r'^[A-Za-z_]\w*$'
    return bool(re.match(pattern, var))

# Test cases
print(is_valid_variable('first_name'))   
print(is_valid_variable('first-name'))   
print(is_valid_variable('1first_name'))  
print(is_valid_variable('firstname'))   
