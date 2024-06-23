class Robot:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def move_forward(self, distance):
        self.y += distance
        print(f"{self.name} moved forward {distance} units. New position: ({self.x}, {self.y})")

    def move_backward(self, distance):
        self.y -= distance
        print(f"{self.name} moved backward {distance} units. New position: ({self.x}, {self.y})")

    def turn_left(self):
        self.x -= 1
        print(f"{self.name} turned left. New position: ({self.x}, {self.y})")

    def turn_right(self):
        self.x += 1
        print(f"{self.name} turned right. New position: ({self.x}, {self.y})")

robot = Robot("Robby")
robot.move_forward(5)
robot.turn_left()
robot.move_backward(2)
robot.turn_right()