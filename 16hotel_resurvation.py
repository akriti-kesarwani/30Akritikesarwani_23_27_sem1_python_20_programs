from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_available = True
        self.reservations = []

    def check_availability(self):
        return self.is_available

    def book_room(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

class Guest:
    def __init__(self, guest_id, name, email):
        self.guest_id = guest_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"

class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def generate_invoice(self):
        num_nights = (self.check_out_date - self.check_in_date).days
        total_cost = num_nights * self.room.price_per_night
        return f"Invoice for {self.guest.name} - Room {self.room.room_number}: ${total_cost}"

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_room_availability(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.check_availability()
        return False

    def book_room(self, room_number, guest, check_in_date, check_out_date):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.book_room():
                    reservation_id = len(room.reservations) + 1
                    reservation = Reservation(reservation_id, guest, room, check_in_date, check_out_date)
                    room.reservations.append(reservation)
                    return reservation
                else:
                    return None
        return None

# Function to get user input for date
def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

# Example usage with user input
if __name__ == "__main__":
    # Create a hotel
    my_hotel = Hotel("My Hotel")

    # Add rooms to the hotel
    room1 = Room(101, 2, 100)
    room2 = Room(102, 4, 150)
    my_hotel.add_room(room1)
    my_hotel.add_room(room2)

    # Create a guest
    guest_name = input("Enter your name: ")
    guest_email = input("Enter your email: ")
    guest1 = Guest(1, guest_name, guest_email)

    # Check room availability
    room_number_to_check = int(input("Enter the room number to check availability: "))
    print(f"Room {room_number_to_check} is available: {my_hotel.check_room_availability(room_number_to_check)}")

    # Book a room
    room_number_to_book = int(input("Enter the room number to book: "))
    check_in_date = get_date_input("Enter check-in date")
    check_out_date = get_date_input("Enter check-out date")

    reservation = my_hotel.book_room(room_number_to_book, guest1, check_in_date, check_out_date)

    if reservation:
        print(f"Room {room_number_to_book} booked for {guest1.name}")
        print(reservation.generate_invoice())
    else:
        print(f"Room {room_number_to_book} is not available")

    # Check room availability after booking
    print(f"Room {room_number_to_book} is available: {my_hotel.check_room_availability(room_number_to_book)}")
