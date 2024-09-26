def main():
    x = input().strip().lower()
    return x

def check42(x):
    yes = 'Yes'
    no = 'No'
    if x == '42':
        return yes
    elif x == 'forty-two':
        return yes
    elif x == 'forty two':
        return yes
    else:
        return no

x = main()
check42(x)




