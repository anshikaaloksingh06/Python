print("Name: Anshikaa A Singh")
print("USN: 1AY24AI011")
print("Section: M")
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        return [random.choice(['brain', 'shotgun', 'footprint']) for _ in range(3)]

def play_game():
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    player1 = Player(player1_name)
    player2 = Player(player2_name)

    while True:
        for player in [player1, player2]:
            print(f"{player.name}'s turn")
            input("Press Enter to roll the dice...")
            rolls = player.roll_dice()
            print(f"Rolled: {rolls}")
            brains = rolls.count('brain')
            shotguns = rolls.count('shotgun')
            player.score += brains
            print(f"{player.name} scored {brains} brains. Total score: {player.score}")

            if shotguns > 0:
                print(f"{player.name} got shotguns! Turn over.")
                break

        if player.score >= 13:
            print(f"{player.name} wins with a score of {player.score}!")
            break

play_game()
