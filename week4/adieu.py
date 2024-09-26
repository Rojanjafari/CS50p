import inflect

p = inflect.engine()
names = []
while True:
    try:
        name = input()
        names.append(name)
        bye = p.join(names)
        print(f"Adieu, adieu, to {bye}")
    except EOFError:
        break