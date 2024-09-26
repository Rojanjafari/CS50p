from validator_collection import checkers

email_add = input('Email: ')
email_val = checkers.is_email(email_add)
if email_val:
    print('Valid')
else:
    print('Invalid')