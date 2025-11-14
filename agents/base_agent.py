from abc import ABC, abstractmethod
import gymnasium as gym

class Agent(ABC):
    def __init__(self, env: gym.Env):
        """Initializes the agent with the environment."""
        self.env = env
        self.action_space = env.action_space
        self.observation_space = env.observation_space

    @abstractmethod
    def act(self, obs):
        """Return an action given an observation."""
        pass

    def reset(self):
        pass
