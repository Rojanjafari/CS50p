def calculator(x, y, z):
    if y == '+':
        return float(int(x) + int(z))
    elif y == '-':
        return float(int(x) - int(z))
    elif y == '*':
        return float(int(x) * int(z))
    elif y == '/':
        return float(int(x) / int(z))


elements = input('Enter number: ')
x, y, z = elements.split()
print(calculator(x, y, z))


