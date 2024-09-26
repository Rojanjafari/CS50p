from random import choice

while True:
    try:
        n = int(input('Level: '))
        if n <= 0:
            raise ValueError
        
        num_set = []
        for i in range(1, n+1):
            num_set.append(i)
        random_num = choice(num_set)

        guess = int(input('Guess: '))
        if n <= 0:
            raise ValueError
        
        if guess < random_num:
            print('Too small!')
        elif guess > random_num:
            print('Too large!')
        elif guess == random_num:
            print('Just right!')
            break

    except ValueError:
        pass