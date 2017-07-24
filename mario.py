height = int(input('Enter the piramide height > '))

for i in range(0, height):
    indentation =  height - (i + 1)
    print(" " * indentation, end = "")
    print("#" * (i + 2))
