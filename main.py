from absl import app
from pysc2.lib import actions, features
from pysc2.env import sc2_env, run_loop
from BattleManager import BattleManager
from PredictorAgent import PredictorAgent
from EnemyAgent import EnemyAgent


def main(unused_argv):
    bm = BattleManager()
    agent1 = PredictorAgent(bm)
    agent2 = EnemyAgent(bm)
    try:
        with sc2_env.SC2Env(
                map_name="Flat128",
                players=[sc2_env.Agent(sc2_env.Race.terran),
                         sc2_env.Agent(sc2_env.Race.terran)],
                agent_interface_format=features.AgentInterfaceFormat(
                    action_space=actions.ActionSpace.RAW,
                    use_raw_units=True,
                    raw_resolution=64,
                ),
                step_mul=128,
                disable_fog=True,
        ) as env:
            run_loop.run_loop([agent1, agent2], env, max_episodes=20)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    app.run(main)
