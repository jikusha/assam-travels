from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors
from utils import *
from signup import Signup
from login import Login
from exception import UserNotFoundException, WrongPasswordException

if __name__ == '__main__':
    print("######### Welcome to Assam Travels ############")
    print("\nPlease Login for Booking and Managing your Bus Tickets => \n")

    while True:
        print("Please select an option from below: \n")
        print(f"Press {Options.Login.value} for Login")
        print(f"Press {Options.SignUp.value} for Sign Up")
        print(f"Press {Options.Exit.value} for Exit")
        print()
        try:
            choice = int(input("Please Enter your choice: "))
        except Exception as ex:
            print(f"!!!!! Could not proceed with the choice due to invalid choice format !!!!!!"
                  f" Please enter a valid choice. \n")
            continue

        if choice == Options.Login.value:
            while True:
                print("You have chosen for Login\n")
                credential = get_user_inputs(Actions.Login.value)
                login = Login(credential)
                try:
                    user = login.get_user()
                except UserNotFoundException as ex:
                    print("\n!!!! Given email is not found !!!\n")
                    continue
                except WrongPasswordException as ex:
                    print("\n!!!! You have entered a wrong password !!! Please enter correct password !!!\n")
                    continue
                except Exception as ex:
                    raise ex

                print("\n!!!!! You are successfully logged in !!!!\n")

        elif choice == Options.SignUp.value:
            while True:
                print("You have chosen for Sign Up\n")
                print("Please enter the following required details: \n")
                user = get_user_inputs(Actions.SignUp.value)
                signup = Signup(user)
                try:
                    signup.create_new_user()
                except errors.lookup(UNIQUE_VIOLATION) as ex:
                    print(f"\nGiven email_id {user.email} is already exists!! Please enter a different email_id !!!\n")
                    continue
                except Exception as ex:
                    print(f"Unable to register the user due to: {ex}")
                    raise ex
                print("Please Login to Proceed further.\n")
                break
        elif choice == Options.Exit.value:
            break
        else:
            print("!!! You have entered an invalid choice !!! Please enter a valid choice. \n")
