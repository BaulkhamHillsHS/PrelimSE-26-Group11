from cryptography.fernet import Fernet

# assume this some kind of serverside encryption system
# The password for each account is encrypted using fernet beforehand
# This could probably also be done to other sensitive info

# made from Fernet.generate_key()
key = "izT5hls4qlm_rmXk635kVyulwuaEc9xo-1pzPOzeRfQ=".encode()


def encrypt(password: bytes) -> bytes:
    return Fernet(key).encrypt(password)


def decrypt(token: bytes) -> bytes:
    return Fernet(key).decrypt(token)


def validate_password(token: bytes, password: str):
    if decrypt(token) == password.encode():
        return True
    return False


""" Original passwords
print(encrypt("1234567890".encode()))
print(encrypt("1234567890".encode()))
print(encrypt("You will fail worthless lizard".encode()))
print(encrypt("Baulko11!!".encode()))
print(encrypt("Append".encode()))
print(encrypt("password".encode()))
print(encrypt("gotta go fast".encode()))
print(encrypt("sugar, spice, and everything nice".encode()))
print(encrypt("Oh! Banana.".encode()))
print(encrypt("better".encode()))
"""
