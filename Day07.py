# Write a program that calculates 
# the factorial of a given number
#  (e.g., 5!) using a for loop.

print("Enter a Number to find fact")
num = int(input())

fact = 1
for i in range(1,num+1):
    fact = i  * fact
    print(i)

print(f"Factorial of {num}: {fact}")