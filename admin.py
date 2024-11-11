from datetime import datetime

class Room:
    def __init__(self, room_number, is_available, room_type = "", price_per_night = 0):
        self.room_number = room_number
        self.is_available = is_available
        self.room_type = room_type
        self.price_per_night = price_per_night

    def display_info(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Booked"

        print("Room", self.room_number, "-", status)
        print("Room Type:", self.room_type)
        print("Price per night:", self.price_per_night, "PHP\n")

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
        if room.is_available:
            status = "Available"
        else:
            status = "Booked"
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
            room_type_choice = input("\nEnter Room type number: ")

            if room_type_choice not in room_types:
                print("\nInvalid room type choice. Please enter a valid number.")
                continue

            room_type = room_types[room_type_choice]
            room_price = int(input("\nEnter Price of room per night: "))
            new_room = Room(new_room_number, True, room_type, room_price)
            rooms.append(new_room)
            print(f"\nAdd New Room {new_room_number}\nRoom Type: {new_room.room_type}\nPrice per night: {new_room.price_per_night} PHP. is added successfully!")
            save_room_status()
            break
        except ValueError:
            print("\nInvalid input. Please try again.")

def delete_room():
    try:
        for room in rooms:
            print("\n------------- Room Information -------------\n")
            room.display_info()
        room_number = int(input("\nRoom Number to delete: "))

        room = None
        for r in rooms:
            if r.room_number == room_number:
                room = r
                break

        if room:
            if room.is_available:
                rooms.remove(room)
                print(f"\nRoom {room_number} has been deleted successfully!")
                save_room_status()
            else:
                print(f"\nRoom {room_number} is currently booked and cannot be deleted.")
        else:
            print("\nRoom not found.")
    except ValueError:
        print("\nPlease enter a valid room number.")

def view_check_in_records():
    f = open("check_in.txt", "r")
    records = f.read()
    if records:
        print("\n------------- Check In Information -------------\n")
        print(records)
    else:
        print("\nNo Check In Information found")

def view_check_out_records():
    f = open("check_out.txt", "r")
    records = f.read()
    if records:
        print("\n------------- Check Out Information -------------\n")
        print(records)
    else:
        print("\nNo Check Out Information found.")

def view_employee_record_login():
        f = open("staff.txt", "r")
        records = f.read()
        if records:
            print("\n------------- Staff Login Information -------------\n")
            print(records)
        else:
            print("\nNo Employee Information found.")

def view_admin_record_login():
    f = open("admin.txt", "r")
    records = f.read()
    if records:
        print("\n------------- Admin Login Information -------------\n")
        print(records)
    else:
        print("\nNo Admin Information found.")

def new_employee():
    print("\n------------- New Employee Register Information -------------\n")
    employee_name = input("\nEnter Name: ")
    while True:
        employee_password = input("\nEnter Password (8 characters or more): ")
        if len(employee_password) >= 8:
            break
        else:
            print("\nPassword must be at least 8 characters. Please try again.")

    f = open("staff.txt", "a")
    f.write(f"Name: {employee_name}, Password: {employee_password}\n")
    f.close()
    print("\nRegister success!")

def new_admin():
    print("\n------------- New Admin Register Information -------------\n")
    admin_name = input("\nEnter Name: ")
    while True:
        admin_password = input("\nEnter Password (8 characters or more): ")
        if len(admin_password) >= 8:
            break
        else:
            print("\nPassword must be at least 8 characters. Please try again.")
            
    f = open("admin.txt", "a")
    f.write(f"Name: {admin_name}, Password: {admin_password}\n")
    f.close()
    print("\nRegister success!")

def admin_portal():
    global rooms
    rooms = []
    load_room_status()

    while True:
        print("\n------------- Admin -------------\n")
        print("1. Add New Room")
        print("2. Delete Room")
        print("3. Display Rooms")
        print("4. View Check In Information")
        print("5. View Check Out Information")
        print("6. Add New Employee")
        print("7. Add New Admin")
        print("8. View Employee Information")
        print("9. View Admin Information")
        print("10. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            add_new_room()

        elif choice == '2':
            delete_room()

        elif choice == '3':
            if rooms:
                print("\n------------- Room Information -------------\n")
                for room in rooms:
                    room.display_info()
            else:
                print("\nNo room record Information found.")

        elif choice == '4':
            view_check_in_records()

        elif choice == '5':
            view_check_out_records()

        elif choice == '6':
            new_employee()

        elif choice == '7':
            new_admin()

        elif choice == '8':
            view_employee_record_login()

        elif choice == '9':
            view_admin_record_login()

        elif choice == '10':
            print("\nReturn to the menu...")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    admin_portal()