def addition():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    sum = a + b
    print(sum)


def substraction():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    subs = a - b
    print(subs)


def multiplication():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    mult = a * b
    print(mult)


def division():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    div = a / b
    print(div)


while True:
    print("1.Addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        addition()

    elif choice == 2:
        substraction()

    elif choice == 3:
        multiplication()

    elif choice == 4:
        division()

    elif choice == 5:
        print("!!EXIT!!")
        break
    else:
        print("**INVALID CHOICE**")