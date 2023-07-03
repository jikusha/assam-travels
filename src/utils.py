from enum import Enum
from entity import *
import psycopg2

class Options(Enum):
    Login = 1
    SignUp = 2

class Actions(Enum):
    SignUp = 'signup'

user_inputs = ['name', 'mobile', 'email', 'password', 'type']

def get_user_inputs(action = Actions.SignUp.value):
    inputs = {}
    if action == Actions.SignUp.value:
        for key in user_inputs:
            val = input(f"Please enter {key}: ")
            inputs[key] = val

        return User(name=inputs['name'], mobile=inputs['mobile'], email=inputs['email'],
                    type=inputs['type'], password=inputs['password'])

def db_connect():
    try:
        conn = psycopg2.connect(host="localhost",
                                database="assam-travels",
                                user="postgres",
                                password="Nagaon@123"
                                )
    except Exception as ex:
        print(f"Unable to connect to data base due to {ex}")
        raise ex

    return conn

