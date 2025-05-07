# manage.py

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


def delete_password():
    website = input("Enter the website you want to delete")
    
    if website in passwords:
        comfirm = input(f"Warning: Are you sure you want to delete information about {website}? (y/n): ").strip().lower()
        if comfirm == 'y':
            del passwords[website]
            save_data(passwords)
            print("Password successfully deleted!")
        else:
            print("Operation canceled")
    else:
        print("Unable to find the website history")
    return