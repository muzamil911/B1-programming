

user_name = "muz"
user_pin = '1234'
total_attempts = 3
current_attempt = 0

while current_attempt < total_attempts:
    # conditions for numbers of attempts:

    attempts = total_attempts - current_attempt
    if attempts > 1:
        print(f"--->>>You have {total_attempts-current_attempt} more attempts<<<---\n")
    elif attempts == 1:
        print("--->>> Be Careful<<<---\n -> Its your last attempt!\n")

    # user input:
    entered_name = input(">>Enter username: ")
    entered_pin = input(">>Enter your PIN: ")

    # Conditions for data check:

    if entered_name == user_name and entered_pin == user_pin:
        print("\n-------->>Your are loged in.<<--------")
        break
    elif entered_name != user_name or entered_pin != user_pin:
        print("\n!!!Invalid credentials!!!")
        current_attempt = current_attempt + 1
    
        # Message if all the inputs were wrong:
        if attempts == 1:
            print("Forgot password?\n-> Your account is currently paused!")
        else:
            continue

    


