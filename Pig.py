import random


def roll():
    max_value = 6
    min_value= 1
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input('Enter the random of numbers from (2-4)')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 to 4 players")
    else:
        print("Invalid, Please try Again")

max_scores = 50
player_scores = [0 for _ in range(players)]
print(player_scores)

while max(player_scores) < max_scores:

    for players_idx in range(players):
        print("\nPlayer", players_idx + 1, "turn has just started\n")
        currentScore = 0

        while True:
            should_roll = input('Would you like to roll(y)')
            if should_roll.lower == "y":
              break

            value = roll()
            if value == 1:
                print("You rolled a one! You are done")
                currentScore = 0
                break
            else:
                currentScore += value
                print("You rolled a ", value)

            print("Your score is ", currentScore)

        player_scores[players_idx] += currentScore
        print('Your total score is', player_scores[players_idx])
    
max_scores = max(player_scores)
winningIDX = player_scores.index(max)
print("Player number", winningIDX + 1)
