import pickle

class Phonebook:

    def __init__(self, filename):

        self.filename = filename
        self.records = []
    
    def save(self, obj):
        with open(self.filename, 'ab') as f:
            pickle.dump(obj, f)

    def view(self):
        with open(self.filename, "rb") as f:
            try:
                while True:
                    self.records.append(pickle.load(f))
            except EOFError:
                pass
        return self.records
