vehicles= []
while True:
    print("options")
    print("1 - add vehicle")
    print("2 - change vehicle price")
    print("3 - display")
    print("4 - exit")
    choice=int(input("enter your choice: "))

    if choice == 1:
        name = input("enter vehicle name: ")
        price = int(input("enter vehicle price: "))
        num_wheels = int(input("enter number of wheels: "))
        vehicles.append({"name":name, "price":price, "num_wheels": num_wheels})

    elif choice == 3:
        print("select number of wheels: ")
        print("1- 2 wheeler")
        print("2- 3 wheeler")
        print("3- 4 wheeler")
        wheel_choice=int(input("enter your choice: "))
        print(f"{'name':<10}{'price':<10}{'number of wheels':10}")
        for vehicle in vehicles:
            if wheel_choice == 1 and vehicle['num_wheels']==2:
                print(f"{vehicle['name']:<10}{vehicle['price']:<10}{vehicle['num_wheels']:<10}")
            elif wheel_choice == 2 and vehicle['num_wheels']==3:
                print(f"{vehicle['name']:<10}{vehicle['price']:<10}{vehicle['num_wheels']:<10}")
            elif wheel_choice == 3 and vehicle['num_wheels'] == 4:
                print(f"{vehicle['name']:<10}{vehicle['price']:<10}{vehicle['num_wheels']:>9}")


    elif choice == 2:
        vehicle_name = input("Enter the name of the vehicle: ")
        new_price = float(input("Enter the new price: "))
        for vehicle in vehicles:
            if vehicle['name'] == vehicle_name:
                vehicle['price'] = new_price
                print("Price updated successfully.")
                break
        else:
            print("Vehicle not found.")
    elif choice == 4:
        print("!!EXIT!!")
        break
    else:
        print("!!invalid choice!!")