
class User:
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def get_email_address(self):
        return self.email_address

    def set_email_address(self, email_address):
        self.email_address = email_address

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
