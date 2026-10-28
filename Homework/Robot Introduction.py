class Robot:

    def __init__(self, name):
        self.name = name

Tom=Robot("Tom")
Jerry=Robot("Jerry")

print("Robot 1's name is {}".format( Tom.name))
print("Robot 2's name is {}".format( Jerry.name))
