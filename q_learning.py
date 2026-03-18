from traffic_env import TrafficEnv
import random
import pickle

env = TrafficEnv()
Q = {}
actions = [0, 1]

episodes = 200
alpha = 0.1
gamma = 0.9

epsilon = 0.3
epsilon_decay = 0.995
epsilon_min = 0.05

best_reward = float("-inf")

for episode in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        if state not in Q:
            Q[state] = [0, 0]

        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = Q[state].index(max(Q[state]))

        next_state, reward, done = env.step(action)

        if next_state not in Q:
            Q[next_state] = [0, 0]

        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * max(Q[next_state]) - Q[state][action]
        )

        state = next_state
        total_reward += reward

    env.close()

    best_reward = max(best_reward, total_reward)
    epsilon = max(epsilon_min, epsilon * epsilon_decay)

    print(
        f"Episode {episode}: Total Reward = {total_reward}, "
        f"Best Reward = {best_reward}, Epsilon = {epsilon:.3f}"
    )

    # save checkpoint every 10 episodes
    if episode % 10 == 0:
        with open("q_table.pkl", "wb") as f:
            pickle.dump(Q, f)
        print(f"Checkpoint saved at episode {episode}")

with open("q_table.pkl", "wb") as f:
    pickle.dump(Q, f)

print("Final Q-table saved successfully.")
