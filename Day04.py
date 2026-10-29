'''
Practice Problem: Display only those characters which are present at an even index number in given string.
'''

def even_index(text ):
    even  = text[0::2]
    for char in even:
        print(char)

even_index("String Indexing and Even Slicing")
