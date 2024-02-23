alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_active = True

def caesar(c_text, c_shift, c_direction):
    caesar_text = ''

    for letter in c_text:
        index = alphabet.index(letter)
        if c_direction == 'encode':
            if index + shift > 25:
                caesar_text += alphabet[(index + c_shift) - 26]
            else:
                caesar_text += alphabet[index + c_shift]
        else:
            if index + shift < 0:
                caesar_text += alphabet[26 - (index - c_shift)]
            else:
                caesar_text += alphabet[index - c_shift]

    print(f'The {c_direction}d text is {caesar_text}')

from art import logo
print(logo)

while is_active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode':
        if direction != 'decode':
            print("Invalid input. Buh-bye!")
            break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(c_text=text, c_shift=shift, c_direction=direction)

    choice = input("Would you like to continue? Type 'y' for YES or 'n' for NO:\n").lower()

    if choice == 'n':
        is_active = False
