import sys
from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def template_method(self):
        """Template method contains a collection of methods to stay the same, 
        to be overriden, and to be overriden optionally"""
        self.__always_do_this()
        self.do_step_1()
        self.do_step_2()
        self.do_this_or()

    def __always_do_this(self):
        # protected method that should not be overriden
        name = sys._getframe().f_code.co_name
        print(f"{self.__class__.__name__}.{name}")

    @abstractmethod
    def do_step_1(self):
        # this method should be overriden
        ...

    @abstractmethod
    def do_step_2(self):
        ...

    def do_this_or(self):
        print("This method can be overriden but doesn't have to...")


class ConcreteClassA(AbstractClass):
    def do_step_1(self):
        print("Doing step 1 for ConcreteClassA...")

    def do_step_2(self):
        print("Doing step 2 for ConcreteClassA...")


class ConcreteClassB(AbstractClass):
    def do_step_1(self):
        print("Doing step 1 for ConcreteClassB...")

    def do_step_2(self):
        print("Doing step 2 for ConcreteClassB...")

    def do_this_or(self):
        print("Overriden optional method doing something new...")


print("===ConcreteClassA===")
a = ConcreteClassA()
a.template_method()
print("===ConcreteClassB===")
b = ConcreteClassB()
b.template_method()
