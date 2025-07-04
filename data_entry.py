from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {'I':'Income', 'E':'Expense'}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)    # to give today's date in string format
    
    try:
        valid_date = datetime.strptime(date_str, date_format)    # checking if the entered date is in valid format
        return valid_date.strftime(date_format)    # returing the date in string format
    except ValueError:
        print("INVALID DATE FORMAT!! Enter date in dd-mm-yy.")
        return get_date(prompt, allow_default)    # to prompt again recursively to get date and return only the last correct response

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError ("Amount must be non-negative or non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income, 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("INVALID CATEGORY!! Please Enter 'I' for Income and 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")