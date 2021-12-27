class ThreatTrack:
    """
    Definition of a threat track
    - threats -> [class Threat]
    - squares = list of squares containing either nothing of a threat action ("X", "Y", "Z") -> [str]

    Methods
    - new_game = prepare for new game -> /
    """

    def __init__(self, squares):
        self.threats = []
        self.squares = squares

    def new_game(self):
        self.threats = []