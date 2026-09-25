from datetime import date, timedelta
from storage import save_members
from validators import get_valid_payment_method

PLANS = {
    "1": ("Monthly", 1000, 30),
    "2": ("Quarterly", 2700, 90),
    "3": ("Yearly", 9000, 365)
}

def membership_menu(members):
    while True:
        print("\n--- Membership & Payment ---")
        print("1. View Membership Plans")
        print("2. Assign Membership")
        print("3. Record Payment")
        print("4. Renew Membership")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1": view_plans()
        elif choice == "2": assign_membership(members)
        elif choice == "3": record_payment(members)
        elif choice == "4": renew_membership(members)
        elif choice == "5": break
        else: print("Invalid choice. Please select 1 to 5.")

def view_plans():
    print("\nAvailable Membership Plans:")
    print("1. Monthly   - ₹1000")
    print("2. Quarterly - ₹2700")
    print("3. Yearly    - ₹9000")

def choose_plan():
    view_plans()
    choice = input("Choose membership plan: ")
    if choice not in PLANS:
        print("Invalid plan.")
        return None
    return PLANS[choice]

def find_member(members, member_id):
    for member in members:
        if member["id"].upper() == member_id.upper():
            return member
    return None

def apply_plan(member, plan):
    name, fee, days = plan
    member["plan"] = name
    member["fee"] = fee
    member["start_date"] = str(date.today())
    member["expiry_date"] = str(date.today() + timedelta(days=days))
    member["payment_status"] = "Pending"

def assign_membership(members):
    member = find_member(members, input("Enter Member ID: "))
    if member is None:
        print("Member not found.")
        return
    plan = choose_plan()
    if plan is None: return
    apply_plan(member, plan)
    save_members(members)
    print("Membership assigned successfully!")
    print("Member:", member["name"])
    print("Plan:", member["plan"])
    print("Fee: ₹", member["fee"])
    print("Expiry Date:", member["expiry_date"])

def record_payment(members):
    member = find_member(members, input("Enter Member ID: "))
    if member is None:
        print("Member not found.")
        return
    if "plan" not in member:
        print("This member does not have a membership plan yet.")
        return
    print("Member:", member["name"])
    print("Plan:", member["plan"])
    print("Amount Due: ₹", member["fee"])
    member["payment_method"] = get_valid_payment_method()
    member["payment_status"] = "Paid"
    save_members(members)
    print("Payment recorded successfully!")

def renew_membership(members):
    member = find_member(members, input("Enter Member ID: "))
    if member is None:
        print("Member not found.")
        return
    print("Current Plan:", member.get("plan", "No plan"))
    plan = choose_plan()
    if plan is None: return
    apply_plan(member, plan)
    save_members(members)
    print("Membership renewed successfully!")
    print("Member:", member["name"])
    print("New Plan:", member["plan"])
    print("Amount Due: ₹", member["fee"])
    print("New Expiry Date:", member["expiry_date"])
