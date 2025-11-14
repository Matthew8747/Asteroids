from .base_agent import Agent
import gymnasium as gym

class RandomAgent(Agent):
    def __init__(self, env: gym.Env):
        super().__init__(env)

    def act(self, obs):
        return self.action_space.sample()
