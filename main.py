#main.py

from storage import load_data, save_data

passwords = load_data()

def add_password():
    website = input("name of website:\n")
    username = input("enter username:\n")
    password = input("enter password:\n")

    passwords[website] = {
        "username": username,
        "password": password
    }
    save_data(passwords)
    print("Password Saved!")

def view_password():
    if not passwords:
        print("no password saved currently")
        return
    print("Password saved:")
    for site, info in passwords.items():
        print(f"{site}:\nusername={info['username']}\npassword={info['password']}\n")

def main():
    while True:
        print("\n====== Passowrd Keeper Menu ======")
        print("Type 1 to add password")
        print("Type 2 to view all saved passwords")
        print("Type 3 to exit the program\n")

        choice = input("Please type in operation:\n")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            print("Data saved, now exiting")
            break
        else:
            print("Invalid input! Please re-enter")

if __name__ == "__main__":
    main()
    