from InvalidInputError import InvalidInputError
from SimpleError import SimpleError

def simple():
    try:
        number = int(input('Enter a number: '))
        print('You entered: ', number)
    except:
        print('That is not a number!')
    finally:
        print('Thank you for your time!')

def with_error_type():
    try:
        number = int(input('Enter a number: '))
        print('You entered: ', number)
    except ValueError as e:
        print('That is not a number!')
        print('Error occurred: ', e.__str__())
    finally:
        print('Thank you for your time!')

    # Zero Division Error
    try:
        print('Let\'s\' Zero Division example')
        a = int(input('Enter A value: '))
        b = int(input('Enter B value: '))
        print('Division Result: ', a/b)
    except ZeroDivisionError as e:
        print('cannot divide a number by zero!')
        print('Error occurred: ', e)
    finally:
        print('Thank you for your time!')

# Custom Error Handling
def raise_custom_simple_error():
    raise SimpleError('Simple Custom Error Raised')

def raise_custom_invalid_input_error():
    number = int(input('Enter 10 to raise the InvalidInputError: '))
    if number == 10:
        raise InvalidInputError('10', 'number is not permitted')

def handle_custom_errors():
    try:
        raise_custom_simple_error()
    except SimpleError as e:
        print('Custom Error: ', e)

    print('SimpleError is handled')

    try:
        raise_custom_invalid_input_error()
    except InvalidInputError as e:
        print('Custom InvalidInputError has Occurred: ', e.expression, e.message)

    print('InvalidInputError is handled')


def handle_multiple_exceptions():
    try:
        number = int(input('Enter a number: '))
        print('You entered: ', number)
    except (ValueError, TypeError) as e:
        print('That is not a valid input!')
        print('Error occurred: ', e)
    finally:
        print('Thank you for your time!')


def handle_try_except_finally_else():
    try:
        number = int(input('Enter a number: '))
        if number < 0:
            raise ValueError('Number cannot be negative')
        else:
            print('You entered a positive number: ', number)
    except ValueError as e:
        print('Error occurred: ', e)
    else:
        print('No error occurred')
    finally:
        print('Thank you for your time!')


def main():
    # simple()
    # with_error_type()
    # handle_multiple_exceptions()
    handle_custom_errors()

if __name__ == '__main__':
    main()