def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and char(s) and numPlace(s) and firstNum(s) and sign(s):
        return True
    else:
        return False

def char(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False

def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def numPlace(s):
    if s.isalpha():
        return True
    else:
        for i in range(len(s)):
            if s[i].isnumeric():
                j = i
        
        for i in range(len(s)):
            if s[i].isalpha():
                k = i

        if(k > j):
            return False
        else:
            n = 0
            for i in range(0,k):
                if s[i].isnumeric():
                    n += 1
            if n == 0:
                return True
            else:
                return False
        
def firstNum(s):
    if s.isalpha():
        return True
    else:
        for i in range(len(s)):
            if s[i].isnumeric():
                j = i
                break
            
        if s[j] == '0':
            return False
        else:
            return True

def sign(s):
    if s.find('.') != -1 or s.find(' ') != -1:
        return False
    else:
        return True

    
main()