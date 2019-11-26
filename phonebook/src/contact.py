import json
class Contact:
    def __init__(self, name, phone, mobile, address):
        self.name = name
        self.mobile = mobile
        self.phone = phone
        self.address = address

    def toJson(self):
        '''
        Serialize the object custom object
        '''
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)