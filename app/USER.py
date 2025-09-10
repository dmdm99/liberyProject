


class USER(object):

# create a new object
    def __init__(self, First_Name:str, Last_Name:str, address:str, email:str, Phone_Number:str, Password:str != None):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.address = address
        self.email = email
        self.Phone_Number = Phone_Number
        self.Password = Password

    def get_user_info(self):
        return self.__init__()

    def get_username(self):
        return self.First_Name

    def get_last_name(self):
        return self.Last_Name

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def get_user_phone(self):
        return self.Phone_Number

    def get_user_password(self):
        return self.Password

    def set_username(self, username):
        self.First_Name = username

    def set_last_name(self, last_name):
        self.Last_Name = last_name

    def set_address(self, address):
        self.address = address

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        if password != None and len(password) >= 8:
            self.Password = password










