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
        self.used_gravolift = False

        # Assign station neighbors (using gravolift)
        self.upper_station.other_deck = self.lower_station
        self.lower_station.other_deck = self.upper_station

    def new_game(self, energy, threat_track):
        self.energy = energy
        self.shield = 1
        self.threat_track = threat_track

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
