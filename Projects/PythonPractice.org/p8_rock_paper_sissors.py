# Rock Paper Scissors Game
import random
replay = 'y'
moves = ['rock', 'paper', 'scissor']

while replay == 'y':
    print("Hello, welcome to Rock Paper Scissors!")
    while True:
        move = input("Enter your move: ").lower()
        if move == 'rock' or move == 'paper' or move == 'scissor':
            opponent_pick = random.choice(moves)
            if move == opponent_pick:
                print("Tie, try again")
                continue
            elif move == 'rock':
                if opponent_pick == 'paper':
                    print(f"{move} loses to  {opponent_pick}")
                else:
                    print(f"{move} beats {opponent_pick}")
            elif move == 'paper':
                if opponent_pick == 'scissor':
                    print(f"{move} loses to {opponent_pick}")
                else:
                    print(f"{move} beats {opponent_pick}")
            elif move == 'scissor':
                if opponent_pick == 'rock':
                    print(f"{move} loses to {opponent_pick}")
                else:
                    print(f"{move} beats {opponent_pick}")
            break
        else:
            continue

    replay = input("Replay? [y/n]: ").lower()  # guides the while loop





