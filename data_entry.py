from datetime import datetime

def get_date (prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and date_str == "":
        return datetime.today().strftime("%d/%m/%Y")
    try:
        valid_date = datetime.strptime(date_str, "%d/%m/%Y")
        return valid_date.strftime("%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please enter the date in the format dd/mm/yyyy")
        return get_date(prompt, allow_default)

def get_amount(prompt):
    pass

def get_category(prompt):
    pass

def get_description(prompt):
    pass
 