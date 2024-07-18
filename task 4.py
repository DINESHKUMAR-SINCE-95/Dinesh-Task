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




#4..Sure, let's start with Part A: creating the `TV` class as described.


class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 0  # You can initialize this as needed
        self.inches = 0  # You can initialize this as needed
        self.on = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        self._display_status()

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        self._display_status()

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
        self._display_status()

    def reset(self):
        self.channel = 1
        self.volume = 50
        self.on = False
        self._display_status()

    def _display_status(self):
        print(f"{self.brand} at channel {self.channel}, volume {self.volume}")

# Example usage:
tv = TV("Panasonic")
tv.increase_volume()  # Increases volume to 51
tv.decrease_volume()  # Decreases volume to 50
tv.set_channel(8)  # Sets channel to 8
tv.reset()  # Resets TV to default settings


#Now, for Part B, let's create `LedTV` and `PlasmaTV` classes inheriting from `TV`, and add additional properties and methods specific to each type of TV.


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        print(f"{self.brand} LED TV: Screen thickness {self.screen_thickness}, Energy usage {self.energy_usage}, Lifespan {self.lifespan}, Refresh rate {self.refresh_rate}")

class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        print(f"{self.brand} Plasma TV: Screen thickness {self.screen_thickness}, Energy usage {self.energy_usage}, Lifespan {self.lifespan}, Refresh rate {self.refresh_rate}, Viewing angle {self.viewing_angle}, Backlight {self.backlight}")

# Example usage:
led_tv = LedTV("Sony", "Thin", "Medium", "Long", "120Hz")
led_tv.display_details()

plasma_tv = PlasmaTV("Samsung", "Thick", "High", "Medium", "60Hz", "Wide", "Yes")
plasma_tv.display_details()
```

#These classes demonstrate inheritance where `LedTV` and `PlasmaTV` inherit properties and methods from `TV` while adding their specific attributes and methods (`display_details` in this case).

# Print the results
print("Areas:", areas)
print("Perimeters:", perimeters)
