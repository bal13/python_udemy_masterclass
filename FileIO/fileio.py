# jabber = open("e:/Downloads/sample.txt", "r") # ez is működik
jabber = open("e:\\Downloads\\sample.txt", "r")

for line in jabber:
    print(line)

jabber.close()