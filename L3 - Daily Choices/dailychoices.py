print("You woke up late and missed the bus, do you start walking or wait for the next bus?")
choice = input()
if choice == 'start walking':
    print("You started walking and realized you will be too late at work, you start running as fast as you can.")
elif choice == 'next bus':
    print("If you hurry you will be at work just in time.")
else:
    print(choice, " wasn't a valid choice")

print("You arrived at work just in time. Your boss is mad because you had to be at work early to help a customer. Do you make an excuse or explain what happenend?")
choice = input()
if choice == 'make an excuse.':
    print("The bus wasn't driving I had to walk I couldn't do anything against it. ")
elif choice == 'Explain what happenend':
    print("I woke up late so I missed the bus, I'm sorry. ")
else:
    print(choice, " wasn't a valid choice")

print("")
choice = input()
if choice == ' ':
    print(" ")
elif choice == '':
    print("")
else:
    print(choice, " ")

