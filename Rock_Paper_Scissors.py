import random

user_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]



while True:
    game_start = input("Welcome to Rock Paper Scissors! Type Play or Quit to Continue. ").lower()
    if game_start not in ["quit","play"]:
        continue
    if game_start == "quit":
        quit()
    if game_start == "play":
        user_input = input("Please Type Rock, Paper, or Scissors. ").lower()
        if user_input not in choices:
            print("Please type a valid response. ")
            continue 
    
    random_number = random.randint(0, 2)
    computer_choice = choices[random_number]
    print("Computer picked", computer_choice + ".")

    if user_input == "rock" and computer_choice == "rock":
        print("Draw, Try Again! ")
    if user_input == "rock" and computer_choice == "paper":
        print("Paper beats Rock, Computer Wins! \n")
        computer_wins += 1 
        print("Computer won " + str(computer_wins) + " Amount of times! ")
    if user_input == "rock" and computer_choice == "scissors":
        print("Rock beats Scissors, You Win! \n") 
        user_wins += 1 
        print("You won " + str(user_wins) + " Amount of times! ")

    if user_input == "paper" and computer_choice == "paper":
        print("Draw, Try Again! ")
    if user_input == "paper" and computer_choice == "scissors":
        print("Scissors beats Paper, Computer Wins! \n") 
        computer_wins += 1 
        print("Computer won " + str(computer_wins) + " Amount of times! ")
    if user_input == "paper" and computer_choice == "rock":
        print("Paper beats Rock, You Win! \n") 
        user_wins += 1 
        print("You won " + str(user_wins) + " Amount of times! ")            

    if user_input == "scissors" and computer_choice == "scissors":
        print("Draw, Try Again! ")
    if user_input == "scissors" and computer_choice == "rock":
        print("Rock beats Scissors, Computer Wins! \n") 
        computer_wins += 1 
        print("Computer won " + str(computer_wins) + " Amount of times! ")
    if user_input == "scissors" and computer_choice == "paper":
        print("Scissors beats Paper, You Win! \n") 
        user_wins += 1 
        print("You won " + str(user_wins) + " Amount of times! ")



    




