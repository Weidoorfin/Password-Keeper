# Password Keeper

An simple program that helps you store you account and password information locally, self developed.

Version: **v1.2.1**

---

## Features
- Adding a new password
- View all existing passwords (in plain text)
- Developed a master password control for security
- Using json to store all local data
- Interaction based on command input
- Delete an existing password

---

## Project Structure
```
Passwork-Keeper/
│
├── README.md
├── .gitignore
│
├── data/
│   ├── data.json
│   └── master_password.json
│
├── src/
│   ├── main.py
│   ├── manager.py
│   ├── storage.py
|   ├── config.py
│   └── master_password.py
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

1. Input command base on the instructions

---

## Update Log

### v1.2.1 (2025-05-08)

- Reconstruct of the project, sorting different file into different folders, planning for future development

---

## Warning
- Never upload `*.json` with real passwords to Github!
- `*.json` has been ignored by including file names in `.gitignore`

---

## Future Plans
- Hide Password with `*`
- Search password function
- Encryption of password
- GUI interface
- Remote access


> Made by Weidoorfin