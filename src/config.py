#config.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Root

DATA_DIR = os.path.join(BASE_DIR, "data")

DATA_FILE = os.path.join(DATA_DIR, "data.json")

MASTER_PASSWORD_FILE = os.path.join(DATA_DIR, "master_password.json")