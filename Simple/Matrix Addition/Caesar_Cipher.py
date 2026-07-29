text = input("Enter message: ")
shift = int(input("Enter shift value: "))

result = ""

for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        shifted = (ord(char) - start + shift) % 26 + start
        result += chr(shifted)
    else:
        result += char

print("Encrypted message:", result)