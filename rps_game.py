#Rock, paper, and scissors game in Python
from random import randint
choices=["rock", "paper", "scissors"]
playGame=True

while playGame==True:
    computer=choices[randint(0,2)]
    player=input("Choose rock, paper, or scissors: ").lower()

    if computer==player:
        print("It's a tie!")
    elif player=="rock":
        if computer=="scissors":
            print("You win! Rock smashes scissors.")
        else:
            print("You lose! Paper covers rock.")

    elif player=="paper":
        if computer=="rock":
             print("You win! Paper covers rock.")
        else:
             print("You lose! Scissors cuts paper.")
    elif player=="scissors":
         if computer=="rock":
             print("You lose! Rock smashes scissors.")
         else:
             print("You win! Scissors cuts paper")
    else:
          print("Not a valid play. Try again!")
          continue
    keepPlaying=input("Play again? Type yes or no ").lower()
    
    if keepPlaying=="no":
          playGame=False
          print("Thanks for playing!")
    elif keepPlaying=="yes":
          playGame=True
          print("Let's go!")
    else:
        print("Invalid entry. Type yes or no.")
        keepPlaying=input("Play again? ")
        if keepPlaying=="no":
            playGame=False
            print("Thanks for playing!")
        elif keepPlaying=="yes":
            playGame=True
            print("Let's go!")
        else:
            print("Invalid entry.")
            continue
            
        
        
        
    
    
