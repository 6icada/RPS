#Code by 6icada
#Please do not copy code

#Adding libraries
import random

#Adding vars
user_win = 0
computer_win = 0
money = 10000

#Forever loop
while True:
    #If money is 0 or less than 0 quit game
    if money <= 0:
        print("You are out of money!")
        break
 
    #User input and computer input
    userInput = input("Choose: ")
    computerInput = random.choice(['R', 'P', 'S'])

    if userInput == 'R' and computerInput == 'S':
        print("You won!")
        user_win += 1
        money += 500
    elif userInput == 'R' and computerInput == 'P':
        print("You lose!")
        computer_win += 1
        money -= 1000
    elif userInput == 'R' and computerInput == 'R':
        print("Draw!")
    elif userInput == 'P' and computerInput == 'S':
        print("You lose!")
        computer_win += 1
        money -= 1000
    elif userInput == 'P' and computerInput == 'P':
        print("Draw!")
    elif userInput == 'P' and computerInput == 'R':
        print("You won!")
        user_win += 1
        money += 500
    elif userInput == 'S' and computerInput == 'S':
        print("Draw!")
    elif userInput == 'S' and computerInput == 'R':
        print("You lose!")
        computer_win += 1
        money -= 1000
    elif userInput == 'S' and computerInput == 'P':
        print("You won!")
        user_win += 1
        money += 500

    #Showing score
    elif userInput == '/score':
        print(f"user: {user_win}")
        print(f"computer: {computer_win}")
    elif userInput == '/money':
        print(f"Your money: {money}")
    else:
        #If user's choise is not valid
        print("Invalid choise!")
