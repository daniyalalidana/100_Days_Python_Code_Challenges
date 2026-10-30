'''
Write a function to remove characters 
from a string starting from index 0 up to n
 and return a new string.
'''

def remove_chars(text, no):
    char = text[no::]
    return char

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))