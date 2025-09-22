"""
A nested list is a list that contains other lists as its elements. In simpler terms, it's a list of lists.
Nested lists allow you to organize data in a hierarchical structure, making them useful for representing things like matrices or multi-dimensional data.
"""

# Example: Creating and working with nested lists
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

# Concatenation with `+` operator
new_list = a + b + c
print("Concatenated list:", new_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creating a nested list
nested_list = [a, b, c]
print("Nested list:", nested_list)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Slicing the first two sublists
sliced_list = nested_list[0:2]
print("Sliced nested list:", sliced_list)  # Output: [[1, 2, 3], [4, 5, 6]]

# Accessing elements in a nested list
print("Second element of first sublist:", nested_list[0][1])  # Output: 2

# Summing all numbers in the nested list
total = sum(sum(sublist) for sublist in nested_list)
print("Sum of all elements in nested list:", total)  # Output: 45

user_input = input("What is the sum of all elements in the nested list? ")

if user_input == str(total):
    print("Correct!")
else:
    print("Incorrect. The correct answer is:", total)
# Output:
# Concatenated list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Nested list: [[   1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Sliced nested list: [[1, 2, 3], [4, 5, 6]]
# Second element of first sublist: 2
# Sum of all elements in nested list: 45
my_string = "Hello, World!"
print(my_string[7], my_string[-1])  # Output: W !
