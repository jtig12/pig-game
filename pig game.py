import random


# defined the roll functions
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


# defined the amount of players that can play the game
while True:
    players = input("Enter the number of players (2-4): ")
    # this is used to check if it contains only the variable containns only numbers
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid, try again.")

# define the score system
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    # initiate for all players
    for player_indx in range(players):
        print("\nplayer", player_indx + 1, "has already started")
        print("Your total score is ", player_scores[player_indx], "\n")
        current_score = 0
        while True:
            # how the players can initiate the function
            should_roll = input("would you like to roll(enter y)? ")
            if should_roll.lower() == "y":
                value = roll()
            else:
                break
            # condition of operation
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            print("Your score is: ", current_score)
        player_scores[player_indx] += current_score
        print("\nyour total score is: ", player_scores[player_indx])
        print("player", player_indx + 1, "turn as ended")

max_score = max(player_scores)
winning_indx = player_scores.index(max_score)
print("\nplayer", winning_indx + 1, "is the winner with a score ", max_score)
