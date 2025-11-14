from .base_agent import Agent
import gymnasium as gym


class ShooterAgent(Agent):
  def __init__(self, env: gym.Env):
        super().__init__(env)
        self.FIRE = 1  # Atari fire action

  def act(self, obs):
        return self.FIRE
