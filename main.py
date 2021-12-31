from class_Action import Action
from class_Galaxy import *

# =================================================================================================

galaxy = Galaxy()
galaxy.new_game()

spaceship = galaxy.spaceship
captain = spaceship.players[0]
player2 = spaceship.players[1]
player3 = spaceship.players[2]

captain.actions[0] = Action.GRAVOLIFT
player2.actions[0] = Action.GRAVOLIFT
player3.actions[0] = Action.BUTTON_B

captain.actions[1] = Action.MOVE_RED
player2.actions[1] = Action.MOVE_BLUE # This action is delayed because player2 used the lift at the same time as the captain
player3.actions[1] = Action.MOVE_BLUE

captain.actions[2] = Action.GRAVOLIFT

player2.actions[3] = Action.BUTTON_A
player3.actions[3] = Action.BUTTON_A

player2.actions[4] = Action.BUTTON_A
player3.actions[4] = Action.BUTTON_A

spaceship.resolve_game()
