text = input('Enter the text: ')
vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U']
for i in text:
    if i in vowels:
        text = text.replace(i, '')

print(text)