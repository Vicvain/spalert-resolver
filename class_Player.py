from class_Action import *
from class_Station import *

class Player:
    """
    Definition of a player
    - color -> str
    - actions -> [class Action]
    - station = the station the player is currently in -> class Station

    Methods
    - new_game = prepare for new game -> /
    - play_action: plays its action for a given turn, turn -> /
    """

    def __init__(self, color):
        self.color = color
        self.actions = [None] * 12
        self.station = None

    @ property
    def zone(self):
        return self.station.zone

    def new_game(self, white_upper_station):
        self.actions = [None] * 12
        self.station = white_upper_station

    def move(self, destination):
        self.station.players.remove(self)
        destination.players.append(self)
        self.station = destination
    
    def delay(self, turn):
        previous_action = None
        while self.actions[turn] is not None:
            current_action = self.actions[turn]
            self.actions[turn] = previous_action
            previous_action = current_action
            
            # Note: doing it this way discards any 13th turn action, think about whether keeping it is desirable in any way or not
            turn += 1
            if turn >= len(self.actions):
                return
                
        # Don't forget to add back the last action
        if previous_action is not None:
            self.actions[turn] = previous_action
    
    def play_action(self, turn):
        match self.actions[turn]:
            case Action.MOVE_RED:
                destination = self.station.towards_red
                if destination is not None:
                    self.move(destination)

            case Action.MOVE_BLUE:
                destination = self.station.towards_blue
                if destination is not None:
                    self.move(destination)

            case Action.GRAVOLIFT:
                destination = self.station.other_deck
                
                if self.zone.used_gravolift:
                    self.delay(turn + 1)

                self.move(destination)
                self.zone.used_gravolift = True

            case Action.BUTTON_A:
                pass

            case Action.BUTTON_B:
                pass

            case Action.BUTTON_C:
                pass

            case Action.BATTLE_BOTS:
                pass