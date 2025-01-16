# Caesar-Cipher
This Python program implements a simple Caesar cipher that can encrypt or decrypt messages based on a user-specified shift value. The program supports both encoding (encryption) and decoding (decryption) of messages and allows the user to repeat the process multiple times.

#Features:

   Encrypt a message by shifting the letters forward in the alphabet.

   Decrypt a message by shifting the letters backward in the alphabet.

   Handles non-alphabetical characters gracefully, leaving them unchanged.

   Allows repeated use until the user decides to exit.

#Notes

1)The shift value is applied modulo 26 to ensure it stays within the bounds of the alphabet.

2)If the user enters an invalid option (not "encode" or "decode"), the program will prompt them to enter the correct word.

3)Non-alphabetical characters (e.g., spaces, numbers, punctuation) remain unchanged in the output.
