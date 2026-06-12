from cryptography.fernet import Fernet

# assume this some kind of serverside encryption system


# from Fernet.generate_key()
key = "izT5hls4qlm_rmXk635kVyulwuaEc9xo-1pzPOzeRfQ=".encode()


def encrypt(password: bytes) -> bytes:
    return Fernet(key).encrypt(password)


def decrypt(token: bytes) -> bytes:
    return Fernet(key).decrypt(token)


print(encrypt("Baulko11!!".encode()))
"""
print(encrypt("1234567890".encode()))
print(encrypt("1234567890".encode()))
print(encrypt("a".encode()))
print(encrypt("Baulko11!!".encode()))
"""
