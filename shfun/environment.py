#!/usr/bin/env python
from __future__ import division

import time

from sense_hat import SenseHat


class Environment:
    """Displays some environmental parameters
    Attributes:
        rotation    how is your pi oriented?
        speed       scroll speed to for the text display
        cycles      how many cycles to do (0 to run forever)
        correction  correction factor for the temp sensor
        color       default color used to display values
        elevation   elevation above sea level in feet
        warm        The temp for full red
        cold        The temp for full blue
    """

    def __init__(
            self,
            rotation=0,
            speed=0.1,
            cycles=0,
            correction=0.83,
            color = [150, 150, 150],
            elevation=970,
            cold=68,
            warm=77,
    ):
        self.color = color
        self.speed = speed
        self.cycles = cycles
        self.correction = correction
        self.elevation = elevation
        self.cold = cold
        self.warm = warm

        self.sense = SenseHat()
        self.sense.set_rotation(rotation)
        self.sense.clear()

    def set_color_from_temp(self):
        temp_range = self.warm - self.cold
        if temp_range < 0:
            raise ValueError("warm must be greater than cold!")

        temp = self.temperature
        if temp < self.cold:
            temp = self.cold
        elif temp > self.warm:
            temp = self.warm

        temp_percent = (temp - self.cold) / temp_range
        temp_color_value = int(round(255 * temp_percent))
        self.color = [temp_color_value, 0, 255 - temp_color_value]

    @property
    def temperature(self):
        return self.get_temperature()

    @property
    def temperature_string(self):
        return "{temperature}F".format(temperature=self.get_temperature())

    def get_temperature(self):
        temp = self.sense.get_temperature()
        temp_f = int(round(((temp * 1.8) + 32) * self.correction))
        return temp_f

    @property
    def pressure(self):
        return self.get_pressure()

    @property
    def pressure_string(self):
        return "{pressure}mb".format(pressure=self.get_pressure())

    def get_pressure(self):
        temp_kelvin = (self.temperature + 459.67) * (5 / 9)
        pressure = self.sense.get_pressure()
        elevation_factor = (self.elevation * 0.3048) * 0.0065
        adjusted_pressure = pressure * (1 - (elevation_factor / (temp_kelvin + elevation_factor))) ** -5.2561
        return int(round(adjusted_pressure))

    @property
    def humidity(self):
        return self.get_humidity()

    @property
    def humidity_string(self):
        return "{humidity}%".format(humidity=self.get_humidity())

    def get_humidity(self):
        return int(round(self.sense.get_humidity()))

    def display_environment(self, *args):
        """Displays some environmental parameters
        Attributes:
            args  may be a list or single parameter to display. Empty means display all parameters.
        """

        if len(args) == 0:
            args = ["temperature", "pressure", "humidity"]

        completed_cycles = 0
        while True:
            for param in args:
                prop = getattr(self, "{param}_string".format(param=param))
                self.sense.show_message("{param}".format(param=prop), text_colour=self.color, scroll_speed=self.speed)
                self.sense.clear()
                time.sleep(1)

            completed_cycles += 1
            if completed_cycles >= self.cycles != 0:
                break


if __name__ == "__main__":
    ENVIRONMENT = Environment()
    ENVIRONMENT.display_environment()
