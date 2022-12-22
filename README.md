samogloski = ['a', 'e', 'y', 'i', 'o', 'ą', 'ę', 'u', 'ó']
words = open("slowa.txt", "r")
words = words.read()
samogloski_counter = 0

word_input = input('podaj slowo: ')

if word_input == 'exit':
    exit()
word_length = len(word_input)
word_split = list(word_input)
for letter in word_split:
    if letter in samogloski:
        samogloski_counter += 1

spulgloski_counter = word_length - samogloski_counter
substring_count = words.count(word_input)

if word_input in words:
    print("to jest slowo ")
    print(f'dlugosc slowa to: {word_length}')
    print(f'ilosc samoglosek to: {samogloski_counter}')
    print(f'ilosc samoglosek to: {spulgloski_counter}')
    print(f'wystapil jako podciag: {substring_count}')
else:
    print('to nie jest slowo! ')
