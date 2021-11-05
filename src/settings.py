from dotenv import load_dotenv
from environs import Env
from peewee import SqliteDatabase

load_dotenv()
env = Env()


class Settings:
    DATABASE_PATH = str(env.str("DATABASE_PATH", "\\")).replace("/", "\\")
    DATABASE_NAME = env.str("DATABASE_NAME", "database.db")

    DATABASE = SqliteDatabase(f"{DATABASE_PATH}{DATABASE_NAME}")
