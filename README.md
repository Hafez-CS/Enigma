# Enigma
![_3ea20d66-0f62-4889-b772-25e77c3d3a4c](https://github.com/user-attachments/assets/ec595bda-8102-4b28-8e53-a64df0cf75a5)

Setting up rotors and reflectors: We use a few simple strings to simulate rotors and reflectors.
Encryption and decryption stage:
* **The incoming message passes through three rotors in order.**
* **Then the reflection is done from the reflector.**
* **Then the reverse path is done from the rotors to return the message.**
* **From the same option for decryption and encryption. So decrypting the encrypted message returns the same original message.**

Tips:
This implementation is simple and tutorial and does not include the complexities and details of the actual Enigma machine.
In this implementation, the rotors are fixed and do not rotate. In real Enigma, the rotors spin with each input.
Use encryption algorithms for high security in real projects.

The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military. The Enigma machine was considered so secure that it was used to encipher the most top-secret messages.

The Enigma has an electromechanical rotor mechanism that scrambles the 26 letters of the alphabet. In typical use, one person enters text on the Enigma's keyboard and another person writes down which of the 26 lights above the keyboard illuminated at each key press. If plaintext is entered, the illuminated letters are the ciphertext. Entering ciphertext transforms it back into readable plaintext. The rotor mechanism changes the electrical connections between the keys and the lights with each keypress.

**enigma encrypt :**

```python
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
```

**enigma decrypt :**

```python
class SimpleEnigma:
    def __init__(self, rotor1, rotor2, rotor3, reflector):
        # Adjustment of rotors and reflectors
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def decrypt(self, message):
        # It is the same function as encryption code
        return self.encrypt(message)

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

# Setting the rotors and reflectors (must be the same as the encryption settings)
rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

# An example of an Enigma machine
enigma = SimpleEnigma(rotor1, rotor2, rotor3, reflector)

# Receive an encrypted message from the user
encrypted_message = input("Enter an encrypted message to decrypt: ")
decrypted_message = enigma.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)

```
