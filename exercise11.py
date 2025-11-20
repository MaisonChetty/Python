numbers = [5, 1, 5, 3,8, 8, 9]


for num in numbers:
    numbers.sort()
    numbers.count(num)
    if numbers.count(num) > 1:
        numbers.remove(num)

print(numbers)