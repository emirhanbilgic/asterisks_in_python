def sum_numbers(*numbers):
    return sum(numbers)

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15

#other pack-unpack examples:

def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

info = {"name": "John", "age": 30}
print_info(**info)  # Output: Name: John, Age: 30

values = [10, 20, 30]
print("The values are {} {} {}".format(*values))  # Output: The values are 10 20 30

