from pysc2.agents import base_agent
from pysc2.lib import actions


class ZergAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(ZergAgent, self).step(obs)

        #return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])
        return actions.FUNCTIONS.no_op()
