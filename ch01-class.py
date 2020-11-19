
class Car:

    wheels = 4

    def __init__(self):
        self.data = []

    def drivefast(self):
        print("You are now driving very fast!")


myCar = Car()
print(myCar.wheels)
myCar.drivefast()
