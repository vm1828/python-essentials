class House:
    """The class being visited"""

    def accept(self, visitor):
        """interface to accept a visitor"""
        # triggers the visiting operation
        # for the visitor to be able to visit,
        # it needs a reference to an instance of the house class
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "work on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "work on by", electrician)

    def __str__(self):
        return self.__class__.__name__


class Visitor:
    """Abstract visitor"""

    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""

    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    """Concrete visitor: electrician"""

    def visit(self, house):
        house.work_on_electricity(self)


# create an HVAC specialist and electrician
hv = HvacSpecialist()
e = Electrician()

# create a house
home = House()

# let the house accept visitors and work on the house
home.accept(hv)
home.accept(e)
