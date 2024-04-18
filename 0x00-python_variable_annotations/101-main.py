#!/usr/bin/env python3

safely_get_value = __import__('101-safely_get_value').safely_get_value
annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print(("{}: {}".format(k, v)))

# example of usage
# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using the safely_get_value function to safely access values
value_a = safely_get_value(my_dict, 'a')  # Accessing existing key
# Accessing non-existing key with default value
value_d = safely_get_value(my_dict, 'd', default='Not found')

# Printing the results
print("Value of 'a':", value_a)  # Output: Value of 'a': 1
print("Value of 'd':", value_d)  # Output: Value of 'd': Not found
