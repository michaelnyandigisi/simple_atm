#Simple ATM Machine System

import getpass

def login():
    '''Login Module'''
    
    # Initialisation
    passcount = 0
    trials = 3
    
    # Display
    print('ABC Bank Limited version 1.0')
    print('----------------------------\n')
    
    # Loop to allow multiple login attempts
    while passcount < trials:
        # Username Input
        username = input("Enter your Username: ")
        
        # Password Input (PIN)
        password = getpass.getpass("Enter your PIN: ")
        
        # Check username
        if username.lower() == 'admin':
            # Check password (ensure the PIN is treated as a string)
            if password == '2006':  # Use '2006' as a string
                print("Login Successful!")
                break  # Exit the loop upon successful login
            else:
                passcount += 1
                trials -= 1
                print(f"Login Failed! {trials} attempt(s) left.")
        else:
            print("Invalid Username!")
            break  # Exit the loop if the username is incorrect
    
    # If the user exhausts all trials
    if passcount == 3:
        print("Maximum login attempts reached. Please try again later.")

# Call the login function
login()

        
    
    





