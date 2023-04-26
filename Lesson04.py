number = int(input("Enter a number: "))
summa = 0

while number != 0:
    last_num = number % 10
    summa += last_num
    if last_num == 5:
        print("The split is founded.")
        break
    number //=10
    print(f"The current amount of numbers: {summa}")

print(f"\nThe result amount of numbers: {summa}")
