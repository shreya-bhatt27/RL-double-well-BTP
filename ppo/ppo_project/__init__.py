from gym.envs.registration import register
register(id='classic-v0',
         entry_point='ppo_project.envs:classic',)
