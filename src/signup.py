from utils import db_connect
class Signup:
    def __init__(self, user):
        self.user = user

    def create_new_user(self):
        conn = db_connect()
        cur = conn.cursor()
        cur.execute(
            f"insert into dev.users (name, email, mobile, password, type) values "
            f"('{self.user.name}', '{self.user.email}', '{self.user.mobile}', '{self.user.password}', '{self.user.type}')"
        )
        conn.commit()

        print("\nNew User have been created successfully\n")