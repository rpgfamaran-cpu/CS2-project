#Idk Quarter Project 2 I guesse. Made by Paulo, Cowey, Aidan.
print("SUPER SIMPLE LAPTOP ASSIGNER")
classes = {}
while True:
    print("\nCLASSES:")
    num = 1
    names = []
    for c in classes:
        print(num, ")", c)
        names.append(c)
        num += 1
    print("\n+ = add class")
    choice = input("Choose class number or +: ")
    if choice == "+":
        cname = input("Class name: ")
        classes[cname] = []
        print("Added class!")
    elif choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(names):
            cname = names[choice-1]
            while True:
                print("\nCLASS:", cname)
                print("STUDENTS:")
                if len(classes[cname]) == 0:
                    print("None")
                else:
                    for i in range(len(classes[cname])):
                        print(i+1, ")", classes[cname][i][0], "-", classes[cname][i][1])
                print("\n+ = add student")
                print("- = remove student")
                print("* = back")
                pick = input("Pick: ")
                if pick == "+":
                    n = input("Student name: ")
                    l = input("Laptop: ")
                    classes[cname].append([n, l])
                    print("Added!")
                elif pick == "-":
                    if len(classes[cname]) == 0:
                        print("No one to remove")
                    else:
                        for i in range(len(classes[cname])):
                            print(i+1, ")", classes[cname][i][0])
                        r = input("Number: ")
                        if r.isdigit():
                            r = int(r)
                            if 1 <= r <= len(classes[cname]):
                                classes[cname].pop(r-1)
                                print("Removed!")
                            else:
                                print("Bad number")
                elif pick == "*":
                    break
                else:
                    print("Nope.")
        else:
            print("Bad class.")
    else:
        print("Nope.")
