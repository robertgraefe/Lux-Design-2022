import json
from argparse import Namespace

from _lux.observation import _GameState
from agent import Agent
from lux.config import EnvConfig
from lux.kit import GameState, process_obs, to_json, from_json, process_action, obs_to_game_state

### DO NOT REMOVE THE FOLLOWING CODE ###
agent_dict = dict()  # store potentially multiple dictionaries as kaggle imports code directly
agent_prev_obs = dict()

import logging

logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.DEBUG, filemode='w')


def agent_fn(observation, configurations):
    """
    agent definition for kaggle submission.
    """
    global agent_dict

    if "env_cfg" not in agent_dict:
        agent_dict["env_cfg"] = EnvConfig.from_dict(configurations["env_cfg"])

    env_cfg: EnvConfig = agent_dict["env_cfg"]

    game_state: _GameState = _GameState(observation, env_cfg)

    agent: Agent = Agent(game_state)

    agent.early_setup()

    logging.info(agent.player.water)

    return process_action(agent.action.actions)


if __name__ == "__main__":

    def read_input():
        """
        Reads input from stdin
        """
        try:
            return input()
        except EOFError as eof:
            raise SystemExit(eof)


    step = 0
    player_id = 0
    configurations = None
    i = 0
    while True:
        inputs = read_input()
        obs = json.loads(inputs)

        observation = Namespace(
            **dict(step=obs["step"], obs=json.dumps(obs["obs"]), remainingOverageTime=obs["remainingOverageTime"],
                   player=obs["player"], info=obs["info"]))
        if i == 0:
            configurations = obs["info"]["env_cfg"]
        i += 1
        actions = agent_fn(observation, dict(env_cfg=configurations))
        # send actions to engine
        print(json.dumps(actions))
