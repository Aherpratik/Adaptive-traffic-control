import torch
from traffic_env import TrafficEnv
from dqn_agent import DQNAgent
from replay_buffer import ReplayBuffer
import numpy as np

env = TrafficEnv()

state_size = 3
action_size = 2

agent = DQNAgent(state_size, action_size)
buffer = ReplayBuffer(10000)

episodes = 400
batch_size = 32

best_reward = float("-inf")
rewards_history = []

for episode in range(episodes):
    state = env.reset()
    state = np.array(state, dtype=np.float32)

    done = False
    total_reward = 0

    while not done:
        action = agent.act(state)

        next_state, reward, done = env.step(action)
        next_state = np.array(next_state, dtype=np.float32)

        buffer.push(state, action, reward, next_state, done)

        state = next_state
        total_reward += reward

        if len(buffer) > batch_size:
            batch = buffer.sample(batch_size)
            agent.train(batch)

    if episode % 10 == 0:
        agent.update_target()

    rewards_history.append(total_reward)
    avg10 = sum(rewards_history[-10:]) / len(rewards_history[-10:])

    if total_reward > best_reward:
        best_reward = total_reward
        torch.save(agent.model.state_dict(), "dqn_model_best.pth")

    print(
        f"Episode {episode + 1:3d} | "
        f"Reward: {int(total_reward)} | "
        f"Best: {int(best_reward)} | "
        f"Average Reward of 10 ep: {avg10}"
    )

env.close()

torch.save(agent.model.state_dict(), "dqn_model.pth")
print("DQN model saved successfully.")
