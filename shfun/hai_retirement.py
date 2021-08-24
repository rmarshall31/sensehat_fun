#!/usr/bin/env python3
import datetime

from sense_hat import SenseHat


class General:

    def __init__(self):
        self.retirement_date = datetime.date(2026, 7, 1)
        self.sense = SenseHat()
        self.sense.set_rotation(0)
        self.sense.clear()

    def days_to_retirement(self):
        total_days_left = self.retirement_date - datetime.date.today()
        years_left = int(total_days_left.days / 360)
        weeks_left = int((total_days_left.days - (years_left * 360)) / 7)
        days_left = int(total_days_left.days - (years_left * 360) - (weeks_left * 7))
        message = f'{years_left} years, {weeks_left} weeks, {days_left} days until Hai retires'
        print(message)
        self.sense.show_message(message, text_colour=[150, 150, 150], scroll_speed=0.1)
        self.sense.clear()


if __name__ == '__main__':
    GENERAL = General()
    GENERAL.days_to_retirement()
