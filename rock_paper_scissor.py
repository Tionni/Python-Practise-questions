def start_game():
    print("player 1 Rock, Paper, Scissor")
    player1 = input()
    print("player 2 Rock, Paper, Scissor")
    player2 = input()
    if player1 == player2:
        print("Tie")
    if player1 == 'R' and player2 == "P":
        print("congratulation Player 2 won")
    if player1 == 'P' and player2 == "R":
        print("congratulation Player 1 won")
    if player1 == 'P' and player2 == "S":
        print("congratulation Player 2 won")
    if player1 == 'S' and player2 == "P":
        print("congratulation Player 1 won")
    if player1 == 'R' and player2 == "S":
        print("congratulation Player 1 won")
    if player1 == 'S' and player2 == "R":
        print("congratulation Player 2 won")
start_game()
while True:
    print("Do you want to start a new game yes to continue, no to quit")
    game_over = input()
    if game_over == 'yes':
        start_game()
    else:
        break  
