class InvalidCustomerIdException(Exception):
    """customer_id -a number between 1000-9999"""
    pass

class InvalidNameException(Exception):
    """alpha characters only"""
    pass

class InvalidPhoneNumberFormat(Exception):
    """123-123-1234 format only"""
    pass

class Customer:
    """Customer class"""

    def __init__(self, cid, lname, fname, pnumber):  # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        customer_id_characters = set("1234567890")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise InvalidNameException
        if not phone_number_characters.issuperset(pnumber):
            raise InvalidPhoneNumberFormat
        if not customer_id_characters.issuperset(cid):
            raise InvalidCustomerIdException
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_phone_number(self, number):
        self.phone_number = number

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

#Driver code
# Valid customer
customer_one = Customer('123', 'Duck', 'Donald', '(555)555-5555') # all required
print(str(customer_one))

# Invalid phone
# Wait! try/except needed!
try:
    customer_two = Customer('123', 'Duck', 'Donald', '(555)555-5555P') # all required
except ValueError:
    print("Error found, customer not created")

# Invalid customer_id
# try/except needed
try:
    customer_two = Customer('ABC', 'Duck', 'Donald', '(555)555-5555') # all required
except ValueError:
    print("Error found, customer not created")

# Invalid first_name
# try/except needed!
try:
    customer_two = Customer('123', 'Duck', '2', '(555)555-5555') # all required
except ValueError:
    print("Error found, customer not created")