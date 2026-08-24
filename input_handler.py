from Constants import MIN_ANGLE, MAX_ANGLE, MIN_DISTANCE, MAX_DISTANCE

def get_valid_angle():
    while True:
        try:
            angle = float(input(f"Enter angle ({MIN_ANGLE}-{MAX_ANGLE}): "))
            if MIN_ANGLE <= angle <= MAX_ANGLE:
                return angle
            print(f"Invalid angle! Must be between {MIN_ANGLE} and {MAX_ANGLE}.")
        except ValueError:
            print("Please enter a numeric value.")

def get_valid_distance():
    while True:
        try:
            distance = float(input(f"Enter distance (>{MIN_DISTANCE}, up to {MAX_DISTANCE}): "))
            if MIN_DISTANCE < distance <= MAX_DISTANCE:
                return distance
            print(f"Invalid distance! Must be greater than {MIN_DISTANCE} and up to {MAX_DISTANCE}.")
        except ValueError:
            print("Please enter a numeric value.")