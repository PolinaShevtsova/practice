alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
phrase = input("Введите строку: ")
new_phrase = ''

for letter in phrase:
    index_letter = alphabet.index(letter)
    new_index_letter = index_letter + 13
    if letter in alphabet:
        new_phrase += alphabet[new_index_letter]

print(new_phrase)
