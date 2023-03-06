# functions go here

# valid = false, while loop, error message .lower
def yes_no():
    error = "Please enter 'yes' or 'no'"
    # loop until valid response
    valid = False
    while not valid:
        response = input("Would you like to order snacks: ").lower()
        if response == "yes" or response == "no":
            return response
        else:
            print(error)


# main routine
snacks_question = yes_no()

