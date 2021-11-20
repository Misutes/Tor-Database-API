import os
import sys

file_path = ""


def remove_file(path=""):
    global file_path
    if path:
        file_path = path
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass


def generate_crypto_key():
    from fernet import Fernet
    print(f"Your CRYPTO_KEY: {Fernet.generate_key().decode()}")


def generate_crypto_token():
    from fernet import Fernet
    token = input("Input your `CRYPTO_KEY`: ")
    password = input("Input your password: ")
    print(f"Your CRYPTO_TOKEN: {Fernet(token.encode()).encrypt(password).decode()}")


if __name__ == "__main__":
    method = sys.argv[1]
    getattr(sys.modules[__name__], method)()
