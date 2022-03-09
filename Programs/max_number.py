# Simple list
numbers = [4, 5, 867, 43, 76, 56 ,2354]
max = numbers[0]

for number in numbers:
    if max < number:
        max = number

print(f"Max number is: {max}")

# Our simple matrix for example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Print matrix in the console
for row in matrix:
    print()
    for item in row:
        print(item, end=" ")

# Lists methods:

