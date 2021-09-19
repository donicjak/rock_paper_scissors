import random

t = ["Rock", "Paper", "Scissors"]

def computerTurn():
    computer = t[random.randint(0,2)]
    return computer

def playerTurn():
    player = input("Make your choice: ")
    return player

def game():
    computer = computerTurn()
    player = playerTurn()
    if ( player == "Scissors" ):
        if(computer == "Scissors"):
            print(f"It's a draw! Both of you selected {player}!")
        elif(computer == "Rock"):
            print(f"You lose! {computer} beats {player}!")
        else:
            print(f"You win! {player} beats {computer}!")
    elif( player == "Rock" ):
        if( computer == "Rock" ):
            print(f"It's a draw! You both selected {player}!")
        elif(computer == "Paper"):
            print(f"You lose! {computer} beats {player}!")
        else:
            print(f"You win! {player} beats {computer}")
    else:
        if( computer == "Paper" ):
            print(f"It's a draw! You both selected {player}!")
        elif( computer == "Rock" ):
            print(f"You win! {player} beats {computer}!")
        else:
            print(f"You lose! {computer} beats {player}!")

game()