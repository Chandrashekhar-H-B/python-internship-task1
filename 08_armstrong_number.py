# Task 8: Armstrong Number

num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative number.")
else:
    order = len(str(num))
    sum_val = sum(int(digit) ** order for digit in str(num))

    if num == sum_val:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
