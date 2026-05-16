print("Today your target is 100 jumping jacks!")
remaining=0
for i in range(10,101,10):
    print("Perform 10 jumping jacks")
    choice = input("Are you Tired(Yes/Y/No/N)?")
    if choice.lower() in ("y" , "yes"):
        choice = input("Do you want to skip your remaining jumping jacks(Yes/Y/No/N)?")
        if choice.lower() in ("y" , "yes"):
            print("you completed a total of", i, "jumping jacks")
            break
    if choice.lower() in ("n" , "no"):
        remaining = 100 - i
        print("Your remaining jumping jacks are: ", (remaining))
    if i == 100:
        print("Congratulations! You completed the workout")
        break
