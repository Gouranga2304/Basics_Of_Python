import string

text = input("Enter a sentence: ")

text = text.lower()

clean_text = ""
for char in text:
    if char not in string.punctuation:
        clean_text += char

print(clean_text)

words = clean_text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)