class SimpleEnigma:
    def __init__(self, rotor1, rotor2, rotor3, reflector):
        # Adjustment of rotors and reflectors
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, message):
        encrypted_message = ''
        for char in message.upper():
            if char in self.alphabet:
                # Step 1: Cross the rotors
                char = self.rotor1[self.alphabet.index(char)]
                char = self.rotor2[self.alphabet.index(char)]
                char = self.rotor3[self.alphabet.index(char)]
                
                # Step 2: Reflection from the reflector
                char = self.reflector[self.alphabet.index(char)]
                
                # Step 3: Reverse pass through the rotors
                char = self.alphabet[self.rotor3.index(char)]
                char = self.alphabet[self.rotor2.index(char)]
                char = self.alphabet[self.rotor1.index(char)]
                
                encrypted_message += char
            else:
                # If the character is outside the alphabet, return the same
                encrypted_message += char

        return encrypted_message

# Adjusting rotors and reflectors (simple example)
rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

# An example of an Enigma machine
enigma = SimpleEnigma(rotor1, rotor2, rotor3, reflector)

# Receive messages from the user
message = input("Enter a message to encrypt: ")
encrypted_message = enigma.encrypt(message)
print("Encrypted message:", encrypted_message)
