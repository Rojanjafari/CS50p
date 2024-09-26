import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try :
        decimals =  re.split(r"\.", ip)
        if len(decimals) != 4:
            raise ValueError

        n = 0
        for num in decimals:
            if 0 <= int(num) <= 255:
                n += 1

        if n == len(decimals):
            return True
        else:
            return False
    
    except ValueError:
        return False

if __name__ == "__main__":
    main()