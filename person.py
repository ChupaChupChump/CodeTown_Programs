class Person:
    # TODO: Implement this class properly
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        pass

    def get_name(self):
        name = self.name
        return name

    def get_age(self):
        age = self.age
        return age

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def is_older_than(self, other):
        if self.age > other.age:
            return True
        else:
            return False
    
alice = Person("Alice", 18)
bob = Person("Bob", 19)
if bob.is_older_than(alice):
    print("{0} is older than {1}".format(bob.get_name(), alice.get_name()))
else:
    print("{0} is older than {1}".format(alice.get_name(), bob.get_name()))