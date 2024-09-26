def main():
    fraction = input('Enter the amount: ')
    print(gauge(convert(fraction)))


def convert(fraction):
    try:
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
        return round(fuel * 100)
    
def gauge(percentage):
    if (percentage) <= 1:
            return 'E'
    elif 99 <= (percentage) <=100 :
        return 'F'
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()  