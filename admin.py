from datetime import datetime

class Room:
    def __init__(self, room_number, is_available, room_type = "", price_per_night = 0):
        self.room_number = room_number
        self.is_available = is_available
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Booked"
        print(f"Room {self.room_number} - {status}\nRoom Type: {self.room_type}\nPrice per night: {self.price_per_night} PHP\n\n")

def load_room_status():
    global rooms
    rooms.clear()
    try:
        f = open("room_status.txt", "r")
        lines = f.readlines()
        for line in lines:
                parts = line.strip().split(", ")
                
                if len(parts) == 4:
                    try:
                        # Extract and parse each part of the line
                        room_number = int(parts[0].split(" ")[1])
                        status = parts[1].split(": ")[1]
                        room_type = parts[2].split(": ")[1]
                        price_per_night = int(parts[3].split(": ")[1].split()[0])
                        room = Room(room_number, status == "Available", room_type, price_per_night)
                        rooms.append(room)
                    except (IndexError, ValueError):
                        pass
    except FileNotFoundError:
        pass


def save_room_status():
    f = open("room_status.txt", "w")
    for room in rooms:
        status = "Available" if room.is_available else "Booked"
        f.write(f"Room {room.room_number}, Status: {status}, Room Type: {room.room_type}, Price per night: {room.price_per_night} PHP\n")

def add_new_room():
    room_types = {
        '1': 'Single Room',
        '2': 'Double Room',
        '3': 'Triple Room',
        '4': 'Quadruple Room',
        '5': 'Family Room',
        '6': 'Deluxe Room'
    }

    while True:
        try:
            new_room_number = len(rooms) + 1
            print("\n------------- Room Type -------------\n")
            for key, value in room_types.items():
                print(f"{key}. {value}")
            room_type_choice = input("\nEnter the room type number (1-6): ")
            if room_type_choice not in room_types:
                print("\nInvalid room type choice. Please enter a valid number.")
                continue

            room_type = room_types[room_type_choice]
            room_price = int(input("Enter price of room per night: "))
            new_room = Room(new_room_number, True, room_type, room_price)
            rooms.append(new_room)
            print(f"Add New Room {new_room_number}\nRoom Type: {new_room.room_type}\nPrice per night: {new_room.price_per_night} PHP. is added successfully!")
            save_room_status()
            break
        except ValueError:
            print("\nInvalid input. Please try again.\n")


def delete_room():
    try:
        for room in rooms:
            room.display_info()
        room_number = int(input("\nRoom Number to delete: "))

        room = next((r for r in rooms if r.room_number == room_number), None)

        if room:
            if room.is_available:
                rooms.remove(room)
                print(f"Room {room_number} has been deleted successfully!")
                save_room_status()
            else:
                print(f"Room {room_number} is currently booked and cannot be deleted.")
        else:
            print("Room not found.")
    except ValueError:
        print("Please enter a valid room number.")


def view_check_in_records():
    try:
        f = open("check_in.txt", "r")
        records = f.read()
        if records:
            print("\n------------- Check In Record's -------------")
            print(records)
        else:
            print("\nNo check-in record's found.")
    except FileNotFoundError:
        print("\nNo check-in record's found.")


def view_check_out_records():
    try:
        f = open("check_out.txt", "r")
        records = f.read()
        if records:
            print("\n------------- Check Out Record's -------------")
            print(records)
        else:
            print("\nNo Check Out record's found.")
    except FileNotFoundError:
        print("\nNo Check Out record's found.")

# Admin portal menu
def main():
    global rooms
    rooms = []
    load_room_status()

    while True:
        print("\n------------- Admin -------------\n")
        print("1. View Check In Record's")
        print("2. View Check Out Record's")
        print("3. Add New Room")
        print("4. Delete Room")
        print("5. Display Rooms")
        print("6. Add New Employee")
        print("7. Add New Admin")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            view_check_in_records()

        elif choice == '2':
            view_check_out_records()

        elif choice == '3':
            add_new_room()

        elif choice == '4':
            delete_room()

        elif choice == '5':
            print("\n------------- Room Status -------------\n")
            for room in rooms:
                room.display_info()

        elif choice == '6':
            print("\n--- Employee Registration ---")
            employee_name = input("Enter Name: ")

            while True:
                employee_password = input("Enter Password (8 characters or more): ")
                if len(employee_password) >= 8:
                    break
                else:
                    print("Password must be at least 8 characters. Please try again.")

            f = open("staff.txt", "a")
            f.write(f"Name: {employee_name}, Password: {employee_password}\n")
            f.close()
            print("\nRegister success!")

        elif choice == '7':
            print("\n--- Admin Registration ---")
            admin_name = input("Enter Name: ")

            while True:
                admin_password = input("Enter Password (8 characters or more): ")
                if len(admin_password) >= 8:
                    break
                else:
                    print("Password must be at least 8 characters. Please try again.")

            f = open("admin.txt", "a")
            f.write(f"Name: {admin_name}, Password: {admin_password}\n")
            f.close()
            print("\nRegister success!")

        elif choice == '8':
            print("\nSystem Shutdown...\n")
            break

        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()