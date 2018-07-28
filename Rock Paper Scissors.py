# May Pena
# This rock, paper, scissors game is against the computer.
# The computer randomly generates its pick. This game
# also keeps score and stops once someone wins 3 times.

# Open our library
import random

# Start game and scores
print( "Welcome to my Rock, Paper, Scissors game!")
print( "Type in the word rock, paper or scissors to play.")
print( "The first person to get 3 points wins!")
userScore = 0
compScore = 0

while True:
    # Set viable plays
    plays    = [ "Rock", "Paper", "Scissors" ]
    
    # Ask the user for their play
    print()
    userPlay = input( "What will be your play? " ).title()
    
    if userPlay not in plays:
        userPlay = input("That's not an option, try again: ").title()

    # Generate computer's play 
    compPlay = random.choice( plays )

    # Determine who won the round and keep score
    print()
    print( "Your pick:", userPlay)
    print( "Computer's Pick:", compPlay )

    #     Where there is a tie      
    if userPlay == compPlay:
        print( "It's a tie!" )
        
    #     Occasions where the user wins    
    elif userPlay == "Paper" and compPlay == "Rock":
        print( "You win!" )
        userScore = userScore + 1

    elif userPlay == "Rock" and compPlay == "Scissors":
        print( "You win!" )
        userScore = userScore + 1

    elif userPlay == "Scissors" and compPlay == "Paper":
        print( "You win!" )
        userScore = userScore + 1

    #     Occasions where the user loses   
    elif userPlay == "Paper" and compPlay == "Scissors":
        print( "You lost :( " )
        compScore = compScore + 1
        
    elif userPlay == "Scissors" and compPlay == "Rock":
        print( "You lost :( " )
        compScore = compScore + 1

    elif userPlay == "Rock" and compPlay == "Paper":
        print( "You lost :( " )
        compScore = compScore + 1

    # stop when someone reaches 3 points
    if userScore == 3:
        print( "You won the game!" )
        break
    elif compScore == 3:
        print( "The computer wins :( " )
        break
