class Russian:
    """Russian speaker"""

    def __init__(self):
        self.name = "Russian"

    def speak_russian(self):
        return "Privet!"


class British:
    """English speaker"""

    def __init__(self):
        self.name = "English"

    def speak_english(self):
        return "Hello!"


class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapter_method):
        """Change the name of the method"""
        self._object = object
        # add a new dictionary item that establishes the mapping between a generic method name (speak)
        # and a concrete method name (speak_russian or speak_english)
        self.__dict__.update(**adapter_method)

    def __getattr__(self, attr):
        """Returns the rest of attributes"""
        return getattr(self._object, attr)


# list to store speaker objects
objects = []
# create objects
russian = Russian()
british = British()
# append objects to the objects list
objects.append(Adapter(russian, speak=russian.speak_russian))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print(f"{obj.name} says {obj.speak()}")
    # print(obj.__dict__)
