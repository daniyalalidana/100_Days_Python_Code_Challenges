"""
Exercise 16. Numerical Palindrome Check
Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

Exercise Purpose: This exercise introduces the idea of “Reversing Logic.” Reversing a string is simple, but reversing an integer takes some math, like using division and modulo, or changing its type. This shows how data types can work differently.

Given Input:

Case 1: number = 121
Case 2: number = 125

"""

def is_plindrome( number):
    no = str(number)
    if no[::-1] == str(number):
        return True
    else:
        False
no = 1
while(no != 0):
    no = int(input("Enter a number to check plindrome(0- exit): "))
    if is_plindrome(no):
        print(f"{no} is a Plindrome")
    else:
        print(f"{no} is not Plindrome")
    if no ==0:
        print("Good Bye")