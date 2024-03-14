class Calculator:
    def addition(self):
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        sum = a+b
        print(sum)

    def substraction(self):
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        sub = a-b
        print(sub)

    def multiplication(self):
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        mult = a*b
        print(mult)

    def division(self):
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        div = a/b
        print(div)
c = Calculator()

while True:
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    choice = int (input("Enter your choice: "))

    if choice == 1:
        c.addition()

    elif choice == 2:
        c.substraction()
        
    elif choice == 3:
        c.multiplication()

    elif choice == 4:
        c.division()
