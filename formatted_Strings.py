first = "Maison"
last = "Chetty"

# Old way of formatting strings
message = first + '[' + last + '] is a coder'
print(message)

# New way of formatting strings (f-strings)
msg = f'{first} [{last}] is a coder'
print(msg)


