import random


def play():
    number = random.randint(1, 100)
    guess = 0
    count = 0

    tryAgain = 'y'

    while tryAgain == 'y':
        count = count + 1
        guess = int(input("Please guess a number between 1 and 1000:" ))
        print("number is ", number)
        print("guess is ", guess)
        if (guess > number + 10):
            print("Too high")
        elif guess > number:
            print("Too high, but so close")
        elif (guess < number - 10):
            print("Too low")
        elif (guess < number):
            print("Too low, but so close")
        elif (number == guess):
            print("You rock! You guessed the number in", count, "tries")
            break
    
        tryAgain = input("Try again? Input y for yes: ")
   

    playAgain = input("Would you like to play the game again? Press y for yes: ")
    if playAgain == 'y':
        play()
    else:
        print("Thanks for playing!")


play()

#If the player’s guess is higher than the number generated then display the message “Too
#High!”. If the player’s guess is within a 10-point difference of the number generated
#but higher than the number generated, then give the message “Getting warm but still
#high!” (LO 1)
#4. If the player’s guess is lower than the number generated then display the message “Too
#Low!” If the player’s guess is within a 10 point difference of the number generated but
#lower than the number generated, then give the message “Getting warm but still Low!”
#5. The program will keep taking guesses until the player guesses the number. (LO 1)
#6. Once the player guesses the number, give them a congratulatory message like “You
#rock! You guessed the number in x tries!!” where x is the actual number of tries it took
#the player to guess the number. You can write any message as long as you include the
#number of tries in the message.
#7. Once the player has guessed the number, ask them if they wish to play again. If they do
#then generate another random number and start the game over again. (LO 3)
#8. All input to the program will be interactive from the keyboard.
#Use the IDLE programming environment if you are using Python with IDLE. S
