'''Practice Problem:
Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000,
return their product; otherwise, return their sum. '''

num1 = 90
num2 = 98

if num1 * num2 > 1000:
    print("Product is: ", num1*num2)
else:
    print("Sum of Two number is: ", num1 + num2)