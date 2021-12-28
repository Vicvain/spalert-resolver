from class_Spaceship import *
from random import sample

class Galaxy():
    """
    Definition of the galaxy
    - players = all five players -> [class Player]
    - spaceship = the spaceship the players move in -> class Spaceship
    - threat_tracks = all existing threat tracks -> [class ThreatTrack]
    - white_external_threats = all existing white external threats -> [class Threat]
    - threats = all existing threats (maybe?) -> [class Threat] TODO

    Methods
    - new_game = prepare for new game -> /
    """
    def __init__(self):
        self.players = [Player("Cyan"), Player("Purple"), Player("Red"), Player("Green"), Player("Yellow")]
        self.spaceship = Spaceship()

        track_1 = ThreatTrack(["Z", None, None, None, "X", None, None, None, None, None])
        track_2 = ThreatTrack(["Z", None, None, None, None, None, None, "X", None, None, None])
        track_3 = ThreatTrack(["Z", None, "Y", None, None, None, None, "X", None, None, None, None])
        track_4 = ThreatTrack(["Z", None, None, None, "Y", None, None, None, "X", None, None, None, None])
        track_5 = ThreatTrack(["Z", None, None, None, None, None, "Y", None, None, None, "X", None, None, None])
        track_6 = ThreatTrack(["Z", None, "Y", None, None, None, "Y", None, None, "X", None, None, None, None, None])
        track_7 = ThreatTrack(["Z", None, None, None, "Y", None, None, "Y", None, None, None, "X", None, None, None, None])
        self.threat_tracks = [track_1, track_2, track_3, track_4, track_5, track_6, track_7]

        # See https://stackoverflow.com/a/59582067 for explanation on partialmethod
        e1_05 = Threat(name="Gunship", health=5, shield=2, speed=2, points_when_survived=2, points_when_destroyed=4)
        e1_05.action_x = partialmethod(Threat.attack, attack_strength=2).__get__(e1_05, Threat)
        e1_05.action_y = partialmethod(Threat.attack, attack_strength=2).__get__(e1_05, Threat)
        e1_05.action_z = partialmethod(Threat.attack, attack_strength=3).__get__(e1_05, Threat)

        e1_07 = Threat(name="Fighter", health=4, shield=2, speed=3, points_when_survived=2, points_when_destroyed=4)
        e1_07.action_x = partialmethod(Threat.attack, attack_strength=1).__get__(e1_07, Threat)
        e1_07.action_y = partialmethod(Threat.attack, attack_strength=2).__get__(e1_07, Threat)
        e1_07.action_z = partialmethod(Threat.attack, attack_strength=3).__get__(e1_07, Threat)

        self.white_external_threats = [e1_05, e1_07]

    def new_game(self):
        for track in self.threat_tracks:
            track.new_game()

        for player in self.players:
            player.new_game(self.spaceship.white_zone.upper_station)
        
        # TODO: player selection

        selected_tracks = sample(self.threat_tracks, 4)
        selected_tracks[0].zone = self.spaceship.red_zone
        selected_tracks[1].zone = self.spaceship.white_zone
        selected_tracks[2].zone = self.spaceship.blue_zone

        # TODO: threat selection
        threat1 = self.white_external_threats[0]
        threat2 = self.white_external_threats[1]
        selected_tracks[1].assign_threat(threat=threat1, spawn_turn=2)
        selected_tracks[1].assign_threat(threat=threat2, spawn_turn=7)

        self.spaceship.new_game(selected_tracks[0], selected_tracks[1], selected_tracks[2], selected_tracks[3], self.players[:4])