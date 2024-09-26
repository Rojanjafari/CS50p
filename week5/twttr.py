def main():
    text = input('Enter the text: ')
    print(shorten(text))

def shorten(word):
    vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U']
    for i in word:
        if i in vowels:
            word = word.replace(i, '')
    return word

if __name__ == "__main__":
    main()