class health_monitor:
    def __init__(self, cpu, temperature, voltage):
        self.cpu = cpu
        self.temperature = temperature
        self.voltage = voltage
        self.sensors = [self.cpu, self.temperature, self.voltage]

    def check_all(self): # dy check law kol 7aga fy range el tabi3y bta3ha wala la2
        for sensor in self.sensors:
            if not sensor.is_healthy():
                return False

        return True

    def report(self):
        for sensor in self.sensors:
            print(f"current sensor name :{sensor.name}")
            print(f"current sensor value:{sensor.current_value}")
            print(f"Sensor's health: {sensor.is_healthy()}")
