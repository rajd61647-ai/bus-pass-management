def display_menu():
    print("\n===== BUS PASS MANAGEMENT SYSTEM =====")
    print("1. Add Bus Pass")
    print("2. View All Passes")
    print("3. Search Pass by ID")
    print("4. Delete Pass by ID")
    print("5. Exit")


# List to store bus pass details
bus_passes = []


def add_pass():
    print("\n--- Add New Bus Pass ---")
    pass_id = input("Enter Pass ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    route = input("Enter Bus Route: ")

    bus_pass = {
        "Pass ID": pass_id,
        "Name": name,
        "Age": age,
        "Route": route
    }

    bus_passes.append(bus_pass)
    print("✔ Bus Pass Added Successfully!")


def view_passes():
    print("\n--- All Bus Passes ---")
    if not bus_passes:
        print("No records found.")
        return

    for bp in bus_passes:
        print(f"ID: {bp['Pass ID']} | Name: {bp['Name']} | Age: {bp['Age']} | Route: {bp['Route']}")


def search_pass():
    print("\n--- Search Bus Pass ---")
    search_id = input("Enter Pass ID to search: ")

    for bp in bus_passes:
        if bp["Pass ID"] == search_id:
            print("✔ Pass Found:")
            print(f"ID: {bp['Pass ID']}")
            print(f"Name: {bp['Name']}")
            print(f"Age: {bp['Age']}")
            print(f"Route: {bp['Route']}")
            return

    print("✘ No Pass found with this ID.")


def delete_pass():
    print("\n--- Delete Bus Pass ---")
    delete_id = input("Enter Pass ID to delete: ")

    for bp in bus_passes:
        if bp["Pass ID"] == delete_id:
            bus_passes.remove(bp)
            print("✔ Pass Deleted Successfully!")
            return

    print("✘ No Pass found with this ID.")


# Main Program Loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_pass()
    elif choice == '2':
        view_passes()
    elif choice == '3':
        search_pass()
    elif choice == '4':
        delete_pass()
    elif choice == '5':
        print("Exiting Program... Thank You!")
        break
    else:
        print("Invalid choice! Enter between 1-5.")
