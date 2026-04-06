import torch
import numpy as np
from traffic_env import TrafficEnv
from dqn_agent import DQN

state_size = 3
action_size = 2

model = DQN(state_size, action_size)
model.load_state_dict(torch.load("dqn_model_best.pth"))
model.eval()

env = TrafficEnv(use_gui=True)

state = env.reset()
state = np.array(state, dtype=np.float32)
done = False

total_reward = 0
step_num = 0
while not done:
    state_tensor = torch.FloatTensor(state).unsqueeze(0)

    with torch.no_grad():
        q_values = model(state_tensor)

    action = q_values.argmax().item()

    next_state, reward, done = env.step(action)

    state = np.array(next_state, dtype=np.float32)

    total_reward = total_reward + reward
    step_num += 1

    print(
        f"Step {step_num} | Action: {action} | Reward: {reward} | Total Reward: {total_reward}"
    )

print(f"The best Episode reward: {total_reward}")
env.close()
