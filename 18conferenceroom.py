from datetime import datetime, timedelta

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.reservations = {}

    def is_available(self, start_time, end_time):
        for reserved_start, reserved_end in self.reservations.values():
            if start_time < reserved_end and end_time > reserved_start:
                return False
        return True

    def reserve(self, user, start_time, end_time):
        if self.is_available(start_time, end_time):
            reservation_id = len(self.reservations) + 1
            self.reservations[reservation_id] = (start_time, end_time, user)
            return reservation_id
        else:
            return None

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class ReservationSystem:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def display_rooms(self):
        print("Available Rooms:")
        for room_name, room in self.rooms.items():
            print(f"{room_name} (Capacity: {room.capacity})")

    def display_reservations(self, room_name):
        room = self.rooms.get(room_name)
        if room:
            print(f"Reservations for {room_name}:")
            for reservation_id, (start_time, end_time, user) in room.reservations.items():
                print(f"Reservation {reservation_id}: {user.username} ({user.email}) | "
                      f"Start: {start_time}, End: {end_time}")
        else:
            print(f"Room {room_name} not found.")

    def book_room(self, room_name, user, start_time, end_time):
        room = self.rooms.get(room_name)
        if room:
            reservation_id = room.reserve(user, start_time, end_time)
            if reservation_id is not None:
                print(f"Reservation successful! Reservation ID: {reservation_id}")
            else:
                print("The room is not available for the specified time.")
        else:
            print(f"Room {room_name} not found.")

def main():
    reservation_system = ReservationSystem()

    room1 = Room("Conference Room 1", 10)
    room2 = Room("Conference Room 2", 8)

    reservation_system.add_room(room1)
    reservation_system.add_room(room2)

    while True:
        print("\nConference Room Booking System")
        print("1. Display Available Rooms")
        print("2. Display Reservations for a Room")
        print("3. Book a Room")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            reservation_system.display_rooms()
        elif choice == '2':
            room_name = input("Enter the room name: ")
            reservation_system.display_reservations(room_name)
        elif choice == '3':
            room_name = input("Enter the room name: ")
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            user = User(username, email)
            start_time = input("Enter start time (YYYY-MM-DD HH:MM): ")
            end_time = input("Enter end time (YYYY-MM-DD HH:MM): ")

            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

            reservation_system.book_room(room_name, user, start_time, end_time)
        elif choice == '4':
            print("Exiting the Conference Room Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
