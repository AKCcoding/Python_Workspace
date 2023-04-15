class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point()
point1.move()

point1.x = 10
print(point1.x)