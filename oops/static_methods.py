class User:
    # Constructor
    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email

    def post_status(self, status):
        print(f'{self.user_name} posted: {status}.')

    @staticmethod # Decorator
    def validate_mail(email):
        return "@" in email and len(email) > 3

def main():
    user_one = User('Leo', 'leo@ninja.com')
    user_two = User('Ralph', 'ralph@ninja.com')

    print(User.validate_mail('leo@ninja.com'))
    print(User.validate_mail('ralphninja.com'))

if __name__ == '__main__':
    main()