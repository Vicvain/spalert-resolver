from class_Zone import *
from class_ThreatTrack import *

class Spaceship():
    """
    Definition of the spaceship
    - red_zone = port side (left) zone -> class Zone
    - white_zone = middle zone (bridge) -> class Zone
    - blue_zone = starboard side (right) zone -> class Zone
    - internal_threat_track -> class ThreatTrack
    - players = all playing players -> [class Player]

    Methods
    - new_game = prepare for new game -> /
    - resolve_game = run game, returns whether or not the players won -> bool
    """
    def __init__(self):
        self.red_zone = Zone("red")
        self.white_zone = Zone("white")
        self.blue_zone = Zone("blue")
        self.internal_threat_track = None
        self.players = []

    def new_game(self, internal_track, red_track, white_track, blue_track, players):
        self.red_zone.new_game(energy=2, threat_track=red_track)
        self.white_zone.new_game(energy=3, threat_track=white_track)
        self.blue_zone.new_game(energy=2, threat_track=blue_track)
        self.internal_threat_track = internal_track
        self.players = players

        # Assign station neighbors
        # -> Towards blue side 
        self.red_zone.upper_station.towards_blue = self.white_zone.upper_station
        self.red_zone.lower_station.towards_blue = self.white_zone.lower_station
        self.white_zone.upper_station.towards_blue = self.blue_zone.upper_station
        self.white_zone.lower_station.towards_blue = self.blue_zone.lower_station
        # -> Towards red side
        self.blue_zone.upper_station.towards_red = self.white_zone.upper_station
        self.blue_zone.lower_station.towards_red = self.white_zone.lower_station
        self.white_zone.upper_station.towards_red = self.red_zone.upper_station
        self.white_zone.lower_station.towards_red = self.red_zone.lower_station

        # Put all players on bridge
        self.white_zone.upper_station.players = list(players) # Making a shallow copy here is important
    
    def zones(self):
        yield self.red_zone
        yield self.white_zone
        yield self.blue_zone
    
    def resolve_game(self):
        for turn in range(12):
            print("Turn " + str(turn+1) + ":")
            for zone in self.zones():
                zone.new_turn()

            for player in self.players:
                player.play_action(turn)
                print("Player " + player.color + " position: " + player.station.deck_str + " " + player.zone.color_str)
                