from _lux.observation import _GameState


class _Player:
    id: str
    units: dict
    water: int
    metal: int
    factories_to_place: int
    my_turn_to_place: bool

    def __init__(self, id: str, game_state: '_GameState'):
        self.id = id
        self.units = game_state.observation["units"][id]
        self.water = self.init_water(game_state)
        self.metal = self.init_metal(game_state)
        self.factories_to_place: int = self.init_factories_to_place(game_state)
        self.my_turn_to_place: bool = self.init_my_turn_to_place(game_state)
        self.factories = self.

    def init_water(self, game_state) -> int:
        if self.id not in game_state.observation["teams"]:
            return 0

        if "water" not in game_state.observation["teams"][self.id]:
            return 0

        return game_state.observation["teams"][self.id]["water"]

    def init_metal(self, game_state) -> int:
        if self.id not in game_state.observation["teams"]:
            return 0

        if "metal" not in game_state.observation["teams"][self.id]:
            return 0

        return game_state.observation["teams"][self.id]["metal"]

    def init_factories_to_place(self, game_state):
        if self.id not in game_state.observation["teams"]:
            return 0

        if "factories_to_place" not in game_state.observation["teams"][self.id]:
            return 0

        return game_state.observation["teams"][self.id]["factories_to_place"]

    def init_my_turn_to_place(self, game_state) -> bool:

        place_first: bool = False

        if self.id in game_state.observation["teams"]:
            if "place_first" in game_state.observation["teams"][self.id]:
                place_first = game_state.observation["teams"][self.id]["place_first"]

        if place_first:
            if game_state.step % 2 == 1:
                return True
        else:
            if game_state.step % 2 == 0:
                return True
        return False
