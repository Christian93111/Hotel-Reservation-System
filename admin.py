import main
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
        print(f"Price per night: ₱ {self.price_per_night}\n")

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
    with open("room_status.txt", "w") as f:
        sorted_rooms = sorted(rooms, key=lambda x: x.room_number)
        for room in sorted_rooms:
            status = "Available" if room.is_available else "Booked"
            f.write(f"Room {room.room_number}, Status: {status}, Room Type: {room.room_type}, Price per night: {room.price_per_night} PHP\n")

def add_new_room():
    while True:
        room_types = {
            '1': 'Single Bed Room',
            '2': 'Double Bed Room',
            '3': 'Triple Bed Room',
            '4': 'Quadruple Bed Room',
            '5': 'Family Bed Room',
            '6': 'VIP Room'
        }

        while True:
            try:
                room_numbers = [room.room_number for room in rooms]

                new_room_number = 1
                while new_room_number in room_numbers:
                    new_room_number += 1

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
                rooms.insert(0, new_room)

                print(f"\nAdd New Room {new_room_number}\nRoom Type: {new_room.room_type}\nPrice per night: ₱ {new_room.price_per_night}. is added successfully!")
                save_room_status()
                break

            except ValueError:
                print("\nInvalid input. Please try again.")

        while True:
            print("\nDo you want to continue?")
            print("1. Yes")
            print("2. No")

            again = input("\nChoose an option: ").strip()
            if again == "1":
                break

            elif again == "2":
                print("\nReturn to the main menu....")
                admin_portal()
                return

            else:
                print("\nInvalid input. Please enter '1' to continue adding or '2' to return to the main menu.")

def delete_room():
    while True:
        try:
            print("\n------------- Room Information -------------\n")
            for room in rooms:
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

            while True:
                print("\nDo you want to continue?")
                print("1. Yes")
                print("2. No")

                again = input("\nChoose an option: ").strip()

                if again == '1':
                    break

                elif again == '2':
                    print("\nReturning to the main menu...")
                    admin_portal()
                    return

                else:
                    print("\nInvalid input. Please enter '1' to continue editing or '2' to return to the main menu.")
        except ValueError:
            print("\nPlease enter a valid room number.")

def edit_room():
    while True:
        try:
            print("\n------------- Room Information -------------\n")
            for room in rooms:
                room.display_info()

            room_number = int(input("\nEnter Room Number to Edit: "))

            room = None
            for r in rooms:
                if r.room_number == room_number:
                    room = r
                    break

            if room:
                if room.is_available:
                    room_types = {
                        '1': 'Single Bed Room',
                        '2': 'Double Bed Room',
                        '3': 'Triple Bed Room',
                        '4': 'Quadruple Bed Room',
                        '5': 'Family Bed Room',
                        '6': 'VIP Room'
                    }

                    print("\n------------- Room Type -------------\n")
                    for key, value in room_types.items():
                        print(f"{key}. {value}")

                    new_room_type = input("\nEnter Room Type: ").strip()

                    # Ensure valid selection from room_types dictionary
                    if new_room_type in room_types:
                        room.room_type = room_types[new_room_type]
                    else:
                        print("\nInvalid choice. Please select a number between 1 and 6.")
                        continue  # restart the process if the user makes an invalid selection

                    try:
                        new_price = int(input("\nEnter New Price Per Night: "))
                        room.price_per_night = new_price

                    except ValueError:
                        print("\nInvalid input. Please enter a valid number for the price.")

                    print(f"\nRoom Type: {room.room_type}\nPrice per night: ₱ {room.price_per_night}. has been updated successfully!")
                    save_room_status()

                    while True:
                        print("\nDo you want to continue?")
                        print("1. Yes")
                        print("2. No")

                        again = input("\nChoose an option: ").strip()

                        if again == '1':
                            break
                        elif again == '2':
                            print("\nReturning to the main menu...")
                            admin_portal()
                            return
                        else:
                            print("\nInvalid choice. Please enter '1' to continue editing or '2' to return to the main menu.")
                else:
                    print(f"\nRoom {room_number} is currently booked and cannot be edited.")
            else:
                print("\nRoom not found.")
        except ValueError:
            print("\nInvalid choice. Please enter a valid room number.")


def view_check_in_records():
    f = open("check_in.txt", "r")
    records = f.read()
    if records:
        print("\n------------- View Customer Check In Information -------------\n")
        print(records)
    else:
        print("\nNo Check In Information found")

def view_check_out_records():
    f = open("check_out.txt", "r")
    records = f.read()
    if records:
        print("\n------------- Check Out Log -------------\n")
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
        print("\n------------- Admin Login Information Login -------------\n")
        print(records)
    else:
        print("\nNo Admin Information found.")

def view_cancel_booking_records():
    f = open("cancel_booking.txt", "r")
    records = f.read()
    if records:
        print("\n------------- Cancel Booking Log -------------\n")
        print(records)
    else:
        print("\nNo Cancel Booking Information found")

def new_employee():
    while True:
        print("\n------------- New Employee Register Login -------------\n")
        while True:
            employee_name = input("\nEnter Name: ")
            if employee_name.replace(" ", "").isalpha():
                break
            else:
                print("\nName must only contain alphabetic characters.")
        while True:
            employee_password = input("\nEnter Password (8 characters or more): ")
            if len(employee_password) >= 8:
                break
            else:
                print("\nPassword must be at least 8 characters. Please try again.")

        f = open("staff.txt", "a")
        f.write(f"Name: {employee_name}, Password: {employee_password}\n\n")
        f.close()
        print("\nRegister success!")

        while True:
            print("\nDo you want to continue?")
            print("1. Yes")
            print("2. No")

            again = input("\nChoose an option: ").strip()
            if again == "1":
                break

            elif again == "2":
                print("\nReturn to the main menu....")
                admin_portal()
                return
            else:
                print("\nInvalid choice. Please enter '1' to continue editing or '2' to return to the main menu.")

def new_admin():
    while True:
        print("\n------------- New Admin Register Login -------------\n")
        while True:
            admin_name = input("\nEnter Name: ")
            if admin_name.replace(" ", "").isalpha():
                break
            else:
                print("\nName must only contain alphabetic characters.")

        while True:
            admin_password = input("\nEnter Password (8 characters or more): ")
            if len(admin_password) >= 8:
                break
            else:
                print("\nPassword must be at least 8 characters. Please try again.")

        f = open("admin.txt", "a")
        f.write(f"Name: {admin_name}, Password: {admin_password}\n\n")
        f.close()
        print("\nRegister success!")

        while True:
            print("\nDo you want to continue?")
            print("1. Yes")
            print("2. No")

            again = input("\nChoose an option: ").strip()

            if again == '1':
                break
            elif again == '2':
                print("\nReturn to the main menu....")
                return
            else:
                print("\nInvalid choice. Please enter '1' to continue editing or '2' to return to the main menu.")

def view_rooms():
    if rooms:
        print("\n------------- Room Information -------------\n")
        for room in rooms:
            room.display_info()
    else:
        print("\nNo Room Information Found.")

def admin_portal():
    global rooms
    rooms = []
    load_room_status()

    while True:
        print("\n-------------  -------------\n")
        print("1. Add New Room")
        print("2. Delete Room")
        print("3. Edit Room")
        print("4. Display Rooms")
        print("5. View Check In Log")
        print("6. View Check Out Log")
        print("7. View Cancel Booking Log")
        print("8. Add New Employee")
        print("9. Add New Admin")
        print("10. View Employee Information Login")
        print("11. View Admin Information Login")
        print("12. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            add_new_room()

        elif choice == '2':
            delete_room()

        elif choice == '3':
            edit_room()

        elif choice == '4':
            view_rooms()

        elif choice == '5':
            view_check_in_records()

        elif choice == '6':
            view_check_out_records()

        elif choice == '7':
            view_cancel_booking_records()

        elif choice == '8':
            new_employee()

        elif choice == '9':
            new_admin()

        elif choice == '10':
            view_employee_record_login()

        elif choice == '11':
            view_admin_record_login()

        elif choice == '12':
            print("\nReturn to the menu...")
            main.main_portal()

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    admin_portal()