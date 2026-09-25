from storage import load_members
from members import member_menu
from memberships import membership_menu
from reports import reports_menu

members = load_members()

print("GYM MEMBERSHIP MANAGEMENT SYSTEM")
print("Welcome to the Gym!")

while True:
    print("\n========================================")
    print("   GYM MEMBERSHIP MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Member Management")
    print("2. Membership & Payment")
    print("3. Reports & Analytics")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        member_menu(members)
    elif choice == "2":
        membership_menu(members)
    elif choice == "3":
        reports_menu(members)
    elif choice == "4":
        print("Thank you for using the Gym Management System!")
        break
    else:
        print("Invalid choice. Please select 1 to 4.")
