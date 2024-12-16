import admin
import staff
import sys
import getpass

def getpass_asterisks(prompt=''):
    if sys.platform == 'win32':
        import msvcrt

        password = []
        print(prompt, end='', flush=True)

        while True:
            ch = msvcrt.getch()  # Get a single character from user

            if ch == b'\r' or ch == b'\n':  # Enter key pressed
                break

            elif ch == b'\x08':  # Backspace key pressed
                if password:
                    password.pop()
                    print('\b \b', end='', flush=True)  # Erase the last character

            else:
                password.append(ch.decode())
                print('*', end='', flush=True)  # Display asterisk

        print()  # Move to the next line after password input
        return ''.join(password)

    else:
        # UNIX-based system solution (Linux/macOS)
        password = getpass.getpass(prompt)  # getpass already hides input by default
        return password

def main_portal():
    print("\n----- Hotel Reservation -----")

    username = input("\nUsername: ")

    while True:
        password = getpass_asterisks("\nPassword: ")
        if len(password) >= 8:
            break
        else:
            print("\nError: Password must be at least 8 characters or more. Please try again.")

    login_success = False
    user_type = None

    try:
        f = open("admin.txt", "r")
        for line in f:
            if line.strip() == f"Username: {username}, Password: {password}":
                login_success = True
                user_type = "admin"
                break
        f.close()
    except FileNotFoundError:
        print("\nError: Admin login file not found.")

    if not login_success:
        try:
            f = open("staff.txt", "r")
            for line in f:
                if line.strip() == f"Username: {username}, Password: {password}":
                    login_success = True
                    user_type = "employee"
                    break
            f.close()
        except FileNotFoundError:
            print("\nError: Staff login file not found.")

    if login_success:
        print(f"\nLogin Success!\n\nWelcome {username}")
        if user_type == "admin":
            admin.admin_portal()
        elif user_type == "employee":
            staff.staff_portal()

    else:
        print("\nLogin failed. Please try again.")
        main_portal()

if __name__ == "__main__":
    main_portal()