txt = "Coding is the language of the future"

with open('sample.txt', 'w+') as file:
    file.write(txt)


with open('sample.txt', 'r') as file:
    txt = file.read()
    print(txt)
    