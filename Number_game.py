# get input from user
# 8 tries will give to user
# if user choose < 1 or > 100, it will show out of limit
# if user choose < actual_number, then say lower number
# if user choose > actual_number, then say higher number
# finally if user won, show how many tries the user did.

from random import randint

secret_value = randint(1,100)
retries = 1
max_retry = 8

name = input("What's your name? ")
print(f"""Well {name}, I've thought of a number between 1 and 100 and you have only {max_retry} tries to guess it.""")
while retries <= 8:
    user_input = int(input("What number do you think it is? "))
    if user_input <= 0 or user_input >= 101:
        print(f"it is out of limit, choose between 1 and 100. you have {max_retry - retries} retry left..")
    elif user_input < secret_value:
        print(f"{name} you choosen lesser value then secret, try again.. you have {max_retry - retries} retry left..")
    elif user_input > secret_value:
        print(f"{name} you choosen greater value then secret, try again..you have {max_retry - retries} retry left..")
    elif user_input == secret_value:
        print(f"{name}, Hooray You won..!!")
        break
    retries += 1
else:
    print(f"Sorry {name}, Try harder Next time...!!!")
