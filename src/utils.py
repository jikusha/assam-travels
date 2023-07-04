from enum import Enum
from entity import *
import psycopg2
import re

class Options(Enum):
    Login = 1
    SignUp = 2

class Actions(Enum):
    SignUp = 'signup'

user_inputs = ['name', 'mobile', 'email', 'password', 'type']

def get_user_inputs(action = Actions.SignUp.value):
    inputs = {}
    if action == Actions.SignUp.value:
        i = 0
        while i < len(user_inputs):
            if user_inputs[i] != 'type':
                val = input(f"Please enter {user_inputs[i]}: ")
            else:
                val = input(f"Please enter {user_inputs[i]}(C/O): ")

            if is_valid(user_inputs[i], val):
                inputs[user_inputs[i]] = val
                i += 1
            else:
                print(f"\nGiven {user_inputs[i]} is not valid. Please enter in proper format.")
                continue

        return User(name=inputs['name'].upper(), mobile=inputs['mobile'], email=inputs['email'],
                    type=inputs['type'].upper(), password=inputs['password'])

def is_valid(col: str, val) -> bool:
    if col == 'email':
        regex = re.compile(r'^[A-Za-z][A-Za-z0-9\.]*[A-Za-z0-9]+@[A-Za-z]+\.[a-zA-Z]+')
        if re.fullmatch(regex, val):
            return True
        return False
    elif col == 'mobile':
        regex = re.compile(r'\d{10}')
        if re.fullmatch(regex, val):
            return True
        return False
    elif col == 'type':
        if val in ['C', 'c', 'O', 'o']:
            return True
        return False
    else:
        if val == '':
            return False
        return True


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

