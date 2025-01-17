# Caesar-Cipher
# **Caesar Cipher Program**

This Python program implements a simple **Caesar cipher** for encrypting or decrypting messages. The Caesar cipher is a basic encryption technique that shifts letters by a specified number of positions in the alphabet.

---

## **Features**
1. 🔒 **Encrypt Messages**: Shifts letters forward in the alphabet to encrypt a message.
2. 🔓 **Decrypt Messages**: Shifts letters backward to restore the original message.
3. ✨ **Non-Alphabet Character Handling**: Retains spaces, numbers, and punctuation without modification.
4. 🔁 **Repeatable Usage**: Allows users to repeatedly encrypt or decrypt messages until they choose to exit.

---

## **How It Works**
1. The user specifies whether they want to **encode** (encrypt) or **decode** (decrypt) a message.
2. A shift value (integer) is entered to determine how many positions each letter should be moved.
3. The program applies the Caesar cipher logic to transform the message while preserving non-alphabetical characters.
4. The user can continue or exit after each operation.

---

## **Notes**
1. 🚀 **Modulo Operation**: The shift value is applied modulo 26 to ensure it wraps around the alphabet correctly.
2. ⚠️ **Input Validation**: If the user enters an invalid option (not "encode" or "decode"), the program prompts for a correct response.
3. ✍️ **Character Preservation**: Non-alphabetical characters like spaces, numbers, and punctuation are not affected by the shift.

---
