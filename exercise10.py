numbers = [5, 3, 10, 9, 1]
placeholder = numbers[0]

for num in numbers:
    if num > placeholder:
        placeholder = num

print("The largest number is:", placeholder)