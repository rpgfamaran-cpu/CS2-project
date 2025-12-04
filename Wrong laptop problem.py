#Testing different stuff for reviewing.
#Goals:
#Input/Output included, arith, logical, relational.

#price guessing game!
#credentials stuff like login and signups idk if i should add pass and stuff
Name1 = str(input("Input your name! "))
print("Wow! you made a great name,", Name1)
#game starter
Main_Roundstarter = int(input("Would you like to start? press 1 if yes, 2 if no. "))
if Main_Roundstarter == 1:
    print("Ok! lets start. Here's round 1.")
elif Main_Roundstarter ==2:
    print("Goodbye!")
    quit()
else:
    print("Invalid choice!")
    quit()
#idk what to name
Mainlist = ["Headless", "Rainbow Shaggy", "Golden Crown", "Monopoly hat"]

print("Please choose from this list! USE ONLY 1-5!!!", Mainlist)

