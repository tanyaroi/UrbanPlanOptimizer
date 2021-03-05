class Person:  
    def __init__(self, name="John"):
        self.name = name

    def talk(self):
        self.age = 32
        print(f"Hello my name is {self.name}")

    def talk2(self):
        print(f"Hello my age is {self.age}")


person = Person()
person.talk()