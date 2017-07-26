while True:
    height = int(input('Enter the piramide height > '))
    if height >= 0:
        break

for i in range(0, height):

    indentation =  height - (i + 1)
    print(" " * indentation, end = "")
    for k in range(2):
        print("#" * (i + 2), end = "")
    print(" " * indentation)