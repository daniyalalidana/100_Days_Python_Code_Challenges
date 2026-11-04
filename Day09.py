#Practice Problem: Write a script that takes 
# a list containing duplicate items and returns 
# a new list with only unique elements.

data = [1, 2, 2, 3, 4, 4, 4, 5]

data = set(data)
data = list(data)

print(data)