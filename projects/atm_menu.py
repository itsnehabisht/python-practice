def atm():
    balance = 5000
    while True:
        
        choice = int(input('''
        1. Check Balance
        2. Deposit
        3. Withdraw
        4. Exit
                     
        enter choice: '''))
    
        if choice == 1:
            print("your balance:", balance)
        elif choice == 2:
            deposit = float(input("Enter deposit amount: "))
            balance = balance + deposit
            print("your new balance:", balance)
        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance = balance - amount
                print("your new balance:", balance)
            else:
                print("Insufficient funds")
        elif choice == 4:
            print("Thank you")
            break
        else:
            print("Invalid choice")
        again = input("Do you want another transaction? y/n: ")

        if again != "y":
            break
atm()