class Pet:
    def __init__(self, name, age, color):
        self.pets_name = name
        self.pets_age = age
        self.pets_color = color

    
class Cat(Pet):
    def speak(self):
        print(f"{self.pets_name} is {self.pets_age} years old.")
        print(f"{self.pets_name} says MEOW!")
        print(f"{self.pets_name}' hair color is {self.pets_color}.")
    
    
class Dog(Pet):
    def speak(self):
        print(f"{self.pets_name} is {self.pets_age} years old.")
        print(f"{self.pets_name} says BARK!")
        print(f"{self.pets_name}'s hair color is {self.pets_color}.\n")


def main():
    my_dog = Dog("Barky", 11, "red")
    my_cat = Cat("Whiskers", 7, "white")
    my_dog.speak()
    my_cat.speak()


if __name__ == "__main__":
    main()