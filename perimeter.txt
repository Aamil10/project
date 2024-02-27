while True:
    print("---options---")
    print("1 - perimeter of circle")
    print("2 - perimeter of rectangle")
    print("3 - perimeter of square")
    print("4 - Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius: "))
        perimeter = 2 * 3.14 * radius
        print(perimeter)

    elif choice == 2:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        perimeter = 2 * (length + width)
        print(perimeter)

    elif choice == 3:
        a = float(input("Enter the side: "))
        perimeter = 4 * a
        print(perimeter)

    elif choice == 4:
        print("!!EXIT!!")
        break
    else:
        print("invalid choice")