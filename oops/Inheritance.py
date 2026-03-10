class SuperUser: # Parent
    # Constructor
    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email

    def post_status(self, status):
        print(f'{self.user_name} posted: {status}.')

    @staticmethod # Decorator
    def validate_mail(email):
        return "@" in email and len(email) > 3

class SubUser(SuperUser): # Child
    def __init__(self, user_name, email, avatar):
        super().__init__(user_name, email)
        self.avatar = avatar

    def post_announcement(self, message):
        print(f'Site Announcement from {self.user_name}: {message}')


def main():
    super_user_one = SuperUser('Leo', 'leo@ninja.com')
    super_user_two = SuperUser('Ralph', 'ralph@ninja.com')
    sub_user = SubUser('Splinter', 'splinter@ninja.com', 'Splinter.jpeg')
    sub_user.post_announcement('Here is some News!')
    print(SuperUser.validate_mail('leo@ninja.com'))
    print(SubUser.validate_mail('ralphninja.com'))

if __name__ == '__main__':
    main()