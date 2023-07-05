from db_helper import DbHelper
from utils import db_connect, user_inputs_for_signup
from exception import UserNotFoundException, WrongPasswordException
from entity import User

class Login:
    def __init__(self, credential):
        self.credential = credential
        self.db_helper = DbHelper(db_connect())

    def get_user(self):
        query = "SELECT * from dev.users WHERE email = %(email)s"

        params = {
            'email': f'{self.credential.email}'
        }

        row = self.db_helper.get_user_by_email(query, params)

        if not row:
            raise UserNotFoundException
        elif self.credential.password != row['password']:
            raise WrongPasswordException
        else:
            return User(name=row['name'], mobile=row['mobile'], email=row['email'],
                        type=row['type'], password=row['password'])








