import random

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    def roll_dice(self, player):
        dice_value = random.randint(1,6)
        print(f"{player.get_name()}\'s dice value is {dice_value}")
        player.update_score(dice_value)
        return dice_value
        
    def get_winner(self):
        print("===================================")
        print(f"{self.player1.get_name()}\'s total dice value is {self.player1.get_score()}")
        print("===================================")
        print(f"{self.player2.get_name()}\'s total dice value is {self.player2.get_score()}")
        print("===================================")
        if self.player1.get_score() > self.player2.get_score():
            return "Player1 is the winner!"
        elif self.player2.get_score() > self.player1.get_score():
            return "Player2 is the winner!"
        else:
            return "The game was a draw"