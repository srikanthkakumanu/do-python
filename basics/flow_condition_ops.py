# if elif else
def calculate_benefits(age = 10):
    if age < 18:
        print("You are not eligible for benefits.")
    elif 18 <= age < 60:
        print("You are eligible for benefits.")
    else:
        print("You are not eligible for benefits.")

# Single-line if statement
def check_legal_status(age = 10): # 10 is default value if no value is passed
    legal_status = 'Adult' if age >= 18 else 'Child'
    return legal_status

# while loop
def find_matching_number(num = 10):
    matching_num = 0
    while num <= 60:
        if matching_num == num:
            print("matching number found", matching_num)
            break
        matching_num += 1

# Boolean values
def check_truthy_falsy(value = True):
    """
    Truthy, Falsy: Automatic conversion to boolean
    Empty container, string without letters and 0 are Falsy
    Everything else is Truthy.

    Any non-zero number is truthy
    Any zero number is falsy
    Any non-empty string is truthy
    Any empty string is falsy
    """

    if value:
        print("Value is truthy")
    else:
        print("Value is falsy")


def main():
    # if
    calculate_benefits(18)
    calculate_benefits(60)
    calculate_benefits(65)
    calculate_benefits()

    # single-line if statement
    print('User is: ', check_legal_status(11))

    # while
    find_matching_number(10)
    find_matching_number(20)
    find_matching_number(30)
    find_matching_number()

    # boolean and Truthy and Falsy
    check_truthy_falsy(1) # Truthy
    check_truthy_falsy(0) # Falsy
    check_truthy_falsy("hello") # Truthy
    check_truthy_falsy("") # Falsy
    check_truthy_falsy(None) # Falsy
    check_truthy_falsy(True) # Truthy
    check_truthy_falsy(False) # Falsy
    check_truthy_falsy()

if __name__ == "__main__":
    main()