class User:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName


    def hi(self):
        print(f"Hi, my name is {self.name} {self.lastName}")


u = User("Robot", "9000")
u.hi()

