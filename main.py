while True:
    print("\n------------- Hotel Reservation System -------------\n")
    print("1. Employee")
    print("2. Admin")
    print("3. Exit")
    choice = input("\nChoose an option: ")

    if choice == '1':
        print("\n------------- Employee Login -------------\n")

        login_username = input("Enter Name: ")

        while True:
            login_password = input("Enter Password (8 characters or more): ")
            if len(login_password) >= 8:
                break
            else:
                print("\nPassword must be at least 8 characters or more. Please try again.\n")

        login_success = False

        f = open("staff.txt", "r")
        for line in f:
            if line.strip() == f"Name: {login_username}, Password: {login_password}":
                login_success = True
                break

        if login_success:
            print("\nLogin Success!")
            import staff

        else:
            print("\nLogin failed. Please try again.\n")

    elif choice == '2':
        print("\n------------- Admin Login -------------\n")

        admin_username = input("Enter Name: ")

        while True:
            admin_password = input("Enter Password (8 characters or more): ")
            if len(admin_password) >= 8:
                break
            else:
                print("\nPassword must be at least 8 characters. Please try again.\n")

        login_success = False

        f = open("admin.txt", "r")
        for line in f:
            if line.strip() == f"Name: {admin_username}, Password: {admin_password}":
                login_success = True
                break

        if login_success:
            print("\nLogin Success!\n")

            import admin
            admin.main()

        else:
            print("\nLogin failed. Please try again.\n")

    elif choice == '3':
        print("\nSystem Shutdown....\n")
        break

    else:
        print("\nInvalid option. Please try again.\n")