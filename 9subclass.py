class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # This method will be overridden by subclasses

    def display_info(self):
        print(f"Name: {self.name}\nSpecies: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof! Woof!")

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        print("Meow!")

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

# Take user input for Dog
dog_name = input("Enter the name of the dog: ")
dog_breed = input("Enter the breed of the dog: ")
dog = Dog(name=dog_name, breed=dog_breed)

# Take user input for Cat
cat_name = input("Enter the name of the cat: ")
cat_color = input("Enter the color of the cat: ")
cat = Cat(name=cat_name, color=cat_color)

# Display information and make sounds
print("\nDog Information:")
dog.display_info()
dog.make_sound()

print("\nCat Information:")
cat.display_info()
cat.make_sound()
