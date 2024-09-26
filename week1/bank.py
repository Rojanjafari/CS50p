def greeting(x):
    items = x.split()
    start = items[0]
    letter = list(start)

    if items[0] == 'hello' or items[0] == 'hello,':
        return 0
    elif letter[0] == 'h':
        return 20
    else:
        return 100

def main(greetings):
    greetings = greetings.lower()
    dollar = greeting(greetings)
    print(f"${dollar}")

x = input()
main(x)