dogs = ['dog1', 'dog2', 'dog3']
ages = [' 2', '3', '4']
types = ['bulldog', 'labrador', 'poodle']

dog_info = list(zip(dogs, ages, types))
print(dog_info)
print(dog_info[0][0])  # Accessing the name of the first dog 
# Output: dog-2
print(dog_info[-1][1])  # Accessing the age of the last dog
# -1,-2,-3, negative indexes
cars = ['bmw', 'audi', 'ford']
car_info = [list(zip(cars, ages))]
