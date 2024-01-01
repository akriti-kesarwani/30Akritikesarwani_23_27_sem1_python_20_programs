class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_details(self):
        return f"{self.year} {self.make} {self.model}"

# Taking user input for car details
make = input("Enter the car make: ")
model = input("Enter the car model: ")
year = input("Enter the car year: ")

# Creating an object of the Car class with user input
user_car = Car(make=make, model=model, year=year)

# Printing the details of the user's car
print("User's car details:", user_car.get_details())
