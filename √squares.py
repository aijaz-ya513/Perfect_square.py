import math

while True:
    print("\n--- MENU ---")
    print("1. Check if a number is a perfect square")
    print("2. Show the square of a number")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice =='1':
        num = int(input("Enter a number: "))
        root = math.isqrt(num)
        if root * root == num:
            print(f"{num} is a perfect square.")
        else:
            print(f"{num} is NOT a perfect square.")

    elif choice == '2':
        num = int(input("Enter a number: "))
        print(f"The square of {num} is {num ** 2}")

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")