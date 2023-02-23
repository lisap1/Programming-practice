# import statements
count = 0
max_tickets = 5
name = ""


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

while count < max_tickets:
    # Get name (can't be blank)
    not_blank("Name:")
    # count tickets
    if name != "xxx":
        count += 1
    tickets_left = max_tickets - count
    # display tickets sold and tickets left
    if tickets_left > 0:
        print("You have sold {} tickets. \nThere are {} tickets left.".format
              (count, tickets_left))
    else:
        print("You have sold all the tickets!")
    # exit code
    if name == "xxx":
        break

    # Get age ( between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # ask for payment method ( and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text files
