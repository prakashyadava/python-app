alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encode(text,shift):
    text = text.lower()
    encoded = ""
    for letter in text:
        if alphabets.count(letter) == 0:
            encoded += letter
        else:
            index_let = alphabets.index(letter)
            index_let = (index_let + shift) % 26
            encoded += alphabets[index_let]
    # print(index_let)
    print(f"Encoded result : {encoded}")

def decode(text,shift):
    text = text.lower()
    decoded = ""
    for letter in text:
        if alphabets.count(letter) == 0:
            decoded += letter
        else:
            index_let = alphabets.index(letter)
            index_let = (index_let + (26 - shift)) % 26
            decoded += alphabets[index_let]
    # print(index_let)
    print(f"Decoded result : {decoded}")


user = True
# print("Type 'encode' to encode or type 'decode' to decode : ")
while user:
    response = input("Type 'encode' to encode or type 'decode' to decode : ")
    if response == 'encode':
        message = input("Tye your message: ")
        shift = int(input("Enter the shift: "))
        encode(message,shift)
    else:
        message = input("Tye your message: ")
        shift = int(input("Enter the shift: "))
        decode(message, shift)

    try_again = input("Type 'yes' if you want to go again . Otherwise 'no' : ")
    if try_again=='yes':
        user = True
    elif try_again=='no':
        user = False