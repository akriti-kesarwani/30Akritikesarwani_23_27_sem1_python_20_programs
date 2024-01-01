class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.1 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare

def main():
    try:
        seating_capacity = int(input("Enter the seating capacity of the bus: "))
        if seating_capacity <= 0:
            print("Seating capacity must be a positive integer.")
            return

        bus_instance = Bus(seating_capacity)
        total_fare = bus_instance.calculate_fare()

        print(f"\nTotal fare for the bus with seating capacity {seating_capacity} is: ${total_fare:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for seating capacity.")

if __name__ == "__main__":
    main()
