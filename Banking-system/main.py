from bank import BankSystem

bank = BankSystem()

while True:
    print("\n-------- Welcome to the Banking System --------\n")
    print("1.Register")
    print("2.Login")
    print("3.Deposit")
    print("4.Withdraw")
    print("5.Balance")
    print("6.Transaction history")
    print("7.Delete all records.")
    print("8.Exit")
    print("\n------------------------------------------\n")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        pin = input("Set PIN: ")
        bank.register(name,pin)
    
    elif choice == 2:
        user_id = int(input("Enter User ID: ")) 
        pin = input("Enter PIN: ") 
        bank.login(user_id, pin)
    
    elif choice == 3:
        amount = float(input("Enter amount: ")) 
        bank.deposit(amount)

    elif choice == 4:
        amount = float(input("Enter amount: ")) 
        bank.withdraw(amount)

    elif choice == 5:
        bank.check_balance()

    elif choice == 6:
        bank.transaction_history()

    elif choice == 7:
        bank.delete_all_data()

    elif choice == 8:
        break

    else:
        print("Invalid Choice!!")