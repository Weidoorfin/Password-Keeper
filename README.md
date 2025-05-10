# Password Keeper

An simple program that helps you store you account and password information locally, self developed.

Version: **v1.3.1**

---

## Features
- Adding a new password
- View all existing passwords (in plain text)
- Delete an existing password
- Edit an existing password
- Developed a master password control for security
- Using json to store all local data
- Interaction based on command input
- Import XOR encryption by C module

---

## Project Structure
```
Passwork-Keeper/
│
├── README.md
├── .gitignore
│
├── data/   #Folder & file generates upon first execution
│   ├── data.json
│   └── master_password.json
│
├── src/
│   ├── main.py
│   ├── manager.py
│   ├── storage.py
|   ├── config.py
|   ├── crypto.py
│   └── master_password.py
│
├── build/
│   └── crypto.dll
│
├── clib/
|   ├── crypto.c
|   └── crypto.h
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
python src/main.py
```

4. Input command base on the instructions

---

## Update Log

### v1.3.1 (2025-05-10)

- Introducing a new feature: **Edit Password** to change one of your existing passwords

---

## Warning
- Never upload `*.json` with real passwords to Github!
- `*.json` has been ignored by including file names in `.gitignore`

---

## Future Plans
- Hide Password with `*`
- Search password function
- GUI interface (planned v2.0)
- Remote access (planned v3.0)


> Made by Weidoorfin