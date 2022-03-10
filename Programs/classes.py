class Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def move():
        print("move")

    @staticmethod
    def draw():
        print("draw")


point1 = Point(24, 35)

# point1.x = 242
# point1.y = 22
print(f"Coordination X is: {point1.x} \nCoordination Y is: {point1.y}")
print("__________________________________")

# Call function move from class Point
point1.move()
# Call function draw from class Point
point1.draw()
print(point1.x)

print("=============================")


# Simple practice with classes
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Chika")
bob.talk()
