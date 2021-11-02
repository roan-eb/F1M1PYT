while True:

    answer = input ("Would you like to play? (yes/no) ")

    if answer.lower().strip() == "yes":

        answer = input("You reach a crossroad, would you like to go left or right? (left/right) ").lower().strip()
        if answer == "left":
            answer = input("You encountered a bear, would you like to run or attack? (run/attack) ")

            if answer == "attack":
                    print("That was not the greatest idea, you lost! ")
            else:
                print("Good choice, you made it away safely. ")

            answer = input("You see a car and a plane. Which one would you like to use? (car/plane) ")

            if answer == "plane":
                    print("You have no clue how to fly a plane... Game over! ")
            else: 
                print("Well done, but you didnt check the gas tank.. ")
                
                answer = input("You ended up without gas in the middle of nowhere will you start walking or wait for a bypassing car? (walk/wait) ")
                
                if answer == "walk":
                        print("You found a house well done! You won the game!")
                else: 
                    print("No one came by and you werent able to warm yourself up. Game over! ")  

        elif answer == "right":
                print("You walked to the right and stepped on a venomous snake, the snake bites you. Game over!  ")
        
        else: 
            print("Invalid choice, you lost! ")

    else:
        print("That's too bad!" )
        break 