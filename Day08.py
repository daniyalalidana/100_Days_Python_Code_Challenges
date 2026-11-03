#Practice Problem: Write a program that takes
#  a string and reverses it 
# (e.g., “Python” becomes “nohtyP”).

def reverse_str(text):
    return text[::-1]

rev = reverse_str("Python")

print(reverse_str("Python"))

#Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

def check_vowels(text):
    count = 0
    vol = "aeiou"
    for char in text.lower():
        if char in vol:
             count +=1
    
  
    return count

val = "Learning Python is fun!"
print(check_vowels(val))