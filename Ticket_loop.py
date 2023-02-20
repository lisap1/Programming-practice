# start the loop
count = 0
max_tickets = 5
name = ""


# if tickets less than max continue loop

while name != "xxx" and count < max_tickets:
    name = input("name: ")
    count += 1
    tickets_left = max_tickets - count
    if tickets_left > 0:
        print("You have sold " + str(count) + " tickets")
        print("There are " + str(tickets_left) + " tickets left.")
    else:
        print("You have sold all the tickets!")
