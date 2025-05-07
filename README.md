# Password Keeper

An simple program that helps you store you account and password information locally

Version: **v1.1**

---

## Features
- Adding a new password
- View all existing passwords (in plain text)
- Using json to store all local data
- Interaction based on command input
- Delete an existing password

---

## Project Structure
```
Passwork-Keeper/
├── main.py          # Program Interface
├── manage.py        # Program Operations (NEW)
├── storage.py       # Management of adding or loading password
├── data.json        # Local file that stores data (inside .gitignore)
├── README.md        # Project Instruction
├── .gitignore       # ignoring private files such as data.json
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

## Update Blog

### v1.1 (2025-05-07)

- Reconstruct of the project:  
Seperating operations and user interfact, store operation into `manage.py`
- Adding new **delete password** function

---

## Warning
- Never upload `data.json` with real passwords to Github!
- `data.json` has been ignored in `.gitignore`, no further action needed

---

## Future Plans
- Hide Password with `*`
- Main password verification
- Search password function
- Encryption of password
- GUI interface
- Remote access


> Made by Weidoorfin