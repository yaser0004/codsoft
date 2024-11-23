while True:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    print("\nChoose an operation:")
    print("1:Addition(+)")
    print("2:Subtraction(-)")
    print("3:Multiplication(*)")
    print("4:Division(/)")
    operation=input("\nEnter the number corresponding to the operation:")
    if operation=="1":
        result=num1+num2
        print(f"\nResult = {result}")
    elif operation=="2":
        result=num1-num2
        print(f"\nResult = {result}")
    elif operation=="3":
        result=num1*num2
        print(f"\nResult = {result}")
    elif operation=="4":
        if num2!=0:
            result=num1/num2
            print(f"\nResult = {result}")
        else:
            print("\nError:Division by zero is not allowed.")
    else:
        print("Invalid operation choice.")
    continue_choice=input("\nDo you want to perform another operation? (yes/no):").strip().lower()
    if continue_choice!="yes":
        print("Exiting the calculator. Goodbye!")
        break
