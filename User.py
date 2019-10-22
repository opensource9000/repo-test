class User:
    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age


    def hi(self):
        print(f"Hi, my name is {self.name} {self.lastName}")


    def whoami(self):
        print(f"My name is {self.name} {self.lastName} and I am {self.age}")
