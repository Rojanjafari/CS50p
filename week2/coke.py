due = 50
coin = input('Insert Coin: ')
if int(coin) == 5 or int(coin) == 10 or int(coin) == 25:
    due -= int(coin)
    print(f"Amount Due: {due}")
else:
    print(f"Amount Due: {due}")

while due > 0:
    coin = input()
    if int(coin) == 5 or int(coin) == 10 or int(coin) == 25:
        due -= int(coin)
        if due > 0:
            print(f"Amount Due: {due}")
        else:
            change = 0 - due
            print(f"Change Owed: {change}")
    else:
        if due >= 0:
            print(f"Amount Due: {due}")
        else:
            print(f"Amount Due: {0}")


