"""
CryptAMessage Module

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '{', '}', '[', ']', ' ','?','a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '{', '}', '[', ']', ' ','?']

class CryptAMessage:
    def __init__(self):
        self.run()

    def ceasar(self, start_text, shift_amount, cipher_direction):
        end_text = ""
        new_position = 0
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here's the {cipher_direction}d result: {end_text}")

    def run(self):
        should_end = False
        while not should_end:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))

            if shift > len(alphabet):
                shift = shift % len(alphabet)
            self.ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
            choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
            if choice == 'no':
                should_end = True
                print("Goodbye")

