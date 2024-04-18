#!/usr/bin/env python3

element_length = __import__('9-element_length').element_length

print(element_length.__annotations__)

# Define a list of sequences (lists and tuples)
sequences = [(1, 2, 3), [4, 5, 6, 7], "hello"]

# Call the element_length function with the list of sequences
result = element_length(sequences)

# Print the result
print(result)
