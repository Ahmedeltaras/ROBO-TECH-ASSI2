import pynput
from Health_monitor import health_monitor
from Sensors import Sensor
from Thrustercontroller import thrusterController
import time

cpu = Sensor("CPU", 0, 90)
voltage = Sensor("Voltage", 4.75, 5.25)
temperature = Sensor("Temperature", 0, 80)

cpu.generate_value()
voltage.generate_value()
temperature.generate_value()

monitor = health_monitor(cpu, temperature, voltage)
monitor.report()
print(monitor.check_all())

rov = thrusterController()
rov.move("up")
print(rov.thrusters)
rov.move("left")
print(rov.thrusters)
rov.stop_all()
print(rov.thrusters)

def handle_key_press(key, rov):
    if key == pynput.keyboard.Key.up:
        rov.move("up")
    elif key == pynput.keyboard.Key.down:
        rov.move("down")
    elif key == pynput.keyboard.Key.right:
        rov.move("right")
    elif key == pynput.keyboard.Key.left:
        rov.move("left")
    print(rov.thrusters)

listener = pynput.keyboard.Listener(on_press=lambda key: handle_key_press(key, rov))
listener.start()

#cpu.current_value = 999


while True:
    cpu.generate_value()
    voltage.generate_value()
    temperature.generate_value()
    if not monitor.check_all():
        rov.is_cooling_down = True
        rov.stop_all()
        print("the Rover is in a cool down !")
        time.sleep(5)
        rov.is_cooling_down = False
        print("Cooldown Ended :)")
    time.sleep(1)
