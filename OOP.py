class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Dancer(Person):
    def __init__(self, name, age, dance_style):
        super().__init__(name, age)
        self.dance_style = dance_style

    def dance(self):
        print(f"I love to dance {self.dance_style}!")


person1 = Person("Esihle", 23)
person1.introduce()


dancer1 = Dancer("Esihle", 23, "Floss")
dancer1.dance()
