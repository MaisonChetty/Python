customer = {
    'name': 'John Doe',
    'age': 30,
    'is_verified': True
}

name = customer['name']
print("Customer name:", name)

age = customer.get('age', 0)
print("Customer age:", age)

customer['name'] = 'Jane Doe'
print("Updated customer name:", customer['name'])

customer['birthdate'] = '2002-01-01'
print("Customer birthdate added:", customer['birthdate'])

