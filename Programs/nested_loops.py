for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 7, 8, 4, 2, 13, 6, 1, 0]

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "*"
    print(output)
