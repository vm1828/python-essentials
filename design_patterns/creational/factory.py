class Animal:
    def __init__(self, name):
        self._name = name


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """The Factory Method"""
    pets = dict(dog=Dog("Rex"), cat=Cat("Lucy"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
