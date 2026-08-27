# Task 4: Fibonacci Sequence

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    first = 0
    second = 1

    print("Fibonacci sequence:")

    for _ in range(n):
        print(first, end=" ")
        next_number = first + second
        first = second
        second = next_number
