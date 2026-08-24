from Rover import Rover
from Randomizer import randomizer
rover = Rover()
rover.mov(10, 90)
print(rover.x, rover.y)


def get_valid_angle():
    while True:
        angle = float(input("Enter angle (0-360): "))
        if 0 <= angle <= 360:
            return angle
        else:
            print("Invalid angle! Please enter a value between 0 and 360.")

def get_valid_distance():
    while True:
        distance = float(input("Enter distance (must be positive): "))
        if distance > 0:
            return distance
        else:
            print("Invalid distance! Please enter a positive value.")
