class Circle:
    """
    It is a class representing a circle.

    Attributes
    -----------
    - rad: int or float, Radius of the circle.

        Class Attributes
    ----------------
    - pi: mathematic constant, used to count the area of the circle
    - all_circles: list of all appended elements.

    Methods
    --------
    - area(): Returns the area of the circle.
    - total_area(): Returns the total area of all circles created.
    - __str__(): Returns the string representation of the circle.
    - __repr__(): Returns the string representation of the circle for interactive presentation.
    """

    pi = 3.1415
    all_circles = []

    def __init__(self, rad=1):
        self.rad = rad
        Circle.all_circles.append(self)

    def area(self):
        """
        Returns the area of the circle.
        """
        return (self.rad ** 2) * Circle.pi

    @staticmethod
    def total_area():
        """
        Returns the total area of all circles.
        """
        total = 0
        for el in Circle.all_circles:
            total += el.area()
        return total

    def __str__(self):
        return str(self.rad)

    def __repr__(self):
        return self.__str__()


c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))
