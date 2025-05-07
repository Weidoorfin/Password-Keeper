# Password Keeper

An simple program that helps you store you account and password information locally

Version: **v1.0**

---

## Features
- Adding a new password
- View all existing passwords (in plain text)
- Using json to store all local data
- Interaction based on command input

---

## Project Structure
```
Passwork-Keeper/
├── main.py          # Program Interface and Interaction
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

### v1.0 (2025-05-07)

- Initialization of the project
- Realization of adding and viewing functions
- Utilization of JSON file to locally store data
- Modulization of Project (main.py + storage.py)

---

## Warning
- Never upload `data.json` with real passwords to Github!
- `data.json` has been ignored in `.gitignore`, no further action needed

---

## Future Plans
- Delete password function
- Hide Password with `*`
- Main password verification
- Search password function
- Encryption of password
- GUI interface
- Remote access


> Made by Weidoorfin