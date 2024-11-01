class Subject:
    # represents what is being 'observed'

    def __init__(self):
        self._observers = []
        # this where references to all the observers are being kept
        # one-to-many relationship

    def attach(self, observer):
        # if observer is not already in the observers list append it to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # for all the observers in the list
        for observer in self._observers:
            # don't notify the observer who is actually updating the temperature
            if modifier != observer:
                # alert the observers
                observer.update(self)


class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # set the name of the core
        self._temp = 0  # initialize the temperature of the core

    @property  # getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        # notify the observers whenever somebody changes the core temperature
        self.notify()


class TempViewer:

    def __init__(self, name):
        self._name = name

    def update(self, subject):
        # alert method that is invoked when the notify() method in a concrete subject is invoked
        print(
            f"{self._name}: {subject._name} has Temperature {subject._temp}")


# create subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# create observers
v1 = TempViewer("TempViewer 1")
v2 = TempViewer("TempViewer 2")

# attach observers to the first core
c1.attach(v1)
c1.attach(v2)

# change the temperature of first core
c1.temp = 80
c1.temp = 90
