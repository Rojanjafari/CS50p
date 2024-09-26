while True:
    try:
        fraction = input('Enter the amount: ')
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        fuel = x / y
        if fuel > 1:
            raise ValueError
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break

if (fuel * 100) <= 1:
    print('E')
elif 99 <= (fuel * 100) <=100 :
    print('F')
else:
    print(f"{round(fuel * 100)}%")


