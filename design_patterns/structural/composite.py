from abc import ABC, abstractmethod


class Component(ABC):
    """Abstract class"""

    @abstractmethod
    def __init__(self, *args, **kwargs):
        ...

    @abstractmethod
    def component_function(self):
        ...


class Child(Component):
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        # this is where we store the name of the child item
        self.name = args[0]

    def component_function(self):
        # print the name of the child item here!
        print(f"{self.name}")


class Composite(Component):
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        # this is where we store the name of the composite object
        self.name = args[0]
        # this is where we keep our child items
        self.children = []
        self.indentation = 1

    def append_child(self, child):
        """Add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Remove a child item"""
        self.children.remove(child)

    def component_function(self):
        # print the name of the component object
        print(f"{self.name}")
        # iterate through the child objects and invoke their component_function
        for i in self.children:
            print("\t"*self.indentation, end='')
            if isinstance(i, Composite):
                # increment indentation by 1 if there are nested composite objects
                i.indentation += 1
            i.component_function()


# build a composite submenu 1
sub1 = Composite("submenu1")
# create a new childs
sub11 = Child("sub_submenu 11")
sub12 = Child("sub_submenu 12")

# add sub_submenu 11 and 12 to submenu 1
sub1.append_child(sub11)
sub1.append_child(sub12)

# build a top-level composite menu
top = Composite("top_menu")

# build a submenu 2 that is not a composite
sub2 = Child("submenu2")

# add the composite submenu1 to the top-level composite menu
top.append_child(sub1)

# add the plain submenu2 to the top-level composite menu
top.append_child(sub2)

# invoke component_function of top-level composite menu object
top.component_function()
