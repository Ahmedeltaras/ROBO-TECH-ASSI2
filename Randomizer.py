import random
from Constants import MIN_ANGLE, MAX_ANGLE, MIN_DISTANCE, MAX_DISTANCE

class Randomizer:
    def __init__(self, min_angle_value, max_angle_value, min_distance_value, max_distance_value):
        if not (MIN_ANGLE <= min_angle_value <= max_angle_value <= MAX_ANGLE):
            raise ValueError("Invalid angle range")
        if not (MIN_DISTANCE < min_distance_value <= max_distance_value <= MAX_DISTANCE):
            raise ValueError("Invalid distance range")

        self.min_angle_value = min_angle_value
        self.max_angle_value = max_angle_value
        self.min_distance_value = min_distance_value
        self.max_distance_value = max_distance_value

    def generate(self):
        angle = random.uniform(self.min_angle_value, self.max_angle_value)
        distance = random.uniform(self.min_distance_value, self.max_distance_value)
        return distance, angle