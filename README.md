# Password Keeper

An simple program that helps you store you account and password information locally

Version: **v1.2**

---

## Features
- Adding a new password
- View all existing passwords (in plain text)
- Developed a master password control for security **(*NEW)**
- Using json to store all local data
- Interaction based on command input
- Delete an existing password

---

## Project Structure
```
Passwork-Keeper/
├── main.py                 # Program Interface
├── manage.py               # Program Operations
├── storage.py              # Management of adding or loading password
├── master_password.py      # Management of master password
├── data.json               # Local file that stores data (in .gitignore)
├── master_password.json    # Local file that stores master password (in .gitignore)
├── README.md               # Project Instruction
├── .gitignore              # ignoring private files, mostly *.json
```

---

## Manual
1. Makesure you have installed Python 3
2. Clone the project with given commands below:

```bash
git clone https://github.com/Weidoorfin/Passwork-Keeper.git
cd Passwork-Keeper
```
3. Execute the program by:

```bash
python main.py
```

4. Input command based on instruction (adding/viewing)

---

## Update Log

### v1.2 (2025-05-08)

- Adding a new module `master_password.py`, secure the data by using a master password control

---

## Warning
- Never upload `*.json` with real passwords to Github!
- `*.json` has been ignored in `.gitignore`, no further action needed

---

## Future Plans
- Hide Password with `*`
- Search password function
- Encryption of password
- GUI interface
- Remote access


> Made by Weidoorfin