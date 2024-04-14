class Circle:
    pi = 3.1415
    all_circles = []

    def __init__(self, rad=1):
        self.rad = rad
        Circle.all_circles.append(self)

    def area(self):
        return (self.rad ** 2) * Circle.pi

    @staticmethod
    def total_area():
        total = 0
        for el in Circle.all_circles:
            total += Circle.area(el)
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