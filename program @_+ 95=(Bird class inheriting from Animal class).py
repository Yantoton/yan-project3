class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Bird(Animal):
    def __init__(self,name,age,sing):
        super().__init__(name,age)
        self.sing = sing
    def __iter__(self):
        yield self.name
        yield self.age
        yield self.sing

my_bird = Bird("Tuntun", 1, True)
for bird in my_bird:
    print(bird)
print(f"Bird Name:{my_bird.name} Bird Age:{my_bird.age} Can Sing:{my_bird.sing}")
