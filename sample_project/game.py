import random
import logging

class Game:
    logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def roll_dice(self, player):
        dice_value = random.randint(1,6)
        logging.info(f"{player.get_name()}\'s dice value is {dice_value}")
        player.update_score(dice_value)
        return dice_value
        
    def get_winner(self):
        logger = logging.getLogger("game")
        logger.info("***********************************")
        logger.info("***********************************")

        logger.info(f"{self.player1.get_name()}\'s total dice value is {self.player1.get_score()}")
        logger.info("***********************************")
        logger.info(f"{self.player2.get_name()}\'s total dice value is {self.player2.get_score()}")
        logger.info("***********************************")
        if self.player1.get_score() > self.player2.get_score():
            return "Player1 is the winner!"
        elif self.player2.get_score() > self.player1.get_score():
            return "Player2 is the winner!"
        else:
            return "The game was a draw"
        logger.info("for conflict")