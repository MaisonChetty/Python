phoneNumber = input("Enter your phone number: ")

for char in phoneNumber:
    if char == '0':
        print("Zero", end="")
    elif char == '1':
        print("One", end="")
    elif char == '2':
        print("Two", end="")
    elif char == '3':
        print("Three", end="")
    elif char == '4':
        print("Four", end="")
    elif char == '5':
        print("Five", end="")
    elif char == '6':
        print("Six", end="")
    elif char == '7':
        print("Seven", end="")
    elif char == '8':
        print("Eight", end="")
    elif char == '9':
        print("Nine", end="")
    else:
        print("Invalid character", end="")

print("\n-----------------")

print("\nUsing dictionary:")

diggits = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
    }

for char in phoneNumber:
    print(diggits.get(char, "Invalid character"), end="")