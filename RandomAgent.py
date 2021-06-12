import random
import numpy as np
from pysc2.agents import base_agent
from pysc2.lib import actions, features, units
from Agent import Agent


class RandomAgent(Agent):
    def step(self, obs):
        super(RandomAgent, self).step(obs)
        action = random.choice(self.actions)
        return getattr(self, action)(obs)
