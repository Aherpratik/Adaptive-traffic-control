import torch
import numpy as np
from traffic_env import TrafficEnv
from dqn_agent import DQN

state_size = 4
action_size = 2

model = DQN(state_size, action_size)
model.load_state_dict(torch.load("dqn_model_best.pth"))
model.eval()

env = TrafficEnv(use_gui=True)

state = env.reset()
state = np.array(state, dtype=np.float32) / 20.0

done = False

while not done:
    state_tensor = torch.FloatTensor(state).unsqueeze(0)
    action = model(state_tensor).argmax().item()

    next_state, _, done = env.step(action)
    state = np.array(next_state, dtype=np.float32) / 20.0

env.close()
