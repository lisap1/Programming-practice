# import statements

# functions go here
def not_blank(question):
    valid = False

    # while valid= False, continue asking

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - This can't be blank, please enter your name")

# ******** Main Routine ********


# set up dictionaries / lists needed to hold data

# ask user if they have used the program before and show instructions if necessary

# Loop to get tickets details

    # Get name (can't be blank)
    not_blank("Name:")

    # Get age ( between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # ask for payment method ( and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text files