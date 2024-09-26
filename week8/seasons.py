from datetime import date
import re
import sys
import inflect

def main():
    birthday = input('Birthday: ')
    birthday = check_date(birthday)
    min_age = age_calculator(birthday)
    print(convertor(min_age))

def check_date(date):
    match = re.search(r'\d\d\d\d-\d\d-\d\d',date)
    if match:
        return date
    else:
        sys.exit('Invalid format')
    
def age_calculator(birthday):
    birthday = date.fromisoformat(birthday)
    today = date.today()
    age = date.__sub__(today, birthday)
    min_age = age.days * 24 * 60
    return min_age
    
def convertor(minute):
    p = inflect.engine()
    words = p.number_to_words(minute)
    age_in_words = re.sub(' and', '', words)
    age_in_words = age_in_words.capitalize()
    return f"{age_in_words} minutes"

if __name__ == "__main__":
    main()