import math
import random

class Ball:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_z(self):
        return self.z

    def set_z(self, z):
        self.z = z

    def set_xyz(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class Player:
    def __init__(self, number, x, y, z):
        self.number = number
        self.x = x
        self.y = y
        self.z = z

    def move(self, x_disp, y_disp):
        self.x += x_disp
        self.y += y_disp

    def jump(self, z_disp):
        self.z += z_disp

    def near(self, ball):
        distance = math.sqrt((ball.get_x() - self.x) ** 2 + (ball.get_y() - self.y) ** 2 + (ball.get_z() - self.z) ** 2)
        return distance < 8

    def kick(self, ball):
        ball.set_x(ball.get_x() + random.randint(0, 19))
        ball.set_y(ball.get_y() + random.randint(0, 19))
        ball.set_z(ball.get_z() + random.randint(0, 4))

class TestPlayer:
    @staticmethod
    def main():
        ball = Ball(15, 15, 15)
        player = Player(4, 15, 15, 15)
        player.kick(ball)
        print(ball)

if __name__ == "__main__":
    ball2 = Ball(10, 10, 10)
    player3 = Player(3, 6, 6, 6)
    print(player3.near(ball2))