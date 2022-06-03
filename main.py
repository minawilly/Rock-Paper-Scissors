import random
print("Welcome to Rock, Paper, Scissors.\nRock crushes Scissors.\nScissors cuts Paper.\nPaper Covers Rock.")
while True:
    list = ["rock","paper","scissors"]
    try:
        CPU = random.choice(list)
        player = input("What is your choice; Rock, Paper or Scissors?").lower()

        if player not in list:
            raise Exception
        
    except:
        print("Not a valid selection, make a valid choice")
        
    if player == CPU:
        print("Player (",player, ")", ":""CPU (",CPU, ")")
        print("It is a tie! You have to try again")

    elif player == "rock":
        if CPU == "paper":
            print("Player (Rock):CPU (Paper)")
            print("CPU won!")
            break
        if CPU == "scissors":
            print("Player (Rock): CPU (Scissors)")
            print("Player won!")
            break

    elif player == "scissors":
        if CPU == "rock":
            print("Player (Scissors):CPU (Rock)")
            print("CPU won!")
            break
        if CPU == "paper":
            print("Player (Scissors):CPU (Paper)")
            print("Player won!")
            break

    elif player == "paper":
        if CPU == "scissors":
            print("Player (Paper):CPU (Scissors)")
            print("CPU won!")
            break
        if CPU == "rock":
            print("Player (Paper):CPU (Rock)")
            print("Player won!")
            break

    #play_again = input("will you like to play again? (yes or no)").lower()

    #if play_again != "yes":
        #break

#print("Bye!")