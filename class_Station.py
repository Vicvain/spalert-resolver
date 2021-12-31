from enum import Enum

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
    - laser_strength = quantity of damage dealt by this laser -> int
    - laser_range = range of this laser (1 to 3) -> int
    - laser_type = type of weapon (HeavyLaser, LightLaser or PulseCannon) -> class WeaponType
    
    Game-dependant properties
    - players = players currently in this station -> [class Player]
    - internal_threats -> [class Threat]
    - fired_laser_cannon = whether or not the laser fired this turn already -> bool

    Methods
    - action_a
    - action_b
    - action_c
    - new_game = prepare for new game -> /
    """

    def __init__(self, parent_zone, deck_str, laser_strength, laser_range, laser_type):
        self.zone = parent_zone
        self.deck_str = deck_str
        self.towards_red = None
        self.towards_blue = None
        self.other_deck = None
        self.laser_strength = laser_strength
        self.laser_range = laser_range
        self.laser_type = laser_type

        self.players = []
        self.internal_threats = []
        self.fired_laser_cannon = False

    def fire_laser(self):
        if not self.fired_laser_cannon:
            if self.laser_type != WeaponType.LightLaser:
                if self.zone.energy <= 0:
                    return
                self.zone.energy -= 1
                
            self.fired_laser_cannon = True

    def new_game(self):
        self.players = []
        self.internal_threats = []

    def new_turn(self):
        self.fired_laser_cannon = False

class WeaponType(Enum):
    HeavyLaser = 0
    LightLaser = 1
    PulseCannon = 2
    Rocket = 3
    Interceptors = 4
