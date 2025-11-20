def greet_user(first_Name, last_Name):
    print(f"HI {first_Name} {last_Name}!")
    print("Welcome aboard")


full_name = input("Enter your  Full Name: ")
first_Name, last_Name = full_name.split(" ")

print("starting...")
greet_user(first_Name, last_Name)
print("finishing...")
