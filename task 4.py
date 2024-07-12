class Circle:
    def __init__(self, radii):
        self.__pi = 3.141  # private member variable
        self.radii = radii  # public member variable

    def area(self):
        areas = []
        for radius in self.radii:
            area = self.__pi * (radius ** 2)
            areas.append(area)
        return areas
    
    def perimeter(self):
        perimeters = []
        for radius in self.radii:
            perimeter = 2 * self.__pi * radius
            perimeters.append(perimeter)
        return perimeters

# Create a list of radii
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create a Circle object
circle = Circle(radii_list)

# Calculate areas and perimeters
areas = circle.area()
perimeters = circle.perimeter()

# Print the results
print("Areas:", areas)
print("Perimeters:", perimeters)
