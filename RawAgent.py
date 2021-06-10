from pysc2.agents import base_agent
from pysc2.lib import actions


class RawAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(RawAgent, self).step(obs)

        return actions.RAW_FUNCTIONS.no_op()
