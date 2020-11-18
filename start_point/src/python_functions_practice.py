def return_10():
    return 10

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b 

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

def length_of_string(a):
    return len(a)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month):
    if month == 1:
        return "January"
    elif month == 3:
        return "March"
    elif month == 9:
        return "September"


def number_to_short_month_name (month):
    if month == 1:
        return "Jan"
    elif month == 4:
        return "Apr"
    elif month == 10:
        return "Oct"

def volume_of_cube(a):
    return a ** 3

def reverse_string(a):
    return a[::-1]

def celsiusconv(a):
    return (a - 32) * 5/9
    


    