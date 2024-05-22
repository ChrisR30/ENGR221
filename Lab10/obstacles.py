import random

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # You can add more properties like size, color, etc. if needed

class Game:
    def __init__(self):
        self.obstacles = []

    def generate_obstacles(self, num_obstacles, width, height):
        for _ in range(num_obstacles):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            obstacle = Obstacle(x, y)
            self.obstacles.append(obstacle)
