# Functions go here

# function for asking name

def not_blank(question):
    valid = False


# while valid= False, continue asking
    while not valid:
        response = input(question)
        # Verifying whether name doesn't contain numbers or symbols
        if response != "" and response.isalpha():
            return response
        elif response == "":
            print("Sorry - This can't be blank, please enter your name")
        elif not response.isalpha():
            print("Sorry - Your name cannot contain numbers or symbols")
        else:
            print("Error - Please try again")


# Main Routine goes here

not_blank("Name: ")

