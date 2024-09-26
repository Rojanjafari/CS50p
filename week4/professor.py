import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for i in range(3):
            try:
                response = int(input(f"{x} + {y} = "))
                if response == (x + y):
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print('EEE')
                if i == 2:
                    print(x + y)
                pass
    print(score)

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    try:
        if level not in [1, 2, 3]:
            raise ValueError
        if level == 1:
            n = random.randint(0, 9)
        else:
            range_start = 10**(level-1)
            range_end = (10**level)-1
            n = random.randint(range_start, range_end)
        return n

    except ValueError:
        pass

if __name__ == "__main__":
    main()
