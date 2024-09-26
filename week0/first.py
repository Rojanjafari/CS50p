x = 1
y = 5
score = 0
print(f"{x} + {y} = ")
for i in range(3):
    try:
        response = int(input())
        if response == (x + y):
            score += 1
        else:
            raise ValueError
    except ValueError:
        if i == 2:
            print(x + y)