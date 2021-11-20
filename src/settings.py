import fernet
from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()


class Settings:
    MONGO_ADDRESS = env.str("MONGO_ADDRESS")
    MONGO_DATABASE = env.str("MONGO_DATABASE")
    MONGO_COLLECTION = env.str("MONGO_COLLECTION")

    CRYPTO_KEY = env.str("CRYPTO_KEY")
    ENCRYPTOR = fernet.Fernet(CRYPTO_KEY.encode())

    SECRET_KEY = env.str("SECRET_KEY")
