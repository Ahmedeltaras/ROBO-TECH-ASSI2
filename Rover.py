import math
from Constants import MIN_ANGLE, MAX_ANGLE, MIN_DISTANCE, MAX_DISTANCE

class Rover:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.path_x = [0.0]
        self.path_y = [0.0]

    def mov(self, distance, angle):
        if distance <= MIN_DISTANCE or distance > MAX_DISTANCE:
            raise ValueError(f"Distance must be greater than {MIN_DISTANCE} and no more than {MAX_DISTANCE}")
        if angle < MIN_ANGLE or angle > MAX_ANGLE:
            raise ValueError(f"Angle must be between {MIN_ANGLE} and {MAX_ANGLE}")

        angle_rad = math.radians(angle)
        self.x += distance * math.cos(angle_rad)
        self.y += distance * math.sin(angle_rad)
        self.path_x.append(self.x)
        self.path_y.append(self.y)

    def get_position(self):
        return self.x, self.y