# Simple program with using exception (try)
while True:
    try:
        age = int(input("Age: "))
        zero_error = 1 / age
        print(f"You age is: {age}")
        break
    except ZeroDivisionError:
        print("Age cant be a zero!")
    except ValueError:
        print("Invalid value!")
