import json

class Phonebook:

    def __init__(self, filename):

        self.filename = filename
        self.records = []
    
    def load_data(self):
        with open(self.filename, "r") as f:
            self.records = json.load(f)
        return self.records

    def save(self, obj):
        with open(self.filename, 'w') as f:
            json.dump(obj, f)
