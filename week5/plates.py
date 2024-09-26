def is_valid(s):
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha() and s.find('.') == -1 and s.find(' ') == -1 and s.isalnum():
        for i in s:
            if i.isdigit():
                index = s.index(i)
                if s[index:].isdigit() and i != '0':
                    return True
                else:
                    return False


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()