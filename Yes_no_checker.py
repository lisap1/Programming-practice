# functions go here

# valid = false, while loop, error message .lower
def yes_no(to_check):
    error = "Please enter 'yes' or 'no'"
    # loop until valid response
    valid = False
    while not valid:
        response = input("Would you like to order snacks: ").lower()
        if response in to_check:
            return response
        else:
            for item in to_check:
                if response == item[0]:
                    return item
        print(error)


# main routine
for x in range(0, 6):
    snacks_question = yes_no(["yes", "no"])
    print("You answered " + snacks_question)

