from _lux.observation import _GameState


class _Board:

    def __init__(self, board: dict):

        self.rubble = self.init_rubble(board)
        self.lichen = self.init_lichen(board)
        self.lichen_strains = self.init_lichen_strains(board)
        self.spawns = self.init_valid_spawns_mask(board)
        self.factories_per_team = self.init_factories_per_team(board)

    def init_rubble(self, board: dict) -> list[list[int]]:

        if "rubble" not in board:
            return [[]]

        if board["rubble"]:
            return board["rubble"]

        return [[]]

    def init_lichen(self, board: dict) -> list[list[int]]:

        if "lichen" not in board:
            return [[]]

        if board["lichen"]:
            return board["lichen"]

        return [[]]

    def init_lichen_strains(self, board: dict) -> list[list[int]]:

        if "lichen_strains" not in board:
            return [[]]

        if board["lichen_strains"]:
            return board["lichen_strains"]

        return [[]]

    def init_valid_spawns_mask(self, board: dict) -> list[tuple[int, int]]:

        if "valid_spawns_mask" not in board:
            return []

        spawns = []

        if board["valid_spawns_mask"]:
            for y in range(len(board["valid_spawns_mask"])):
                for x in range(len(board["valid_spawns_mask"][0])):
                    if board["valid_spawns_mask"][y][x] is True:
                        spawns.append((y, x))

        return spawns

    def init_factories_per_team(self, board: dict) -> int:
        if "factories_per_team" not in board:
            return 0

        if board["factories_per_team"]:
            return board["factories_per_team"]

        return 0
