def draw(a):
    a -= 1
    if a == 9:
        print(a, " turns are left")
        print("    -----")
    elif a == 8:
        print(a, " turns are left")
        print("    -----")
        print("     0 ")
    elif a == 7:
        print(a, " turns are left")
        print("    -----")
        print("     0 ")
        print("     | ")
    elif a == 6:
        print(a, " turns are left")
        print("    -----")
        print("     0 ")
        print("     | ")
        print("    /")
    elif a == 5:
        print(a, " turns are left")
        print("    -----")
        print("     0 ")
        print("     | ")
        print("    / \\  ")
    elif a == 4:
        print(a, " turns are left")
        print("    -----")
        print("    \\0 ")
        print("     | ")
        print("    / \\  ")
    elif a==3:
        print(a, " turns are left")
        print("    -----")
        print("    \\0/ ")
        print("     | ")
        print("    / \\  ")
    elif a==2:
        print(a, " turns are left")
        print("    -----")
        print("    \\0/| ")
        print("     | ")
        print("    / \\  ")
    elif a==1:
        print(a, " turns are left")
        print("    -----")
        print("    \\0/_| ")
        print("     | ")
        print("    / \\  ")
    elif a==0:
        print("you loose , you let a kind man die")
        print("    -----")
        print("     0_| ")
        print("    /|\\ ")
        print("    / \\  ")