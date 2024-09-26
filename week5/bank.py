def value(greeting):
    items = greeting.lower().split()
    start = items[0]
    letter = list(start)

    if items[0] == 'hello' or items[0] == 'hello,':
        return 0
    elif letter[0] == 'h':
        return 20
    else:
        return 100

def main():
    greeting = input()
    dollar = value(greeting)
    print(f"${dollar}")

if __name__ == "__main__":
    main()