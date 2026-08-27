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
                self.thrusters = [20, 20, 20, 20, 20, 20, 20, 20] # hna el value el btezhar lama yet7arak fooq
            elif direction == "down":
                self.thrusters = [-20, -20, -20, -20, -20, -20, -20, -20] # hna el value el btezhar lama yet7arak t7t
            elif direction == "right":
                self.thrusters = [10, 10, 10, 10, 10, 10, 10, 10] # hna el value el btezhar lama yet7arak right
            elif direction == "left":
                self.thrusters = [-10, -10, -10, -10, -10, -10, -10, -10] # hna el value el btezhar lama yet7arak shemal
