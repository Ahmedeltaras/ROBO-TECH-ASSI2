import pynput
class thrusterController:
    def __init__(self):
        self.thrusters = [0, 0 , 0 , 0 , 0 , 0 , 0 , 0]
        self.is_cooling_down = False

    def stop_all(self):
        self.thrusters = [0, 0 , 0 , 0 , 0 , 0 , 0 , 0]

    def move(self, direction):
        if not self.is_cooling_down:
            if direction == "up":
                self.thrusters = [20, 20, 20, 20, 20, 20, 20, 20] # here is the values that is displayed when moving upwards
            elif direction == "down":
                self.thrusters = [-20, -20, -20, -20, -20, -20, -20, -20] # here is the values that is displayed when moving downwards
            elif direction == "right":
                self.thrusters = [10, 10, 10, 10, 10, 10, 10, 10] # here is the values that is displayed when moving to the right
            elif direction == "left":
                self.thrusters = [-10, -10, -10, -10, -10, -10, -10, -10] # here is the values that is displayed when moving to the left