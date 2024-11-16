import main
import random
import string
from datetime import datetime

class Room:
    def __init__(self, room_number, is_available, room_type = "", price_per_night = 0):
        self.room_number = room_number
        self.is_available = is_available
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.guest_name = None
        self.check_in_time = None
        self.nights_stay = 0
        self.total_price = 0
        self.reference_number = None

    def check_in(self, guest_name, check_in_time, nights_stay, reference_number):
        self.guest_name = guest_name
        self.check_in_time = check_in_time
        self.reference_number = reference_number
        self.nights_stay = nights_stay
        self.total_price = self.price_per_night * nights_stay
        self.is_available = False
        self.update_room_status_file()

    def check_out(self):
        self.is_available = True
        self.guest_name = None
        self.check_in_time = None
        self.reference_number = None
        self.nights_stay = 0
        self.total_price = 0
        self.update_room_status_file()

    def display_info(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Booked"

        print("Room", self.room_number, "-", status)
        print("Room Type:", self.room_type)
        print(f"Price per night: ₱ {self.price_per_night}\n")

    def update_room_status_file(self):
        with open("room_status.txt", "w") as f:
            for room in rooms:
                status = "Available" if room.is_available else "Booked"
                f.write(f"Room {room.room_number}, Status: {status}, Room Type: {room.room_type}, Price per night: {room.price_per_night} PHP\n")

def generate_reference_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def view_check_in_records():
    reference_number = input("\nEnter reference number to view check-in details: ").strip()
    try:
        f = open("check_in.txt", "r", encoding="utf-8")
        records = f.readlines()
        for i in range(0, len(records), 10):  # Each record is 10 lines, so we step by 10
                record = records[i:i + 10]  # Slice out a single record
                ref_no = record[0].split(":")[1].strip()  # Get reference number from the first line

                records = [line for line in records if line.strip()]

                if reference_number == ref_no:
                # If it is match the reference number, the details in the required format will print
                    print("\n------------- View Customer Check In Information -------------\n")
                    print(record[0].strip())  # Reference Number
                    print(record[1].strip())  # Guest Name
                    print(record[2].strip())  # Contact No
                    print(record[3].strip())  # Address
                    print(record[4].strip())  # Email
                    print(record[5].strip())  # Room Number
                    print(record[6].strip())  # Room Type
                    print(record[7].strip())  # Check In Time
                    print(record[8].strip())  # Night Stay
                    print(record[9].strip())  # Total Price
                    break

    except Exception:
        print("\nSorry, no record found for the provided reference number.")

def view_rooms():
    if rooms:
        print("\n------------- Room Information -------------\n")
        for room in rooms:
            room.display_info()
    else:
        print("\nNo Room Information Found.")

def load_room_status():
    global rooms
    rooms.clear()
    try:
        f = open("room_status.txt", "r")
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(", ")

            try:
                room_number = int(parts[0].split(" ")[1])
                status = parts[1].split(": ")[1]
                room_type = parts[2].split(": ")[1]
                price_per_night = int(parts[3].split(": ")[1].split()[0])

                room = Room(room_number, status == "Available", room_type, price_per_night)
                rooms.append(room)

            except (IndexError, ValueError):
                print(f"\nSkipping invalid room entry: {line.strip()}")

    except FileNotFoundError:
        pass

rooms = []
load_room_status()

def staff_portal():
    while True:
        print("\n------------- Employee -------------\n")
        print("1. Check In / Booking")
        print("2. Cancel Booking")
        print("3. Check Out")
        print("4. Display Rooms")
        print("5. View Customer Check In Record")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            while True:
                if not rooms:
                    print("\nSorry No Room Record Information. Cannot be Check In")
                    break

                while True:
                    guest_name = input("\nEnter Guest Name: ")
                    if guest_name.replace(" ", "").isalpha():
                        break
                    else:
                        print("\nName must only contain alphabetic characters.")

                while True:
                    contact_number = input("\nEnter Contact number (11 digits): ")
                    if len(contact_number) == 11 and contact_number.isdigit():
                        break
                    else:
                        print("\nPlease enter a valid 11-digit contact number.")

                while True:
                    address = input("\nEnter Address: ")
                    if address.replace(" ", "").isalpha():
                        break
                    else:
                        print("\nName must only contain alphabetic characters.")

                while True:
                    email = input("\nEnter Email Address: ")
                    if email.endswith("@gmail.com"):
                        break
                    else:
                        print("\nSorry, is it's not a valid Gmail Address. Please try again.")

                while True:
                    try:
                        room_number = int(input("\nEnter Room Number to Check In: "))

                        room = None
                        for r in rooms:
                            if r.room_number == room_number:
                                room = r
                                break

                        if room:
                            if room.is_available:
                                while True:
                                    check_in_day = input("\nEnter Arrival Date (MM/DD/YYYY) in Numerical: ")

                                    try:
                                        check_in_day = datetime.strptime(f"{check_in_day}","%m/%d/%Y")
                                        today = datetime.now().date()

                                        if check_in_day.date() < today:
                                            print("\nInvalid input. Please enter a future date, not a past date.")

                                        else:
                                            break

                                    except ValueError:
                                        print("\nInvalid day format. Please use (MM/DD/YYYY) in numerical.")

                                while True:
                                    try:
                                        check_in_hour_input = int(input("\nEnter Check in Hour (1-12): "))

                                        if 1 <= check_in_hour_input <= 12:
                                            am_pm = input("\nEnter it is AM or PM?: ").strip().upper()

                                            if am_pm in ["AM", "PM"]:
                                                hour = check_in_hour_input
                                                if am_pm == "AM" and hour == 12:
                                                    hour = 12
                                                elif am_pm == "PM" and hour != 12:
                                                    hour += 12

                                                check_in_time = check_in_day.replace(hour=hour, minute=0)
                                                check_in_time_str = check_in_time.strftime(f"%m/%d/%Y %I:%M %p")
                                                break

                                            else:
                                                print("\nInvalid AM/PM input. Please enter 'AM' or 'PM'.")

                                        else:
                                            print("\nInvalid hour. Please enter a number between 1 and 12.")

                                    except ValueError:
                                        print("\nInvalid input. Please enter a number between 1 and 12 for hour.")

                                while True:
                                    try:
                                        nights_stay = int(input("\nEnter How many days stay in the hotel?: "))
                                        break

                                    except ValueError:
                                        print("\nInvalid input. Please enter numerical")

                                reference_number = generate_reference_number()
                                room.check_in(guest_name, check_in_time, nights_stay, reference_number)

                                f = open("check_in.txt", "a", encoding="utf-8")
                                f.write(f"Reference Number: {reference_number}\nGuest: {guest_name}\nContact No: {contact_number}\nAddress: {address}\nEmail: {email}\nRoom: {room_number}\nRoom Type: {room.room_type}\nCheck In: {check_in_time_str}\nNight Stay: {nights_stay}\nTotal Price: ₱ {room.total_price}\n\n")
                                f.close()

                                print(f"\nReference Number: {reference_number}\nRoom {room_number} booked.\nCheck-in time is {check_in_time_str}.\nRoom Type: {room.room_type}\nNight Stay: {nights_stay}\nTotal Price is: ₱ {room.total_price}")

                                break
                            else:
                                print(f"\nRoom {room_number} is already booked.")
                        else:
                            print("\nInvalid room number.")

                    except ValueError:
                        print("\nPlease enter a valid room number")
                break

        elif choice == '2':
            while True:
                if not rooms:
                    print("Sorry No Room Record Information. Cannot be Cancel Booking")
                    break

                print("\n------------- Room Information -------------\n")
                for room in rooms:
                    room.display_info()

                try:
                    room_number = int(input("\nEnter Room Number to Cancel Booking: "))

                    room = None
                    for r in rooms:
                        if r.room_number == room_number:
                            room = r
                            break

                    if room:
                        if not room.is_available:
                            cancel_booking = datetime.now()
                            cancel_booking_time = cancel_booking.strftime("%m/%d/%Y %I:%M %p")

                            f = open("cancel_booking.txt", "a")
                            f.write(f"Room: {room_number}\nCancellation Time: {cancel_booking_time}\n\n")
                            f.close()

                            room.check_out()
                            print(f"\nRoom {room_number} has been Canceled.")
                            print(f"Cancellation Time: {cancel_booking_time}.")

                        else:
                            print(f"\nRoom {room_number} is already available.")
                            break

                    else:
                        print("\nInvalid room number.")

                except ValueError:
                    print("\nPlease enter a valid room number.")

                while True:
                    print("\nDo you want to continue?")
                    print("1. Yes")
                    print("2. No")

                    again = input("\nChoose an option: ").strip()

                    if again == '1':
                        break

                    elif again == '2':
                        print("\nReturning to the main menu...")
                        staff_portal()

                    else:
                        print("\nInvalid input. Please enter '1' to continue cancel booking or '2' to return to the main menu.")

        elif choice == '3':
            while True:
                if not rooms:
                    print("\nSorry No Room Record Information. Cannot be Check Out")
                    break
                print("\n------------- Room Information ------------\n")

                for room in rooms:
                    room.display_info()

                try:
                    room_number = int(input("\nEnter Room Number to Check Out: "))

                    room = None
                    for r in rooms:
                        if r.room_number == room_number:
                            room = r
                            break

                    if room:
                        if not room.is_available:
                            check_out_time = datetime.now()
                            check_out_time_str = check_out_time.strftime("%m/%d/%Y %I:%M %p")

                            f = open("check_out.txt", "a")
                            f.write(f"Room: {room_number}\nCheck Out: {check_out_time_str}\n\n")
                            f.close()

                            room.check_out()

                            print(f"\nRoom {room_number} has been checked out.")
                            print(f"Check-out time: {check_out_time_str}.")
                        else:
                            print(f"\nRoom {room_number} is already available.")
                            break
                    else:
                        print("\nInvalid room number.")

                except ValueError:
                    print("\nPlease enter a valid room number.")

                while True:
                    print("\nDo you want to continue?")
                    print("1. Yes")
                    print("2. No")

                    again = input("Choose an option: ").strip()

                    if again == '1':
                        break

                    elif again == '2':
                        print("\nReturning to the main menu...")
                        staff_portal()

                    else:
                        print("\nInvalid input. Please enter '1' to continue check out or '2' to return to the main menu.")

        elif choice == '4':
            view_rooms()

        elif choice == '5':
            view_check_in_records()

        elif choice == '6':
            print("\nReturn to the menu...")
            main.main_portal()

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    staff_portal()