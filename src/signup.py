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
            'name': f'{self.user.name}',
            'email': f'{self.user.email}',
            'mobile': f'{self.user.mobile}',
            'password': f'{self.user.password}',
            'type': f'{self.user.type}'
        }

        self.db_helper.execute_query_with_params(query, params)
        print("\nNew User have been created successfully\n")