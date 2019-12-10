class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
   
    @property
    def name(self):
        """
        Возвращаем полное имя
        """
        return "%s %s" % (self.first_name, self.last_name)


# person = Person("Mike", "Driscoll")
# print(person.full_name) # Mike Driscoll
# print(person.first_name) # Mike
# person.name = "Jackalope"

# person.first_name = "Dan"
# print(person.name) # Dan Driscoll


