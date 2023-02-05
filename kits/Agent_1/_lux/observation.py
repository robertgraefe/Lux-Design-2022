import json

from lux.config import EnvConfig


class _GameState:

    def __init__(self, observation, config: EnvConfig):
        self.step: int = observation.step
        self.player_id: str = observation.player
        self.opponent_id: str = "player_1" if observation.player == "player_0" else "player_0"
        self.remainingOverageTime: int = observation.remainingOverageTime

        # observation
        self.observation: dict = json.loads(observation.obs)

        self.config: EnvConfig = config


