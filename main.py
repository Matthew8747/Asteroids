from env_utils import make_env
from agents.shooter_agent import ShooterAgent
from agents.random_agent import RandomAgent

def run_episode(agent, render=True):

    env = agent.env
    obs, info = env.reset()

    done = False
    total_reward = 0

    while not done:
        action = agent.act(obs) # The agent now holds the environment
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

        if terminated or truncated:
            done = True

    print("Episode finished. Total reward:", total_reward)

if __name__ == "__main__":
    env = make_env(render_mode="human")
    agent = RandomAgent(env) #choose agent
    run_episode(agent)
    env.close()
