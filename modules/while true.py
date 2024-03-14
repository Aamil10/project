while True:
    print("1.Addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        from addition import *
        addition()

    elif choice == 2:
        from substraction import *
        substraction()

    elif choice == 3:
        from multiplication import *
        multiplication()

    elif choice == 4:
        from division import *
        division()

    elif choice == 5:
        print("!!EXIT!!")
        break
    else:
        print("**INVALID CHOICE**")