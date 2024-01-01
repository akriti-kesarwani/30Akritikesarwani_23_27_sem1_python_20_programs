class Vehicle:
    # Class attribute with default value "white"
    color = "white"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        # Prompt the user for input to set the color attribute
        self.color = input(f"Enter the color for {brand} {model} (default is white): ") or self.color

# Creating instances of the Vehicle class with user input
car1 = Vehicle(input("Enter the brand for the first vehicle: "), input("Enter the model for the first vehicle: "))
car2 = Vehicle(input("Enter the brand for the second vehicle: "), input("Enter the model for the second vehicle: "))

# Accessing the color attribute
print(f"{car1.brand} {car1.model} color: {car1.color}")
print(f"{car2.brand} {car2.model} color: {car2.color}")
