from game import Game
from player import Player

player1 = Player("pooja","India")
player2 = Player("Ankita","Usa")

game1 = Game(player1,player2)
game1.roll_dice(player1)
game1.roll_dice(player2)
game1.roll_dice(player1)
game1.roll_dice(player2)
game1.roll_dice(player1)
game1.roll_dice(player2)
game1.get_winner()