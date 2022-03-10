import random


x = 0
y = 1
for i in range(2):
    print(f"{x}| {random.random()}")
    print(f"{y}| {random.randint(0, 100)}")
    x += 2
    y += 3

print("==========================")
numbers = [23, 43, 54, 64, 23, 54, 0]
print(f"Random number from the list is: {random.choice(numbers)}")

print("============================")


class Dice:
    @staticmethod
    def roll():
        first_number = random.randint(0, 10)
        second_number = random.randint(0, 10)
        return first_number, second_number


dice = Dice()
print(dice.roll())

