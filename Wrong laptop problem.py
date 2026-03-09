#Idk Quarter Project 2 I guesse. Made by Paulo, Cowey, Aidan.
print("SUPER SIMPLE CLASS LAPTOP NUMBER ASSIGNER")
classes = {}
while True:
    print("\nCLASSES:")
    num = 1
    names = []

    if len(classes) == 0:
        print("No classes yet.")
        
    for c in classes:
        print(num, ")", c)
        names.append(c)
        num += 1
   
    print("\n+ = add class")
    print("x - exit")
   
    choice = input("Choose class number or +: ")
    
    if choice == "+":
        cname = input("Class name: ")
        if cname in classes:
            print("Class already exist!")
        else:
            classes[cname] = []
            print("Added class!")

    elif choice == "x":
        print("Program closed.")
        break

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
                print("e = edit laptop number")
                print("s = search student")
                print("* = back")
                      
                pick = input("Pick: ")
                
                if pick == "+":
                    n = input("Student name: ")
                    l = input("Laptop: ")
                    classes[cname].append([n, l])

                    #sort alphabetically
                    classes[cname].sort()
                    
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
                                print("Invalid number")
                elif pick == "s":
                    search = input("Student name to search: ").lower()
                    found = False
                   
                    for student in classes[cname]:
                        if search in student[0].lower():
                            print("Found: ", student[0], "- Laptop", student[1])
                            found = True
                    if not found:
                        print("Student not found.")
                        
                elif pick == "*":
                    break
                else:
                    print("Invalid Option.")
        else:
            print("No class found.")
    else:
        print("Invalid Option.")




