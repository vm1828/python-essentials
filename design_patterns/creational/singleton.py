class Borg:
    """The Borg design pattern"""

    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make an attribute dictionary


class Singleton(Borg):
    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_data.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_data)


# Create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

# Create another singleton object and check if it refers
# to the same attribute dictionary by adding another acronym

y = Singleton(SNMP="Simple Network Management Protocol")
print(y)
