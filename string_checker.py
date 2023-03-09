# functions go here

# valid = false, while loop, error message .lower
def string_check(question, to_check):
    error = "Please enter a valid snack"
    # loop until valid response
    valid = False
    while not valid:
        response = input(question).lower()
        # if first input matches yes or no, return
        if response in to_check:
            return response
        # if first letter matches yes or no, it is accepted
        else:
            for item in to_check:
                if response == item[0]:
                    return item
        print(error)


# main routine
for x in range(0, 6):
    snacks_wanted = string_check("What snacks would you like: ",
                                 ["pita chips", "popcorn"])
    print("You answered " + snacks_wanted)
