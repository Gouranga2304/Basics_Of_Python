letter = input("Enter a letter: ").lower()

vowels = "aeiou"

if letter in vowels:
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")