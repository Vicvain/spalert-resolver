from operator import attrgetter

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
    - fuel_capsules = available fuel capsules to recharge central reactor -> int

    Methods
    - new_game = prepare for new game -> /
    - resolve_game = run game, returns whether or not the players won -> bool
    """
    def __init__(self):
        self.red_zone = Zone(self, "red", max_energy=3, max_shield=2, upper_laser_damage=4, lower_laser_damage=2, lower_laser_range=3, lower_laser_type=WeaponType.LightLaser)
        self.white_zone = Zone(self, "white", max_energy=5, max_shield=3, upper_laser_damage=5, lower_laser_damage=1, lower_laser_range=2, lower_laser_type=WeaponType.PulseCannon)
        self.blue_zone = Zone(self, "blue", max_energy=3, max_shield=2, upper_laser_damage=4, lower_laser_damage=2, lower_laser_range=3, lower_laser_type=WeaponType.LightLaser)
        self.internal_threat_track = None
        self.players = []
        self.fuel_capsules = 0

    def new_game(self, internal_track, red_track, white_track, blue_track, players):
        self.red_zone.new_game(energy=2, threat_track=red_track)
        self.white_zone.new_game(energy=3, threat_track=white_track)
        self.blue_zone.new_game(energy=2, threat_track=blue_track)
        self.internal_threat_track = internal_track
        self.players = players
        self.fuel_capsules = 3

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
    
    @property
    def zones(self):
        yield self.red_zone
        yield self.white_zone
        yield self.blue_zone
    
    @property
    def external_threat_tracks(self):
        for zone in self.zones:
            yield zone.threat_track

    @property
    def threats(self):
        for track in self.external_threat_tracks:
            yield from track.threats
        yield from self.internal_threat_track.threats
    
    def resolve_game(self):
        try:
            for turn in range(13):
                print("Turn " + str(turn+1) + ":")
                for zone in self.zones:
                    zone.new_turn()
                
                if turn < 8:
                    # Threat appears
                    for threat in self.threats:
                        threat.try_spawn(current_turn=turn)

                if turn < 12:
                    # Player actions
                    for player in self.players:
                        player.play_action(turn)
                        print("Player " + player.color + " position: " + player.station.deck_str + " " + player.zone.color_str)

                # Compute targeting
                for track in self.external_threat_tracks:
                    active_threats = [threat for threat in track.threats if threat.is_active]
                    # Threats are sorted by how close they are to the ship. If tied, the earliest threat takes priority.
                    sorted(active_threats, key=attrgetter("position_on_track", "spawn_turn"))
                    
                    for threat in active_threats:
                        # Heavy and Light lasers
                        for station in track.zone.stations:
                            if station.laser_type != WeaponType.PulseCannon and station.fired_laser_cannon:
                                if threat.try_to_target(station.laser_strength, station.laser_range, station.laser_type):
                                    station.fired_laser_cannon = False
                        
                        # Pulse cannon
                        lower_white = self.white_zone.lower_station
                        if lower_white.fired_laser_cannon:
                            threat.try_to_target(lower_white.laser_strength, lower_white.laser_range, lower_white.laser_type)
                        
                        # Rocket TODO

                        # Interceptors TODO

                # Compute damage
                for track in self.external_threat_tracks:
                    active_threats = [threat for threat in track.threats if threat.is_active]
                    sorted(active_threats, key=attrgetter("spawn_turn"))
                    for threat in active_threats:
                        if threat.planned_damage > 0:
                            threat.damage(threat.planned_damage)
                            threat.planned_damage = 0
                    
                # Threat actions
                for threat in sorted(self.threats, key=attrgetter("spawn_turn")):
                    if threat.is_active:
                        threat.advance()
                        if threat.is_active:
                            print(threat.name + ": " + threat.track.zone.color_str + "[" + str(threat.position_on_track) + "]")
                
                # TODO rocket advance
        
        except ShipDestroyed as failure:
            print("Game lost :(")
            print(f"Reason: {failure}")
