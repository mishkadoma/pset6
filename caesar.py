from sys import argv

first, second = argv

if len(argv) != 2:
    print("Error! Usage: python caesar.py <key>")
    
key = int(second)

def alphabet():
    character = 'a'
    alphabet1 = []
    for i in range(26):
        alphabet1.append(character);
        character = chr(ord(character) + 1)
    return alphabet1


def to_cipher(plaintext, key):
    alphabet1 = alphabet()
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                print(alphabet1[(ord(plaintext[i]) - ord('A') + key) % 26].upper(), end = '')
            else:
                print(alphabet1[(ord(plaintext[i]) - ord('a') + key) % 26], end = '')
        else:
            print(plaintext[i], end = '')
    print()


    

print("plaintext: ", end = "")
plaintext = input("> ")

print("ciphertext: ", end = "")
to_cipher(plaintext, key)



