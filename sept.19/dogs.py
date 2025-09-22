dogs = ['dog1', 'dog2', 'dog3']
dogs[0]
print(dogs[0]) # will print dog1
# slicing, able to etract portion of the list using syntact list[start:stop:step]
print(dogs[0:2])  # dog1, dog2
print(dogs[:2])   # dog1, dog2
print(dogs[1:])   # dog2, dog3

#len function
print(len(dogs))  # 3 ['dog1', 'dog2', 'dog3']

#list methods
dogs.append('dog4')  # adds dog4 to the end of the list
print(dogs)  # ['dog1', 'dog2', 'dog3', 'dog4']
dogs.insert(1, 'dog1.5')  # inserts dog1.5 at index 1
print(dogs)  # ['dog1', 'dog1.5', 'dog2', 'dog3', 'dog4']
dogs.remove('dog1.5')  # removes dog1.5 from the list
print(dogs)  # ['dog1', 'dog2', 'dog3', 'dog4']
popped_dog = dogs.pop()  # removes and returns the last item
print(popped_dog)  # dog4
dogs.insert(0, 'dog0')  # inserts dog0 at the beginning
print(dogs)  # ['dog0', 'dog1', 'dog2', 'dog3']
dogs.sort()  # sorts the list in place
print(dogs)  # ['dog0', 'dog1', 'dog2', '
dogs.remove[dogs]  # removes dog0 from the list
print(dogs)  # ['dog1', 'dog2', 'dog3']
