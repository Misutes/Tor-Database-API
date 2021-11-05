from peewee import TextField, Model

from settings import Settings


class BaseModel(Model):
    class Meta:
        database = Settings.DATABASE


class User(BaseModel):
    email = TextField(primary_key=True)
    state = TextField(null=True)

    class Meta:
        db_table = 'User'
