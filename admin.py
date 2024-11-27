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
                        # print(f"\nSkipping invalid room entry: {line.strip()}")
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

                room_type_choice = input("\nEnter Room type number: ").strip()

                if room_type_choice not in room_types:
                    print("\nInvalid choice. Please select a number between 1 to 6.")
                    continue

                room_type = room_types[room_type_choice]
                room_price = int(input("\nEnter Price of room per night: ").strip())
                new_room = Room(new_room_number, True, room_type, room_price)
                rooms.insert(0, new_room)

                print(f"\nAdd New Room {new_room_number}\nRoom Type: {new_room.room_type}\nPrice per night: ₱ {new_room.price_per_night}. is added successfully!")
                save_room_status()
                break

            except ValueError:
                print("\nError: Invalid choice. Please try again.")

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

            else:
                print("\nError: Invalid choice. Please enter '1' to continue adding or '2' to return to the main menu.")

# def remove_room():
#     while True:
#         try:
#             if not rooms:
#                 print("\nError: Sorry No Room Record Information. Cannot be remove room")
#                 break
#
#             print("\n------------- Room Information ------------\n")
#             for room in rooms:
#                 room.display_info()
#
#             room_number = int(input("Room Number to remove: ").strip())
#
#             room = None
#             for r in rooms:
#                 if r.room_number == room_number:
#                     room = r
#                     break
#
#             if room:
#                 if room.is_available:
#                     rooms.remove(room)
#                     print(f"\nRoom {room_number} has been deleted successfully!")
#                     save_room_status()
#                 else:
#                     print(f"\nError: Room {room_number} is currently booked and cannot be remove.")
#             else:
#                 print("\nError: Room not found.")
#
#             while True:
#                 print("\nDo you want to continue?")
#                 print("1. Yes")
#                 print("2. No")
#
#                 again = input("\nChoose an option: ").strip()
#
#                 if again == '1':
#                     break
#
#                 elif again == '2':
#                     print("\nReturning to the main menu...")
#                     admin_portal()
#
#                 else:
#                     print("\nError: Invalid choice. Please enter '1' to continue remove or '2' to return to the main menu.")
#         except ValueError:
#             print("\nError: Please enter a valid room number.")

def edit_room():
    while True:
        try:
            if not rooms:
                print("\nError: Sorry No Room Record Information. Cannot be edit room")
                break

            print("\n------------- Room Information -------------\n")
            for room in rooms:
                room.display_info()

            room_number = int(input("Enter Room Number to Edit: ").strip())

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

                    # ensure valid selection from room_types dictionary
                    if new_room_type in room_types:
                        room.room_type = room_types[new_room_type]
                    else:
                        print("\nInvalid choice. Please select a number between 1 to 6.")
                        continue  # restart the process if the user makes an invalid selection

                    try:
                        new_price = int(input("\nEnter New Price Per Night: ").strip())
                        room.price_per_night = new_price

                    except ValueError:
                        print("\nError: Invalid input. Please enter a valid number for the price.")

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
                            print("\nError: Invalid choice. Please enter '1' to continue editing or '2' to return to the main menu.")

                else:
                    print(f"\nError: Room {room_number} is currently booked and cannot be edited.")

            else:
                print("\nError: Room not found.")

        except ValueError:
            print("\nError: Invalid choice. Please enter a valid room number.")

def view_rooms():
    if rooms:
        print("\n------------- Room Information -------------\n")
        for room in rooms:
            room.display_info()
    else:
        print("\nError: No Room Information Found. cannot be viewed")

def view_check_in_records():
    f = open("check_in.txt", "r", encoding="utf-8")
    records = f.read().strip()
    if records:
        print("\n------------- View Customer Check In Information -------------\n")
        print(records)
    else:
        print("\nError: No Check In Information found cannot be viewed")

def view_check_out_records():
    f = open("check_out.txt", "r")
    records = f.read().strip()
    if records:
        print("\n------------- Check-Out Log -------------\n")
        print(records)
    else:
        print("\nError: No Check Out Information found. cannot be viewed")

def view_cancel_booking_records():
    f = open("cancel_booking.txt", "r")
    records = f.read().strip()
    if records:
        print("\n------------- Cancel Booking Log -------------\n")
        print(records)
    else:
        print("\nError: No Cancel Booking Information found. cannot be viewed")

def new_employee():
    while True:
        print("\n------------- New Employee Register Login -------------\n")

        employee_username = input("\nEnter Username: ")

        while True:
            employee_password = input("\nEnter Password: ")
            if len(employee_password) >= 8:
                break
            else:
                print("\nError: Password must be at least 8 characters. Please try again.")

        f = open("staff.txt", "a")
        f.write(f"Username: {employee_username}, Password: {employee_password}\n\n")
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
                print("\nError: Invalid choice. Please try again")

def new_admin():
    while True:
        print("\n------------- New Admin Register Login -------------\n")

        admin_username = input("\nEnter Username: ").strip()

        while True:
            admin_password = input("\nEnter Password: ").strip()
            if len(admin_password) >= 8:
                break
            else:
                print("\nError: Password must be at least 8 characters. Please try again.")

        f = open("admin.txt", "a")
        f.write(f"Username: {admin_username}, Password: {admin_password}\n\n")
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
                print("\nError: Invalid choice. Please enter '1' to continue editing or '2' to return to the main menu.")

def view_employee_record_login():
        f = open("staff.txt", "r")
        records = f.read().strip()
        if records:
            print("\n------------- Staff Login Information -------------\n")
            print(records)
        else:
            print("\nError: No Employee Information found. cannot be viewed")

def view_admin_record_login():
    f = open("admin.txt", "r")
    records = f.read().strip()
    if records:
        print("\n------------- Admin Login Information Login -------------\n")
        print(records)
    else:
        print("\nError: No Admin Information found. cannot be viewed")

def admin_portal():
    global rooms
    rooms = []
    load_room_status()

    while True:
        print("\n------------- Admin -------------\n")
        print("1. Add New Room")
        # print("2. Remove Room")
        print("2. Edit Room")
        print("3. Display Rooms")
        print("4. View Check In Log")
        print("5. View Check Out Log")
        print("6. View Cancel Booking Log")
        print("7. Add New Employee")
        print("8. Add New Admin")
        print("9. View Employee Information Login")
        print("10. View Admin Information Login")
        print("11. Log-out")

        choice = input("\nChoose an option: ").strip()

        if choice == '1':
            add_new_room()

        # elif choice == '2':
        #     remove_room()

        elif choice == '2':
            edit_room()

        elif choice == '3':
            view_rooms()

        elif choice == '4':
            view_check_in_records()

        elif choice == '5':
            view_check_out_records()

        elif choice == '6':
            view_cancel_booking_records()

        elif choice == '7':
            new_employee()

        elif choice == '8':
            new_admin()

        elif choice == '9':
            view_employee_record_login()

        elif choice == '10':
            view_admin_record_login()

        elif choice == '11':
            print("\nReturn to the Log-in page...")
            main.main_portal()

        else:
            print("\nError: Invalid choice. Please try again.")

if __name__ == "__main__":
    admin_portal()