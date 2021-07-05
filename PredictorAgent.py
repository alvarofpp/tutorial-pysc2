import csv
import random
from TerranAgent import TerranAgent
from pysc2.lib import actions


class PredictorAgent(TerranAgent):
    def __init__(self, bm):
        super(PredictorAgent, self).__init__()
        self.bm = bm

    def step(self, obs):
        super(PredictorAgent, self).step(obs)

        if obs.first():
            self.bm.predictor_ready = False
            self.bm.predictor_marines = random.randint(1, 10)
            print("predictor", self.bm.predictor_marines)
        if obs.last():
            print(self.bm.predictor_marines, self.bm.enemy_marines, obs.reward)
            with open("tvt.csv", "a", newline="\n") as myfile:
                csvwriter = csv.writer(myfile)
                csvwriter.writerow([self.bm.predictor_marines,
                                    self.bm.enemy_marines,
                                    obs.reward])
        if (len(self.marines) == self.bm.predictor_marines and
                not self.bm.predictor_ready):
            print("predictor ready")
            self.bm.predictor_ready = True
        if self.bm.predictor_ready and self.bm.enemy_ready:
            return self.attack()
        if self.supply_depot is None:
            return self.build_supply_depot()
        if self.barracks is None:
            return self.build_barracks()
        if len(self.marines) + self.queued_marine_count < self.bm.predictor_marines:
            return self.train_marine()
        return actions.RAW_FUNCTIONS.no_op()
