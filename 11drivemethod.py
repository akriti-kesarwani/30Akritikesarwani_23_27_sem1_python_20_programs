class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclasses must implement the drive method")


class Car(Vehicle):
    def drive(self):
        return "I'm driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "I'm pedaling a bicycle"


def main():
    vehicle_type = input("Enter the type of vehicle (car/bicycle): ").lower()

    if vehicle_type == "car":
        vehicle = Car()
    elif vehicle_type == "bicycle":
        vehicle = Bicycle()
    else:
        print("Invalid vehicle type")
        return

    print(vehicle.drive())


if __name__ == "__main__":
    main()
