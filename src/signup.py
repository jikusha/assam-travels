from utils import db_connect
from db_helper import DbHelper

class Signup:
    def __init__(self, user):
        self.user = user
        self.db_helper= DbHelper(db_connect())

    def create_new_user(self):
        query = f"insert into dev.users (name, email, mobile, password, type)" \
                f" values (%(name)s, %(email)s, %(mobile)s, %(password)s, %(type)s)"

        params = {
            'name': f'{self.user.name}' if self.user.name else None,
            'email': f'{self.user.email}' if self.user.email else None,
            'mobile': f'{self.user.mobile}' if self.user.mobile else None,
            'password': f'{self.user.password}' if self.user.password else None,
            'type': f'{self.user.type}' if self.user.type else None
        }

        self.db_helper.execute_query_with_params(query, params)
        print("\nNew User has been created successfully\n")