import gymnasium as gym
import ale_py

def make_env(render_mode=None, seed=0):
    gym.register_envs(ale_py)
    env = gym.make(
        "ALE/Asteroids-v5",
        render_mode=render_mode,
    )
    obs, info = env.reset(seed=seed)
    return env
