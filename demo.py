
n = int(input("Enter the number of integers: "))
numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

# Check if the input length matches n
if len(numbers) != n:
    print(f"Error: Expected {n} numbers but got {len(numbers)}.")
else:
    print("You entered:", numbers)
