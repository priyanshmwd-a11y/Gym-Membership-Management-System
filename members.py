from storage import save_members
from validators import get_valid_name, get_valid_age, get_valid_phone

def member_menu(members):
    while True:
        print("\n--- Member Management ---")
        print("1. Add Member")
        print("2. View Members")
        print("3. Search Member")
        print("4. Update Member")
        print("5. Remove Member")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1": add_member(members)
        elif choice == "2": view_members(members)
        elif choice == "3": search_member(members)
        elif choice == "4": update_member(members)
        elif choice == "5": remove_member(members)
        elif choice == "6": break
        else: print("Invalid choice. Please select 1 to 6.")

def add_member(members):
    member_id = "GYM" + str(len(members) + 1).zfill(3)
    name = get_valid_name("Enter member name: ")
    age = get_valid_age("Enter member age: ")
    phone = get_valid_phone("Enter member phone number: ")
    members.append({"id": member_id, "name": name, "age": age, "phone": phone})
    save_members(members)
    print("Member added successfully!")
    print("Member ID:", member_id)

def view_members(members):
    print("\nAll Registered Members:")
    if not members:
        print("No members found.")
        return
    for member in members:
        print("ID:", member["id"])
        print("Name:", member["name"])
        print("Age:", member["age"])
        print("Phone:", member["phone"])
        print("Plan:", member.get("plan", "No membership"))
        print("Start Date:", member.get("start_date", "N/A"))
        print("Expiry Date:", member.get("expiry_date", "N/A"))
        print("Payment Status:", member.get("payment_status", "Pending"))
        print("-------------------------")

def search_member(members):
    search_id = input("Enter Member ID: ")
    for member in members:
        if member["id"].upper() == search_id.upper():
            print("\nMember Found!")
            for key in ["id", "name", "age", "phone"]:
                print(key.title() + ":", member[key])
            print("Plan:", member.get("plan", "No membership"))
            print("Expiry Date:", member.get("expiry_date", "N/A"))
            print("Payment Status:", member.get("payment_status", "Pending"))
            return
    print("Member not found.")

def update_member(members):
    update_id = input("Enter Member ID to update: ")
    for member in members:
        if member["id"].upper() == update_id.upper():
            member["name"] = get_valid_name("Enter new name: ")
            member["age"] = get_valid_age("Enter new age: ")
            member["phone"] = get_valid_phone("Enter new phone number: ")
            save_members(members)
            print("Member details updated successfully.")
            return
    print("Member not found.")

def remove_member(members):
    remove_id = input("Enter Member ID to remove: ")
    for member in members:
        if member["id"].upper() == remove_id.upper():
            print("Member found:", member["name"])
            if input("Are you sure you want to remove this member? (yes/no): ").lower() == "yes":
                members.remove(member)
                save_members(members)
                print("Member removed successfully.")
            else:
                print("Member was not removed.")
            return
    print("Member not found.")
