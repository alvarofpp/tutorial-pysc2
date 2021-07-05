import random
from TerranAgent import TerranAgent
from pysc2.lib import actions


class EnemyAgent(TerranAgent):
    def __init__(self, bm):
        super(EnemyAgent, self).__init__()
        self.bm = bm

    def step(self, obs):
        super(EnemyAgent, self).step(obs)

        if obs.first():
            self.bm.enemy_ready = False
            self.bm.enemy_marines = random.randint(1, 10)
            print("enemy", self.bm.enemy_marines)
        if len(self.marines) == self.bm.enemy_marines and not self.bm.enemy_ready:
            print("enemy ready")
            self.bm.enemy_ready = True
        if self.bm.predictor_ready and self.bm.enemy_ready:
            return self.attack()
        if self.supply_depot is None:
            return self.build_supply_depot()
        if self.barracks is None:
            return self.build_barracks()
        if len(self.marines) + self.queued_marine_count < self.bm.enemy_marines:
            return self.train_marine()

        return actions.RAW_FUNCTIONS.no_op()
