def main():
    t = input("Enter time: ")
    time = convert(t)
    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('launch time')
    elif 18 <= time <= 19:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + (int(minutes) / 60)


if __name__ == "__main__":
    main()


