from class_Player import *

class Station:
    """
    Definition of a station
    - zone = this station's parent zone -> class Zone
    - deck_str = deck used for display purposes -> str
    - players = players currently in this station -> [class Player]
    - internal_threats -> [class Threat]
    - towards_red = station to the left, can be the same (red) -> class Station
    - towards_blue = station to the right, can be the same (blue) -> class Station
    - other_deck = station on the other deck, using the gravolift -> class Station

    Methods
    - action_a
    - action_b
    - action_c
    - new_game = prepare for new game -> /
    """

    def __init__(self, parent_zone, deck_str):
        self.zone = parent_zone
        self.deck_str = deck_str
        self.players = []
        self.internal_threats = []
        self.towards_red = None
        self.towards_blue = None
        self.other_deck = None

    def new_game(self):
        pass