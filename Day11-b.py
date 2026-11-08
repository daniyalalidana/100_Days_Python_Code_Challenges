"""
Exercise 17. Merging Lists with Parity Filtering
Practice Problem: Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

Given Input:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output: [25, 35, 40, 60, 90]
"""

def merge_list(list1, list2):
    list3 = []
    for no1, no2 in zip(list1, list2):
        if no1 %2 != 0:
            list3.append(no1)
        if no2 %2 == 0:
            list3.append(no2)
    return list3

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list = merge_list(list1,list2)
list.sort()
print(list)

