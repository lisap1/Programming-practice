# Functions go here

# function for asking name

def not_blank(question):
    valid = False


# while valid= False, continue asking
    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - This can't be blank, please enter your name")


# Main Routine goes here

not_blank("Name:")
