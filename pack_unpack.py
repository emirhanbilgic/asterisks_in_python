# Unpacking
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)  # Output: 1 [2, 3, 4] 5

# Packing
numbers = [1, 2, 3, 4, 5]
new_numbers = [*numbers, 6, 7, 8]
print(new_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
