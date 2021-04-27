class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.__pi * self.diameter
        return circumference

    def calculate_area(self):
        area = self.__pi * ((self.diameter / 2) ** 2)
        return area

    def calculate_area_of_sector(self, angle):
        area_of_sector = self.__pi * ((self.diameter / 2) ** 2) * (angle / 360)
        return area_of_sector
