class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point(20,30)
print(point1.x)
print(point1.y)
point1.move()