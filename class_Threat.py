from functools import partialmethod
from enum import Enum

class Threat:
    """
    Definition of a threat
    - name -> str
    - health -> int
    - shield = prevents some damage each turn -> int
    - speed -> int
    - points_when_survived -> int
    - points_when_destroyed -> int
    - action_x = partial/function representing the threat's X action -> partial or function

    Game-dependant properties
    - track -> class ThreatTrack
    - position_on_track -> int
    - status = can be: NotYetSpawned, Active, Survived, Destroyed -> class ThreatStatus
    - spawn_turn = the turn at which the threat appears -> int
    """

    def __init__(self, name, health, shield, speed, points_when_survived, points_when_destroyed):
        self.name = name
        self.health = health
        self.shield = shield
        self.speed = speed
        self.points_when_survived = points_when_survived
        self.points_when_destroyed = points_when_destroyed
        self.action_x = None
        self.action_y = None
        self.action_z = None
        
        self.track = None
        self.position_on_track = None
        self.status = ThreatStatus.NotYetSpawned
        self.spawn_turn = None

    @property
    def is_active(self):
        return self.status == ThreatStatus.Active

    def try_spawn(self, current_turn):
        if self.spawn_turn == current_turn:
            self.position_on_track = len(self.track) - 1
            self.status = ThreatStatus.Active
            print(f"{self.name} spawns on {self.track.zone.color_str} track at distance {self.position_on_track}")
    
    def attack(self, attack_strength, targets=[]):
        if targets == []:
            targets = [self.track.zone]
        
        for target_zone in targets:
            target_zone.external_attack(attack_strength)

    def advance(self):
        speed = self.speed
        for i in range(speed):
            self.position_on_track -= 1
            match self.track.squares[self.position_on_track]:
                case "X":
                    self.action_x()

                case "Y":
                    self.action_y()

                case "Z":
                    self.action_z()
                    self.position_on_track = None
                    self.status = ThreatStatus.Survived
                    break
    
    def damage(self, damage):
        """
        Inflicts damage to the threat (reduced by shield)
        """
        damage -= self.shield
        if damage > 0:
            self.health -= damage
            if self.health <= 0:
                self.position_on_track = None
                self.status = ThreatStatus.Destroyed
        
class ThreatStatus(Enum):
    NotYetSpawned = 0
    Active = 1
    Survived = 2
    Destroyed = 3
