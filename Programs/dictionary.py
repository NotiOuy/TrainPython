customer = {
    "name": "John Smith",
    "age": 23,
    "is_verified": True
}

print(f'Age: {customer["age"]}')
customer["birthdate"] = "04/22/1997"
print(f'Birthday: {customer["birthdate"]}')
print("____________________________")

# Example and solution of simple task
# Make from number input to words
phone = input("Phone: ")
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "@") + " "
print(output)