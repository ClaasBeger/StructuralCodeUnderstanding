class Ball:
    def __init__(self, x, y, radius, xDelta, yDelta):
        self.x = x
        self.y = y
        self.radius = radius
        self.xDelta = xDelta
        self.yDelta = yDelta

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getXDelta(self):
        return self.xDelta

    def setXDelta(self, xDelta):
        self.xDelta = xDelta

    def getYDelta(self):
        return self.yDelta

    def setYDelta(self, yDelta):
        self.yDelta = yDelta

    def move(self):
        self.x += self.xDelta
        self.y += self.yDelta

    def reflectHorizontal(self):
        self.xDelta = -self.xDelta

    def reflectVertical(self):
        self.yDelta = -self.yDelta

    def __str__(self):
        return f"Ball[({self.x},{self.y}),speed=({self.xDelta},{self.yDelta})]"

if __name__ == "__main__":
    ball = Ball(5.0, 5.0, 2, 1.0, 1.0)
    ball.move()
    print(ball)
    ball.reflectHorizontal()
    ball.reflectVertical()
    ball.move()