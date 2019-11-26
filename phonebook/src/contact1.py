class Contact:
    def __init__(self, name, phone, mobile, address):
        self.name = name
        self.mobile = mobile
        self.phone = phone
        self.address = address

    
    def __repr__(self):
        return "Contact({}, {})".format(self.name, self.mobile)
    
    def __str__(self):
        return "({}, {})".format(self.name, self.mobile)
   
# Main
if __name__ == '__main__':
    contact = Contact("Tim", '1123', '2222', 'test')
    print(contact)
    print("contact = {}".format(contact))
   
   