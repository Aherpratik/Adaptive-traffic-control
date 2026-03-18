import pickle
from traffic_env import TrafficEnv

with open("q_table.pkl", "rb") as f:
    q_table = pickle.load(f)

env = TrafficEnv(use_gui=True)

state = env.reset()
done = False

while not done:
    if state in q_table:
        action = q_table[state].index(max(q_table[state]))
    else:
        action = 0  # default action if unseen state appears

    state, _, done = env.step(action)

env.close()
