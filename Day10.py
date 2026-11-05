#Practice Problem: Print the following pattern where each 
# row contains a number repeated a specific number of times based on its value.

for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()