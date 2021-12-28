from random import shuffle
from class_Station import *

class Zone():
    """
    Definition of a zone
    - color_str = color used for display purposes -> str
    - upper_station -> class Station
    - lower_station -> class Station
    - energy = quantity of energy in the reactor -> int
    - shield = quantity of energy in the shield -> int
    - threat_track = track for incoming external threats -> class ThreatTrack
    - damage_pile -> [class ZoneDamage]
    - damages -> [class ZoneDamage]
    - used_gravolift = the gravolift has already been used this turn -> bool

    Methods
    - new_game = prepare for new game -> /
    - new_turn = prepare for a new turn -> /
    """

    def __init__(self, color_str):
        self.color_str = color_str
        self.upper_station = Station(self, "upper")
        self.lower_station = Station(self, "lower")
        self.energy = 0
        self.shield = 0
        self.threat_track = None
        self.damage_pile = []
        self.damages = []
        self.used_gravolift = False

        # Assign station neighbors (using gravolift)
        self.upper_station.other_deck = self.lower_station
        self.lower_station.other_deck = self.upper_station

    def deal_damage(self, attack_strength):
        """
        Deals n damage to the zone, where n is attack_strength.
        Raises a ZoneDestroyed exception if the players screwed up.
        """
        print(f"{self.color_str} zone takes {attack_strength} damage")
        for i in range(attack_strength):
            if len(self.damage_pile) == 0:
                raise ShipDestroyed(f"{self.color_str} zone destroyed")

            damage_token = self.damage_pile.pop()
            # TODO damage consequences
            self.damages.append(damage_token)

    def external_attack(self, attack_strength):
        while attack_strength > 0 and self.shield > 0:
            attack_strength -= 1
            self.shield -= 1
        
        if attack_strength > 0:
            self.deal_damage(attack_strength)

    def new_game(self, energy, threat_track):
        self.energy = energy
        self.shield = 1
        self.threat_track = threat_track
        self.damage_pile = [damage.value for damage in ZoneDamage]
        shuffle(self.damage_pile)
        self.damages = []

        self.upper_station.new_game()
        self.lower_station.new_game()
    
    def new_turn(self):
        self.used_gravolift = False

class ZoneDamage(Enum):
    UpperLaser = 0
    LowerLaser = 1
    Gravolift = 2
    Shield = 3
    Reactor = 4
    Structural = 5

class ShipDestroyed(Exception):
    """
    - cause = the reason the ship was destroyed -> str
    """
    
    def __init__(self, cause):
        self.cause = cause

    def __str__(self) -> str:
        return self.cause
