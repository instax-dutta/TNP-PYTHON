#write a program to check wether the given alphabet is vowel or consonant
input_char = input("Enter a character: ")
input_char = input_char.lower()

if input_char.isalpha():
    vowels = {"a", "e", "i", "o", "u"}
    if input_char in vowels:
        print(input_char, "is a vowel")
    else:
        print(input_char, "is a consonant")
else:
    print("Not an alphabet")
    
