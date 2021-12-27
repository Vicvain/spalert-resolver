from class_Spaceship import *
from random import sample

class Galaxy():
    """
    Definition of the galaxy
    - spaceship = the spaceship the players move in -> class Spaceship
    - threat_tracks = all existing threat tracks -> [class ThreatTrack]
    - threats = all existing threats (maybe?) -> [class Threat] TODO
    - players = all five players -> [class Player]

    Methods
    - new_game = prepare for new game -> /
    """
    def __init__(self):
        self.spaceship = Spaceship()

        track_1 = ThreatTrack(["Z", None, None, None, "X", None, None, None, None, None])
        track_2 = ThreatTrack(["Z", None, None, None, None, None, None, "X", None, None, None])
        track_3 = ThreatTrack(["Z", None, "Y", None, None, None, None, "X", None, None, None, None])
        track_4 = ThreatTrack(["Z", None, None, None, "Y", None, None, None, "X", None, None, None, None])
        track_5 = ThreatTrack(["Z", None, None, None, None, None, "Y", None, None, None, "X", None, None, None])
        track_6 = ThreatTrack(["Z", None, "Y", None, None, None, "Y", None, None, "X", None, None, None, None, None])
        track_7 = ThreatTrack(["Z", None, None, None, "Y", None, None, "Y", None, None, None, "X", None, None, None, None])
        self.threat_tracks = [track_1, track_2, track_3, track_4, track_5, track_6, track_7]

        self.players = [Player("Cyan"), Player("Purple"), Player("Red"), Player("Green"), Player("Yellow")]

    def new_game(self):
        for threat in self.threat_tracks:
            threat.new_game()

        for player in self.players:
            player.new_game(self.spaceship.white_zone.upper_station)
        
        selected_tracks = sample(self.threat_tracks, 4)
        # TODO: player selection
        self.spaceship.new_game(selected_tracks[0], selected_tracks[1], selected_tracks[2], selected_tracks[3], self.players[:4])