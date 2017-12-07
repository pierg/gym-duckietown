from gym.envs.registration import register

register(
    id='DuckietownGrid-v0',
    entry_point='gym_duckietown.envs:DuckietownGrid',
    max_episode_steps=10000,
)