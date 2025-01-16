import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar():
    print(art.logo)
    check = "yes"
    while check == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        new_word = ""
        for i in text:
            if  i not in  alphabet:
                new_word +=i
            else:
                if direction=="encode" or direction=="decode":
                        c = alphabet.index(i)
                        if direction=="encode":
                            word_to_added=alphabet[(c+shift)%26]
                            new_word+=word_to_added
                        elif direction=="decode":
                            word_to_add = alphabet[(c - shift) % 26]
                            new_word += word_to_add
                else:
                    print("Enter the correct word!!")
        print(f"Here is the {direction}ed word:{new_word}")
        end_answer = input("Type 'Yes' if you want to go again. Otherwise, type 'No'.\n").lower()
        check = end_answer
    print("That's It Thank You for using IT.")
caesar()
