import torch
import numpy as np
from traffic_env import TrafficEnv
from dqn_agent import DQN

state_size = 3
action_size = 2

model = DQN(state_size, action_size)
model.load_state_dict(torch.load("dqn_model.pth"))
model.eval()

env = TrafficEnv(use_gui=True)

state = env.reset()
state = np.array(state)

done = False

while not done:
    state_tensor = torch.FloatTensor(state).unsqueeze(0)
    action = model(state_tensor).argmax().item()

    state, _, done = env.step(action)
    state = np.array(state)

env.close()
