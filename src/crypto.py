#crypto.py

import ctypes
import base64
from config import CRYPTO_DLL_FILE
from master_password import get_master

def hash_enpcrypt(password):
    crypto = ctypes.CDLL(CRYPTO_DLL_FILE)
    crypto.xor_crypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    crypto.xor_crypt.restype = ctypes.c_void_p

    crypto.destroy.argtypes = [ctypes.c_void_p]
    crypto.destroy.restype = None

    key = get_master()

    ptr = crypto.xor_crypt(password.encode(), key.encode())

    raw = ctypes.string_at(ptr)
    
    encrypted = base64.b64encode(raw).decode()

    crypto.destroy(ptr)

    return encrypted

def hash_decrypt(password):
    crypto = ctypes.CDLL(CRYPTO_DLL_FILE)
    crypto.xor_crypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    crypto.xor_crypt.restype = ctypes.c_void_p

    crypto.destroy.argtypes = [ctypes.c_void_p]
    crypto.destroy.restype = None

    raw = base64.b64decode(password)

    key = get_master()

    ptr = crypto.xor_crypt(raw, key.encode())

    decrypted = ctypes.string_at(ptr).decode()

    crypto.destroy(ptr)

    return decrypted

