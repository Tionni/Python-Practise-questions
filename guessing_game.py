import random
def start_game():
    random_num =random.randint(1, 9)
    print("Quess a number between 1 and 9")
    user_number = int(input())
    if user_number < random_num:
        print('too low')
    elif user_number > random_num:
        print('too high')
    else:
        print("You are right")

    return user_number
guesses = [] 
while True: 
      
    print("Type exit to stop")
    game_state = input()
    if game_state != "exit":
        g = start_game()
        print(g)
        guesses.append(g)
    else:
        print(guesses)
        break


