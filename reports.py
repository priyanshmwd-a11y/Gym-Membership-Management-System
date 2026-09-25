def reports_menu(members):
    while True:
        print("\n--- Reports & Analytics ---")
        print("1. Total Members")
        print("2. Membership Summary")
        print("3. Payment Summary")
        print("4. Revenue Summary")
        print("5. Plan-wise Summary")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1": print("\nTotal Members:", len(members))
        elif choice == "2": membership_summary(members)
        elif choice == "3": payment_summary(members)
        elif choice == "4": revenue_summary(members)
        elif choice == "5": plan_summary(members)
        elif choice == "6": break
        else: print("Invalid choice. Please select 1 to 6.")

def membership_summary(members):
    active = sum(1 for m in members if "plan" in m)
    print("\nMembers with Membership:", active)
    print("Members without Membership:", len(members) - active)

def payment_summary(members):
    paid = sum(1 for m in members if m.get("payment_status") == "Paid")
    print("\nPayment Summary:")
    print("Paid Members:", paid)
    print("Pending Members:", len(members) - paid)

def revenue_summary(members):
    revenue = sum(m.get("fee", 0) for m in members if m.get("payment_status") == "Paid")
    print("\nRevenue Summary:")
    print("Total Revenue: ₹", revenue)

def plan_summary(members):
    print("\nPlan-wise Summary:")
    print("Monthly Members:", sum(1 for m in members if m.get("plan") == "Monthly"))
    print("Quarterly Members:", sum(1 for m in members if m.get("plan") == "Quarterly"))
    print("Yearly Members:", sum(1 for m in members if m.get("plan") == "Yearly"))
