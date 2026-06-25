# =====================================
# AI Based Missing Person Detection System
# Simple Prototype
# =====================================

print("=====================================")
print(" AI BASED MISSING PERSON DETECTION ")
print("=====================================")

missing_person = input("Enter Missing Person Name: ")
age = input("Enter Age: ")
gender = input("Enter Gender: ")

print("\nMissing Person Registered Successfully!")

print("\nScanning CCTV Database...")
print("Processing Images...")
print("Checking Face Matches...")

result = input("\nIs the person found? (yes/no): ")

if result.lower() == "yes":

    location = input("Enter Location: ")

    print("\n=====================================")
    print(" ALERT : MISSING PERSON FOUND ")
    print("=====================================")
    print("Name     :", missing_person)
    print("Age      :", age)
    print("Gender   :", gender)
    print("Location :", location)
    print("Status   : Found")
    print("=====================================")

else:

    print("\n=====================================")
    print(" SEARCH IN PROGRESS ")
    print("=====================================")
    print("Name   :", missing_person)
    print("Status : Not Found")
    print("=====================================")

print("\nThank You For Using The System")
