with open("sample.txt", "a") as jabber:
    for i in range(1, 12):
        print(f"{i} times 2 is {i * 2}", file=jabber, flush=True)

