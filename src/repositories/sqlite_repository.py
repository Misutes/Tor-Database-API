from repositories.db_models import User


class TorRepository:

    def __init__(self, db):
        self._db = db
        self._create_db_table()

    def _create_db_table(self):
        with self._db:
            self._db.create_tables([User])

    def count_users(self):
        with self._db:
            return len(User.select())

    def get_users(self, state, count):
        with self._db:
            return User.select().where(User.state == state).limit(count)

    def update_users(self, emails, state):
        invalid_emails = []
        with self._db:
            for email in emails:
                if list(User.select().where(User.email == email)):
                    User.update({"state": state}).where(User.email == emails).execute()
                else:
                    invalid_emails.append(email)
            return invalid_emails

    def get_register(self, count):
        with self._db:
            return User.select().where(User.state == 1).limit(count)

    def update_state(self, emails):
        with self._db:
            User.update({"state": 2}).where(User.email << emails).execute()
