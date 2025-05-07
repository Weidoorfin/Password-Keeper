#main.py

import manage

def main():
    while True:
        print("\n====== Passowrd Keeper Menu ======")
        print("Type 1 to add password")
        print("Type 2 to view all saved passwords")
        print("Type 3 to delete a password")
        print("Type 0 to exit the program\n")

        choice = input("Please type in operation:\n")
        if choice == "1":
            manage.add_password()
        elif choice == "2":
            manage.view_password()
        elif choice == "3":
            manage.delete_password()
        elif choice == "0":
            print("Data saved, now exiting")
            break
        else:
            print("Invalid input! Please re-enter")

if __name__ == "__main__":
    main()
    