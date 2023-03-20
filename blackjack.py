import random 

playerCard = []
bankerCard = []

# Give cards to banker and player
def giveCards():
    i = 0
    while i <= 1:
        playerCard.append(random.randint(1,21))
        bankerCard.append(random.randint(1,21))
        i+=1
    continuetoplay()
    bankercardtotal()

# Calculate player card total
def playercardtotal():
     total = 0
     for i in playerCard:
          total += i    
     return total

# Calculate banker card total
def bankercardtotal():
    total = 0
    for i in bankerCard:
          total += i
    return total

# Ask player want to continue to play or not 
def continuetoplay():
    playertotal = playercardtotal()
    print("Your card total is",playertotal)
    if playertotal >= 21:
         print("Bust, thanks for playing")
    else:
        decision = input("Continue to play? (Y/N): ")
        if decision.upper() == 'Y':
            playgame(playertotal, bankercardtotal())
        else:
            print("Thank you for playing")

# Blackjack started 
def playgame(player,banker):
     print(f"Banker card is: {banker}")
     if banker > 21 or player > banker:
          print("You Win !!")
     else:
          print("You lose !!")

# Game started (main function for this project)
def startgame():
     print("WELCOME TO BLACKJACK")
     name = input("YOUR NAME (MR/MRS)?: ")
     print(name)
     ready = input("READY TO PLAY?: ")
     if ready.lower() == 'y':
          giveCards()
     else:
          print("THANKS FOR PLAYING")

startgame()


