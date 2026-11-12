'''
Practice Problem: Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.

Exercise Purpose: This exercise introduces “Metadata Extraction.” Often, you aren’t just interested in the data itself, but in its properties. In web development, this logic is used to validate if a user’s password or username meets specific length requirements.

Given Input: words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]


'''

words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
count =0
for fruits in words:
    for char in fruits:
        count +=1
    print(f"{fruits} - {count}")
    count = 0

