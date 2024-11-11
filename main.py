import staff
import admin

while True:
    print("\n------------- Hotel Reservation System -------------\n")
    print("1. Employee")
    print("2. Admin")
    print("3. Exit")
    choice = input("\nChoose an option: ")

    if choice == '1':
        print("\n------------- Employee Login -------------")

        login_username = input("\nEnter Name: ")

        while True:
            login_password = input("\nEnter Password (8 characters or more): ")
            if len(login_password) >= 8:
                break
            else:
                print("\nPassword must be at least 8 characters or more. Please try again.")

        login_success = False

        f = open("staff.txt", "r")
        for line in f:
            if line.strip() == f"Name: {login_username}, Password: {login_password}":
                login_success = True
                break

        if login_success:
            print("\nLogin Success!")
            staff.staff_portal()

        else:
            print("\nLogin failed. Please try again.")

    elif choice == '2':
        print("\n------------- Admin Login -------------")

        admin_username = input("\nEnter Name: ")

        while True:
            admin_password = input("\nEnter Password (8 characters or more): ")
            if len(admin_password) >= 8:
                break
            else:
                print("\nPassword must be at least 8 characters. Please try again.")

        login_success = False

        f = open("admin.txt", "r")
        for line in f:
            if line.strip() == f"Name: {admin_username}, Password: {admin_password}":
                login_success = True
                break

        if login_success:
            print("\nLogin Success!")
            admin.admin_portal()

        else:
            print("\nLogin failed. Please try again.")

    elif choice == '3':
        print("\nSystem Shutdown....")
        break

    else:
        print("\nInvalid option. Please try again.")