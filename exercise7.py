weight = int(input("Enter your weight: "))
unit = input("Is your weight in (K)g or (L)bs: ").upper()

if unit == "K":
    converted_weight = weight / 0.45
    print(f"Your weight in pounds is: {converted_weight} lbs")
elif unit == "L":
    converted_weight = weight * 0.45
    print(f"Your weight in kilograms is: {converted_weight} kg")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")

