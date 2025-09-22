# index(): Returns the index of the first occurrence of a specified element.
dogs = ['dog1', 'dog2', 'dog3']
index = dogs.index('dog2')
print(f"The index of 'dog2' is: {index}")  # Output: The index of 'dog2' is: 1
sum([1, 2, 3, 4])  # returns the sum of all elements in the list
print(len(dogs))  # Output: 3
print(sum([1, 2, 3, 4]))  # Output: 10


dogs = ['dog1', 'dog2', 'dog3']

# Check if an element is in the list
print('dog1' in dogs)     # True
print('grape' in dogs)      # False

# Check if an element is not in the list
print('dog0' not in dogs)  # True
print('dog1' not in dogs)  # False
print(dogs)  # ['dog0', 'dog1', 'dog2', 'dog3']
dogs.sort()  # sorts the list in place
print(dogs)  # ['dog0', 'dog1', 'dog2', 'dog3']
dogs.insert(0, 'dog0')
print(dogs)  # ['dog0', 'dog0', 'dog1', 'dog2', 'dog3']
