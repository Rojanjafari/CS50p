import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r"src\=\"https?://(www\.)?youtube.com/embed/(\w+)\"", s , re.IGNORECASE)
    if match:
        new_url = f'https://youtu.be/{match.group(2)}'
        return new_url
    else:
        return None


if __name__ == "__main__":
    main()
