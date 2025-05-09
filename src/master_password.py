#master_password.py

import json
import os
from config import MASTER_PASSWORD_FILE
import hashlib

def hash_encrypt(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def get_master():
    if not os.path.exists(MASTER_PASSWORD_FILE):
        return None
    with open(MASTER_PASSWORD_FILE, "r") as file:
        data = json.load(file)
        return data.get("master_password")

def set_master():
    print("Please insert Master Password you want to use:")
    data = input("Please set password with at least 8 characters\n")
    if len(data) < 8:
        print("Password too short! Operation canceled")
        return
    comfirm = input("Please insert again to comfirm:\n")
    if data == comfirm:
        encry = hash_encrypt(data)
        print("Master Password successfully set! Returning to authenticate")
        with open(MASTER_PASSWORD_FILE, "w") as file:
            json.dump({"master_password": encry}, file)
            return
    print("The passwords you entered are not the same! Operation canceled")
    return

def reset_master_password():
    master = get_master()
    old = input("Please insert your old Master Password:\n")
    if old == master:
        set_master()
    else:
        print("Master Password does not match! Operation Canceled")
    

def authenticate():
    master = get_master()

    if master == None:
        print("Please set a Master Password to secure your data for the first launch!")
        set_master()
        return authenticate()
    for i in range(4):
        password = input("Please insert Master Password:\n")
        if hash_encrypt(password) == master:
            print("Authentication successful!")
            return True
        else:
            print("Master Password incorrect! Please re-insert")
            print(f"{3 - i} more attempts remaining")
    print("Too many incorrect attempts! Program exiting...")
    return False