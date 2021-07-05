import random
from Agent import Agent


class RandomAgent(Agent):
    def step(self, obs):
        super(RandomAgent, self).step(obs)
        action = random.choice(self.actions)
        return getattr(self, action)(obs)
