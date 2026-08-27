import random

class Sensor:
    def __init__(self , name , min_value , max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = None

    def generate_value(self):
        range_width = self.max_value - self.min_value ## calculates the range
        margin = range_width * 0.10 # places a constant margin for every calculation
        self.current_value = max(0, random.uniform(self.min_value - margin, self.max_value + margin)) # this is for updating the current value
        return self.current_value

    def is_healthy(self):
        if self.min_value <= self.current_value <= self.max_value: # hena byechck law el current value fy el range wala la2
            return True
        else:
            return False



cpu = Sensor("CPU", 0, 90) # dol el values el min w el max lel CPU
voltage = Sensor("Voltage", 4.75, 5.25) # dol el values el min w el max lel Voltage
temperature = Sensor("Temperature", 0, 80) # dol el values el min w el max lel Tempreture
