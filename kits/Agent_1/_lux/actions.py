

class Faction:
    AlphaStrike = "AlphaStrike"
    MotherMars = "MotherMars"
    TheBuilders = "TheBuilders"
    FirstMars = "FirstMars"


class Action:
    actions: dict

    def __init__(self):
        self.actions = {}

    def bid(self, bid: int):
        self.actions.update(dict(bid=bid))

    def fraction(self, faction: Faction):
        self.actions.update(dict(faction=faction))

    def spawn(self, spawn: tuple[int, int]):
        self.actions.update(dict(spawn=list(spawn)))

    def metal(self, metal: int):
        self.actions.update(dict(metal=metal))

    def water(self, water: int):
        self.actions.update(dict(water=water))
