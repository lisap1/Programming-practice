# start the loop
count = 0
max_tickets = 5
name = ""


# if tickets less than max continue loop

while count < max_tickets:
    name = input("name: ")
    if name != "xxx":
        count += 1
    tickets_left = max_tickets - count
    if tickets_left > 0:
        print("You have sold {} tickets".format(count))
        print("There are {} tickets left.".format(tickets_left))
    else:
        print("You have sold all the tickets!")
    if name == "xxx":
        break
