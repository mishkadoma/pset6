from sys import argv

first, second = argv


print("Enter text to cipher: ")
text = input("> ")
for i in text:
    i += second
print(text)
