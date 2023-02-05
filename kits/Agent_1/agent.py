import random

from _lux.actions import Faction, Action
from _lux.board import _Board
from _lux.observation import _GameState
from _lux.player import _Player
from lux.kit import obs_to_game_state, EnvConfig, GameState
from lux.utils import direction_to, my_turn_to_place_factory
import numpy as np


class Agent:

    def __init__(self, game_state: _GameState) -> None:

        self.step = game_state.step

        self.player: _Player = _Player(game_state.player_id, game_state)

        self.opponent: _Player = _Player(game_state.opponent_id, game_state)

        self.board: _Board = _Board(game_state.observation["board"])

        self.action: Action = Action()

        np.random.seed(0)

    def early_setup(self):

        if self.step == 0:

            self.action.bid(0)

            self.action.fraction(Faction.AlphaStrike)

        if self.player.my_turn_to_place and self.player.factories_to_place > 0:

            random_spawn = random.choice(self.board.spawns)

            self.action.spawn(random_spawn)

            self.action.metal(int(self.player.metal / self.player.factories_to_place))

            self.action.water(int(self.player.water / self.player.factories_to_place))

    def act(self):








    # def _early_setup(self, step: int, obs, remainingOverageTime: int = 60):
    #
    #     if step == 0:
    #
    #         # bid 0 to not waste resources bidding and declare as the default faction
    #         return dict(faction="AlphaStrike", bid=0)
    #
    #     else:
    #
    #         game_state = obs_to_game_state(step, self.env_cfg, obs)
    #         # factory placement period
    #
    #         # how much water and metal you have in your starting pool to give to new factories
    #         water_left = game_state.teams[self.player.id].water
    #         metal_left = game_state.teams[self.player.id].metal
    #
    #         # how many factories you have left to place
    #         factories_to_place = game_state.teams[self.player.id].factories_to_place
    #
    #         # whether it is your turn to place a factory
             # my_turn_to_place = my_turn_to_place_factory(game_state.teams[self.player.id].place_first, step)
    #
    #         if factories_to_place > 0 and my_turn_to_place:
    #             # we will spawn our factory in a random location with 150 metal and water if it is our turn to place
    #             potential_spawns = np.array(list(zip(*np.where(obs["board"]["valid_spawns_mask"] == 1))))
    #
    #             spawn_loc = potential_spawns[np.random.randint(0, len(potential_spawns))]
    #
    #             #logging.info(dict(spawn=spawn_loc, metal=150, water=150))
    #
    #             return dict(spawn=spawn_loc, metal=150, water=150)
    #
    #         return dict()

    # def act(self, step: int, obs, remainingOverageTime: int = 60):
    #     actions = dict()
    #     game_state = obs_to_game_state(step, self.env_cfg, obs)
    #     factories = game_state.factories[self.player.id]
    #     game_state.teams[self.player.id].place_first
    #     factory_tiles, factory_units = [], []
    #     for unit_id, factory in factories.items():
    #         if factory.power >= self.env_cfg.ROBOTS["HEAVY"].POWER_COST and \
    #                 factory.cargo.metal >= self.env_cfg.ROBOTS["HEAVY"].METAL_COST:
    #             actions[unit_id] = factory.build_heavy()
    #         if self.env_cfg.max_episode_length - game_state.real_env_steps < 50:
    #             if factory.water_cost(game_state) <= factory.cargo.water:
    #                 actions[unit_id] = factory.water()
    #         factory_tiles += [factory.pos]
    #         factory_units += [factory]
    #     factory_tiles = np.array(factory_tiles)
    #
    #     units = game_state.units[self.player.id]
    #     ice_map = game_state.board.ice
    #     ice_tile_locations = np.argwhere(ice_map == 1)
    #     for unit_id, unit in units.items():
    #
    #         # track the closest factory
    #         closest_factory = None
    #         adjacent_to_factory = False
    #         if len(factory_tiles) > 0:
    #             factory_distances = np.mean((factory_tiles - unit.pos) ** 2, 1)
    #             closest_factory_tile = factory_tiles[np.argmin(factory_distances)]
    #             closest_factory = factory_units[np.argmin(factory_distances)]
    #             adjacent_to_factory = np.mean((closest_factory_tile - unit.pos) ** 2) == 0
    #
    #             # previous ice mining code
    #             if unit.cargo.ice < 40:
    #                 ice_tile_distances = np.mean((ice_tile_locations - unit.pos) ** 2, 1)
    #                 closest_ice_tile = ice_tile_locations[np.argmin(ice_tile_distances)]
    #                 if np.all(closest_ice_tile == unit.pos):
    #                     if unit.power >= unit.dig_cost(game_state) + unit.action_queue_cost(game_state):
    #                         actions[unit_id] = [unit.dig(repeat=False)]
    #                 else:
    #                     direction = direction_to(unit.pos, closest_ice_tile)
    #                     move_cost = unit.move_cost(game_state, direction)
    #                     if move_cost is not None and unit.power >= move_cost + unit.action_queue_cost(game_state):
    #                         actions[unit_id] = [unit.move(direction, repeat=False)]
    #             # else if we have enough ice, we go back to the factory and dump it.
    #             elif unit.cargo.ice >= 40:
    #                 direction = direction_to(unit.pos, closest_factory_tile)
    #                 if adjacent_to_factory:
    #                     if unit.power >= unit.action_queue_cost(game_state):
    #                         actions[unit_id] = [unit.transfer(direction, 0, unit.cargo.ice, repeat=False)]
    #                 else:
    #                     move_cost = unit.move_cost(game_state, direction)
    #                     if move_cost is not None and unit.power >= move_cost + unit.action_queue_cost(game_state):
    #                         actions[unit_id] = [unit.move(direction, repeat=False)]
    #     return actions
