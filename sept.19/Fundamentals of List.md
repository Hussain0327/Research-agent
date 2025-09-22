01 List, String and Tuple.ipynb
Fundamentals of List
In Python, a list is a built-in data type used to store collections of items. Lists are:

Ordered: Elements have a specific order, and that order is maintained.
Mutable: Elements in a list can be modified, added, or removed after the list is created.
Heterogeneous: A list can contain items of different data types (e.g., integers, strings, other lists).
Dynamic: Lists can grow or shrink in size as items are added or removed.
Key characteristics of lists:

Lists are defined using square brackets ([]).
Items in the list are separated by commas.
dogs = ['d1','d2','d3']
ages = [20,22,25,29,30]
mixed_list=['jamez',20,10.10]
Accessing List Items
To access items in a list, we use indexing. Each element in a list has an index, starting from 0 for the first element.

Given the list dogs = ['d1', 'd2', 'd3'], here's how you can access the items:

1. Accessing by index: You can access each element using its index.

dogs[0] gives you the first item ('d1').
dogs[1] gives you the second item ('d2').
dogs[2] gives you the third item ('d3').
dogs = ['d1', 'd2', 'd3']
# Accessing elements by index
print(dogs[0])  # Output: 'd1'
print(dogs[1])  # Output: 'd2'
print(dogs[2])  # Output: 'd3'
2. Accessing using negative indices: Negative indexing allows you to access elements from the end of the list.

dogs[-1] gives you the last item ('d3').
dogs[-2] gives you the second-to-last item ('d2').
dogs[-3] gives you the third-to-last item (which is also the first item in this case, 'd1').
# Accessing elements using negative indices
print(dogs[-1])  # Output: 'd3'
print(dogs[-2])  # Output: 'd2'
print(dogs[-3])  # Output: 'd1'
Slicing List Items
Slicing in Python lists is a way to extract a portion of the list using the syntax list[start:stop:step]. The start index is where the slice begins (inclusive), the stop index is where it ends (exclusive), and the optional step defines the interval between elements. If omitted, start defaults to the beginning, stop to the end, and step to 1.

dogs = ['d1', 'd2', 'd3', 'd4', 'd5']
# Slice from index 1 to 3 (index 3 not included)
print(dogs[1:3:1])  # Output: ['d2', 'd3']
# Slice using negative indices
print(dogs[-4:-1])  # Output: ['d2', 'd3', 'd4']
Some Common List functions
1. len(): Returns the number of elements in a list.

my_list = [10, 20, 30, 40]
print(len(my_list))  # Output: 4
2. append(): Adds an element to the end of a list.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
3. insert(): Inserts an element at a specified position in the list.

my_list = [1, 2, 4]
my_list.insert(2, 3)  # Insert 3 at index 2
print(my_list)  # Output: [1, 2, 3, 4]
4. remove(): Removes the first occurrence of a specified element from the list.

my_list = [10, 20, 30, 20, 40]
my_list.remove(20)
print(my_list)  # Output: [10, 30, 20, 40]
5. pop(): Removes and returns the element at the specified index. If no index is specified, it removes and returns the last element.

my_list = [1, 2, 3, 4]
popped_item = my_list.pop(2)  # Removes element at index 2
print(popped_item)  # Output: 3
print(my_list)  # Output: [1, 2, 4]
6. index(): Returns the index of the first occurrence of a specified element.

my_list = [10, 20, 30, 40]
print(my_list.index(30))  # Output: 2
7. count(): Returns the number of occurrences of a specified element in the list.

my_list = [1, 2, 2, 3, 2, 4]
print(my_list.count(2))  # Output: 3
8. sort(): Sorts the elements of the list in ascending order. It modifies the list in place.

my_list = [5, 3, 8, 1, 7]
my_list.sort()
print(my_list)  # Output: [1, 3, 5, 7, 8]
# Descending Order
my_list.sort(reverse=True)
print(my_list)  # Output: [8, 7, 5, 3, 1]
9. reverse(): Reverses the order of the elements in the list.

my_list = [10, 20, 30]
my_list.reverse()
print(my_list)  # Output: [30, 20, 10]
10. sum(): Returns the sum of all elements in the list (assuming the list contains numeric elements).

my_list = [1, 2, 3, 4]
print(sum(my_list))  # Output: 10
11. max() and min(): Returns the maximum and minimum element in the list.

my_list = [10, 20, 5, 15]
print(max(my_list))  # Output: 20
print(min(my_list))  # Output: 5
Membership Operations
Membership operation in a Python list checks whether a specific element exists in the list using the keywords in and not in. The expression element in list returns True if the element is present and False otherwise. Conversely, element not in list returns True if the element is absent. This operation works by scanning the list from start to end and is commonly used in conditions, loops, and filters.

fruits = ['apple', 'banana', 'cherry']

# Check if an element is in the list
print('banana' in fruits)     # True
print('grape' in fruits)      # False

# Check if an element is not in the list
print('grape' not in fruits)  # True
print('apple' not in fruits)  # False
  
More on List
Nested List
A nested list is a list that contains other lists as its elements. In simpler terms, it's a list of lists. Nested lists allow you to organize data in a hierarchical structure, making them useful for representing things like matrices or multi-dimensional data.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Here, nested_list contains three elements, each of which is a list itself:

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
To access elements in a nested list, we use multiple indices, one for each level of nesting. For example:

nested_list[0] would give you the first list: [1, 2, 3].
nested_list[1][2] would give you the third element of the second list: 6.
nested_list = [[10, 20, 30], [40, 50], [60, 70, 80]]

# Access the first list
print(nested_list[0])  # Output: [10, 20, 30]

# Access the second element of the first list
print(nested_list[0][1])  # Output: 20

# Access the third element of the third list
print(nested_list[2][2])  # Output: 80
List Operations
Lists support various operations that allow you to manipulate and combine them. The + operator and the * operator are commonly used for concatenating and repeating lists, respectively. However, some operations are unsupported on lists, and understanding them can prevent runtime errors.

1. Concatenation with the + Operator:
The + operator is used to combine two or more lists. When you use the + operator between two lists, it creates a new list that is the result of appending the elements of the second list to the first list.

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
2. Repetition with the * Operator:
The * operator is used to repeat a list a specified number of times. When you multiply a list by an integer, it creates a new list that contains the elements of the original list repeated that many times.

a = [1, 2, 3]
print(a * 2)
3. Unsupported Operations:
Subtraction (-) on Lists: Python does not support the - operator for removing elements from one list based on another.

a = [1, 2, 3]
b = [2, 3]
print(a - b)  # This will raise a TypeError
Division (/) on Lists: Division of lists is not supported in Python.

a = [1, 2, 3]
print(a / 2)  # This will raise a TypeError
Multiplication (*) with Two Lists: Multiplying two lists together is not allowed.

a = [1, 2, 3]
b = [4, 5, 6]
print(a * b)  # This will raise a TypeError
The del statement
The del is a statement used to delete objects. When applied to a list or tuple, it can remove elements, slices, or even the entire object.

Deleting an Element by Index: You can use del to remove a specific element from a list by its index.

my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Removes the element at index 2 (which is 3)
print(my_list)  # Output: [1, 2, 4, 5]
Deleting a Slice of a List: del can also be used to remove a slice from a list.

my_list = [1, 2, 3, 4, 5]
del my_list[1:4]  # Removes elements from index 1 to 3 (inclusive)
print(my_list)  # Output: [1, 5]
Deleting the Entire List: To remove the entire list, you can use del followed by the list name.

my_list = [1, 2, 3, 4, 5]
del my_list
# print(my_list)  # This will raise an error because my_list no longer exists
Strings
In Python, strings are sequences of characters, and they can be treated similarly to lists in many ways. Since both strings and lists are sequences, you can perform common sequence operations on strings, such as indexing, slicing, and iterating.

my_string = "hello"
This string can be thought of as a list of characters: ['h', 'e', 'l', 'l', 'o'].

1. Indexing Strings:
You can use indexing to access individual characters of a string just like you would with a list.

my_string = "hello"
print(my_string[0])  # Output: 'h'
print(my_string[-1]) # Output: 'o'
2. Slicing Strings:
You can also slice strings, just like lists, to get a substring.

my_string = "hello"
print(my_string[1:4])  # Output: 'ell'
print(my_string[:3])   # Output: 'hel'
print(my_string[2:])   # Output: 'llo'
3. Length of a String (len()):
You can use the len() function to get the length of a string, just like with a list.

my_string = "hello"
print(len(my_string))  # Output: 5
4. Concatenation of Strings:
Like lists, you can concatenate strings using the + operator.

a = "hello"
b = "world"
print(a + " " + b)  # Output: 'hello world'
5. Repetition of Strings:
You can repeat strings using the * operator, just like with lists.

my_string = "hi"
print(my_string * 3)  # Output: 'hihihi'
Tuple
A tuple is similar to a list in that it is an ordered collection of elements that can store items of different data types, such as integers, strings, or even other tuples. Like lists, tuples support indexing, slicing, iteration, concatenation, repetition, membership testing, and functions like len(), min(), and max(). In fact, most operations that lists support are also supported by tuples. However, the key difference is that tuples are immutable, meaning their elements cannot be changed, added, or removed after creation. Tuples are defined using parentheses () instead of square brackets []. Because of their immutability, tuples are often used for fixed collections of data and are generally faster and more memory-efficient than lists.

tple = (1, 2, 3, 4)
