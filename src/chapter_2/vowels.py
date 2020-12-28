vowels = ['a', 'e', 'i', 'o', 'u']
found = []

word = input("Enter a word: ")

for letter in vowels:
    if letter in word:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)
