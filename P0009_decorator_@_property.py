#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
Sample 1
    @property
    def x(self):
        return self._x

    is equivalent to

    def getx(self):
        return self._x
    x = property(getx)

Sample 2
    @property
    def x(self): ...

    is the same as

    def x (self): ...
    x = property(x)

    and next step
    @x.setter
    def x(self, value): ...
"""

# Not use decorator
class Distance:
    def __init__(self, kilometer = 0):
        self.set_kilometer(kilometer)

    def to_mile(self):
        return (self.get_kilometer() * 0.621371)

    def get_kilometer(self):
        return self._kilometer

    def set_kilometer(self, value):
        self._kilometer = value

    kilometer = property(get_kilometer, set_kilometer)
    #kilometer = property()
    #kilometer = kilometer.getter(get_kilometer)
    #kilometer = kilometer.setter(set_kilometer)

# Use decorator
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature
        #self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
        #return (self.get_temperature() * 1.8) + 32

    @property
    #def get_temperature(self):
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


if __name__ == '__main__':
    c = Celsius()
    c.temperature = 40
    print(c.to_fahrenheit())

    d = Distance()
    d.set_kilometer(10)
    print(d.to_mile())
