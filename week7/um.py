import re

def main():
    print(count(input("Text: ")))

def count(s):
    s = s.lower()
    match = re.findall(r'\bum\b', s)
    return len(match)

if __name__ == "__main__":
    main()