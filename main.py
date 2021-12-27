from class_Action import Action
from class_Galaxy import *

# =================================================================================================

galaxy = Galaxy()
galaxy.new_game()

spaceship = galaxy.spaceship
captain = spaceship.players[0]
player2 = spaceship.players[1]

captain.actions[0] = Action.GRAVOLIFT
player2.actions[0] = Action.GRAVOLIFT

captain.actions[1] = Action.MOVE_RED
player2.actions[1] = Action.MOVE_BLUE # This action is delayed because player2 used the lift at the same time as the captain

captain.actions[2] = Action.GRAVOLIFT

spaceship.resolve_game()
