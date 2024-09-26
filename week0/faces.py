def convert(x):     
    x = x.replace(':)', '🙂')
    x = x.replace(':(', '🙁')
    return(x)

    
def main():
    x = input()
    print(convert(x))

main()
