numbers = [5, 2, 5, 8, 9]
numbers.append(3)
print(numbers)

numbers.insert(2, 7)
print(numbers)

numbers.remove(8)
print(numbers)

numbers.pop()
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.index(5))

print(numbers.count(5))

numbers2 = numbers.copy()
print(numbers2)

numbers.clear()
print(numbers)