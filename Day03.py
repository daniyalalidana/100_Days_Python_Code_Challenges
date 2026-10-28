# Question
'''
Practice Problem: Iterate through the first 10 numbers (0–9). 
In each iteration, print the current number, the previous number, and their sum.
'''
prev = 0
for i in range(9):
    print(f"Current Number: {i}. Previous No: {prev }. Thier Sum: {i+prev}")
    prev = i
