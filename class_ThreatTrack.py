from class_Threat import *

class ThreatTrack:
    """
    Definition of a threat track
    - zone = the zone the track is linked to (if internal threat track, this is None) -> class Zone
    - threats -> [class Threat]
    - squares = list of squares containing either nothing of a threat action ("X", "Y", "Z") -> [str]

    Methods
    - new_game = prepare for new game -> /
    """

    def __init__(self, squares):
        self.zone = None
        self.threats = []
        self.squares = squares

    def __len__(self):
        return len(self.squares)

    def new_game(self):
        self.zone = None
        self.threats = []

    def assign_threat(self, threat, spawn_turn):
        self.threats.append(threat)
        threat.track = self
        threat.spawn_turn = spawn_turn
