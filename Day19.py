'''   
Exercise 21. Downward Half-Pyramid Pattern
Practice Problem: Print a downward half-pyramid pattern using stars (*).

Exercise Purpose: Learn about reverse indexing. Controlling loop boundaries in reverse is important for algorithms that process data from end to beginning.

Given Input: Rows: 5

Expected Output:

* * * * * 
* * * * 
* * * 
* * 
* 
'''
n = 10
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()