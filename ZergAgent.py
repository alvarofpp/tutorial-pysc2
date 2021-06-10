from pysc2.agents import base_agent
from pysc2.lib import actions, units
import random


class ZergAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(ZergAgent, self).step(obs)

        drones = [unit for unit in obs.observation.feature_units
                  if unit.unit_type == units.Zerg.Drone]

        if len(drones) > 0:
            drone = random.choice(drones)
            return actions.FUNCTIONS.select_point('select_all_type', (drone.x, drone.y))

        return actions.FUNCTIONS.no_op()
