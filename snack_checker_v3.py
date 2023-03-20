valid_yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "m and m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]


# function for snack, asking yes or no question, asking for what snacks, and number of snacks.
def snack_checker():
    # yes or no question
    valid = ""
    # initialise loop
    while not valid:
        response = input("Would you like to order snacks: ").lower()
        # checks if answer valid
        for var_list in valid_yes_no:
            # if valid,
            if response in var_list:
                valid = True
                answer = var_list[0].title()
                if answer == "yes":
                    print("congrats")
                else:
                    continue_no = True
            else:
                print("error")
                # if yes, prompt for snack. If no then break.

# ask yes or no for snacks
    # if yes, ask for what snacks
        # if valid, ask for how many
            # if valid, continue snack loop until exit code recieved
    # if no break


snack_checker()
