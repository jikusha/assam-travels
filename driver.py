from utils import Options

if __name__ == '__main__':
    print("######### Welcome to Assam Travels ############")
    print("\nPlease Login for Booking and Managing your Bus Tickets => \n")
    print("Please select an option from below: \n")
    print(f"Press {Options.Login.value} for Login")
    print(f"Press {Options.SignUp.value} for Sign Up")
    print()

    while True:
        try:
            choice = int(input("Please Enter your choice: "))
        except Exception as ex:
            print(f"!!!!! Could not proceed with the choice due to invalid choice format !!!!!!"
                  f" Please enter a valid choice. \n")
            continue

        if choice == Options.Login.value:
            print("You have chosen for Login")
            break
        elif choice == Options.SignUp.value:
            print("You have chosen for Sign Up")
            break
        else:
            print("!!! You have entered an invalid choice !!! Please enter a valid choice. \n")
