class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " is sitting")

dog = Dog("Tom", 10)
dog.sit()