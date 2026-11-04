# Initial balance
balance = 1000.0

print("=== Welcome to the ATM ===")

while True:
    print("\nChoose a transaction:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    
    try:
        option = int(input("Enter The Task Transaction (1/2/3/4): "))
    except ValueError:
        print("❌ Invalid input! Please enter a number between 1 and 4.")
        continue  # Loop ko dobara start kar dega bina error diye

    if option == 1:
        print(f"💰 Your current balance is: ₹{balance}")

    elif option == 2:
        withdraw = float(input("Enter amount to withdraw: ₹"))
        
        if withdraw <= 0:
            print("❌ Invalid amount! Please enter a value greater than 0.")
        elif balance >= withdraw:
            balance -= withdraw  # Yeh actual balance ko update karega
            print("✅ Transaction Successful!")
            print(f"Your new balance is: ₹{balance}")
        else:
            print("❌ Insufficient Balance!")
    
    elif option == 3:
        deposit = float(input("Enter amount to deposit: ₹"))
        
        if deposit <= 0:
            print("❌ Invalid amount! Please deposit a positive value.")
        else:
            balance += deposit  # Yeh actual balance ko update karega
            print("✅ Transaction Successful!")
            print(f"Total balance now is: ₹{balance}")
    
    elif option == 4:
        print("\n🙏 Thank you for choosing us! Have a great day.")
        break
    
    else:
        print("❌ Please select a valid transaction option (1-4).")