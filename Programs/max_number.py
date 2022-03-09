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

print("\n______________________________________________")
# Lists methods:
numbers.append(3)
print(f"Append number to list: {numbers}")
numbers.insert(1, 34)
print(f"Insert the number: {numbers}")
numbers.remove(4)
print(f"Remove number 4 from the list: {numbers}")
print(f"Number index 43 is: {numbers.index(43)}")
print(f"Number 43 is the list numbers or not? : {43 in numbers}")
print(f"Count of number 5 in the list: {numbers.count(5)}")
print(f"Remove last number in the list: {numbers.pop()}")
numbers.sort()
print(f"Sort list: {numbers}")
numbers.reverse()
print(f"Reverse list: {numbers}")
numbers2 = numbers.copy()
print(f"Second list the copy of first: {numbers2}")
numbers.clear()
print(f"Clear list: {numbers}")

print("___________________________________")
# Solution of task with list
numbers = [3, 6, 45, 234, 65, 78, 43 ,65 , 65]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(f"List uniques is: {uniques}")