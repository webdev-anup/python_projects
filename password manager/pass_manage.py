pwd = input("What is the master password? ")

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print(f"User: {user}, Password: {passw}")
    except FileNotFoundError:
        print("❌ No passwords saved yet! Please add a password first.")


def add():
    name = input("Account name: ")
    pwd = input("password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
    print("✅ Password added successfully!")

    

mode = input("Would you like to add a new password or view existing ones? (add/view), press q to quit? ").lower()

if mode == "q":
    raise SystemExit

if mode == "view":
    view()
elif mode == "add":
    add()
else:
    print("Invalid mode.")