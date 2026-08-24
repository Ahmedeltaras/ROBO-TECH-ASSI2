import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Visualizer:
    def __init__(self, rover):
        self.rover = rover
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], marker='o')
        self.ax.set_xlim(-100, 100)
        self.ax.set_ylim(-100, 100)
        self.ax.set_title("Rover Path")
        self.ax.grid(True)

    def update_static(self):
        self.line.set_data(self.rover.path_x, self.rover.path_y)
        self._autoscale()
        plt.draw()
        plt.pause(0.001)

    def _autoscale(self):
        self.ax.relim()
        self.ax.autoscale_view()

    def run_live(self, update_func, interval=500, frames=100):
        def _animate(i):
            update_func()
            self.line.set_data(self.rover.path_x, self.rover.path_y)
            self._autoscale()
            return self.line,

        ani = animation.FuncAnimation(self.fig, _animate, interval=interval, frames=frames, repeat=False)
        plt.show()