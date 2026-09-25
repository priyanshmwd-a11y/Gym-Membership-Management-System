def get_valid_name(prompt):
    name = input(prompt)
    while name.strip() == "":
        print("Name cannot be empty.")
        name = input(prompt)
    return name

def get_valid_age(prompt):
    age = input(prompt)
    while not age.isdigit() or int(age) < 1 or int(age) > 100:
        print("Please enter a valid age between 1 and 100.")
        age = input(prompt)
    return age

def get_valid_phone(prompt):
    phone = input(prompt)
    while not phone.isdigit() or len(phone) != 10:
        print("Please enter a valid 10-digit phone number.")
        phone = input(prompt)
    return phone

def get_valid_payment_method():
    method = input("Enter payment method (Cash/UPI/Card): ")
    while method.lower() not in ["cash", "upi", "card"]:
        print("Please enter Cash, UPI, or Card.")
        method = input("Enter payment method (Cash/UPI/Card): ")
    return method
