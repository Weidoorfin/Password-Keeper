# manage.py

from storage import load_data, save_data
from crypto import hash_enpcrypt, hash_decrypt

passwords = load_data()


def add_password():
    website = input("name of website:\n")
    username = input("enter username:\n")
    password = input("enter password:\n")

    website = hash_enpcrypt(website)
    username = hash_enpcrypt(username)
    password = hash_enpcrypt(password)

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
        website = hash_decrypt(site)
        username = hash_decrypt(info['username'])
        password = hash_decrypt(info['password'])
        print(f"{website}:\nusername:{username}\npassword:{password}\n")


def delete_password():
    website = input("Enter the website you want to delete:\n")
    
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