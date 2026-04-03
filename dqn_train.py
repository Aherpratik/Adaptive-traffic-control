import torch
from traffic_env import TrafficEnv
from dqn_agent import DQNAgent
from replay_buffer import ReplayBuffer
import numpy as np

env = TrafficEnv()

state_size = 3  # IMPORTANT: match your state size
action_size = 2

agent = DQNAgent(state_size, action_size)
buffer = ReplayBuffer(10000)

episodes = 200
batch_size = 32

for episode in range(episodes):
    state = env.reset()
    state = np.array(state)

    done = False
    total_reward = 0

    while not done:
        action = agent.act(state)

        next_state, reward, done = env.step(action)
        next_state = np.array(next_state)

        buffer.push(state, action, reward, next_state, done)

        state = next_state
        total_reward += reward

        if len(buffer) > batch_size:
            batch = buffer.sample(batch_size)
            agent.train(batch, buffer)

    agent.update_target()

    print(f"Episode {episode}, Reward: {total_reward}")

env.close()

torch.save(agent.model.state_dict(), "dqn_model.pth")
