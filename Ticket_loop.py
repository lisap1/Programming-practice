# start the loop
count = 0
max_tickets = 5
name = ""


# if tickets less than max continue loop

while count < max_tickets:
    # get name
    name = input("name: ")
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
