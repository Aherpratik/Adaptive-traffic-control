from traffic_env import TrafficEnv
import random

env = TrafficEnv()
state = env.reset()
done = False

while not done:
    action = random.randint(0, 3)
    state, reward, done = env.step(action)

    print(f"State: {state}, Reward:{reward}")

env.close()
