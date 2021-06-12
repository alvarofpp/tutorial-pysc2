from pysc2.agents import base_agent
from pysc2.lib import actions, features, units


class RawAgent(base_agent.BaseAgent):
    def __init__(self):
        super(RawAgent, self).__init__()
        self.base_top_left = None

    def get_my_units_by_type(self, obs, unit_type):
        return [unit for unit in obs.observation.raw_units
                if unit.unit_type == unit_type
                and unit.alliance == features.PlayerRelative.SELF]

    def step(self, obs):
        super(RawAgent, self).step(obs)

        if obs.first():
            nexus = self.get_my_units_by_type(obs, units.Protoss.Nexus)[0]
            self.base_top_left = (nexus.x < 32)

        return actions.RAW_FUNCTIONS.no_op()
