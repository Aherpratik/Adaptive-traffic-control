# 🚦 Adaptive Traffic Signal Control using Reinforcement Learning (SUMO with Q-Learning and DQN)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![RL](https://img.shields.io/badge/Reinforcement%20Learning-Q%20Learning%20%7C%20DQN-green)
![SUMO](https://img.shields.io/badge/Simulator-SUMO-orange)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-red)


##  Overview

This project implements an **Adaptive Traffic Signal Control System** using **Reinforcement Learning**, progressing from **Q-Learning (baseline)** to **Deep Q-Network (DQN)** with the **SUMO (Simulation of Urban Mobility)** traffic simulator.

The system learns to dynamically control traffic lights based on real-time traffic conditions to **minimize congestion and optimize traffic flow**.

---

Achieved ~75% improvement in traffic efficiency (from -764 to -185 reward)

##  Problem Statement

Traditional traffic lights operate on fixed timers, which:

* Do not adapt to real-time traffic
* Cause unnecessary waiting
* Lead to congestion and inefficiency

This project solves the problem by using **Reinforcement Learning** to:

* Observe traffic conditions
* Learn optimal signal switching strategies
* Minimize total waiting vehicles

---

---

##  Evolution of Approach

This project was developed in two stages:

### 1. Q-Learning (Tabular RL)
- Discrete state representation
- Limited scalability
- Initial performance improvements

### 2. Deep Q-Network (DQN)
- Neural network-based Q-function approximation
- Experience replay buffer
- Target network stabilization
- Improved learning efficiency and generalization

Transitioning to DQN significantly improved performance and scalability of the system.

### Environment

* Built using **SUMO (Eclipse SUMO)**
* Intersection with traffic lights (`B1`)
* Vehicles generated via predefined routes

### State Representation

The state is represented as:

```python
(direction1_bucket, direction2_bucket, time_bucket)

```
- Traffic is aggregated into two directions
- Bucketed representation reduces state space
- Time awareness improves learning stability


This captures real-time queue length at each lane.

---

### Actions

The agent can choose between:

* `0` → Green phase for direction 1
* `1` → Green phase for direction 2

Internally mapped to SUMO phases:

```python
[0, 2]
```

---

### Reward Function

```python
reward = -(total_waiting) - 0.5 * imbalance - switch_penalty
```

Where:
- `total_waiting` → total halted vehicles
- `imbalance` → difference between directions
- `switch_penalty` → penalty for frequent signal switching

Encourages:
- lower congestion
- balanced traffic flow
- stable signal switching

---

### Algorithm

* Q-Learning (Tabular RL)
* DQN
* ε-greedy policy for exploration
* Bellman update rule

---

##  Tech Stack

* Python
* SUMO (Simulation of Urban Mobility)
* TraCI (Traffic Control Interface)
* Reinforcement Learning (Q-Learning, DQN)
* PyTorch (for Deep Q-Network)

---

##  Project Structure

```
Adaptive-Traffic-Control/
│
├── env/
│ └── traffic_env.py # SUMO + TraCI environment
│
├── q_learning/
│ ├── q_learning.py
│ ├── run_trained.py
│ └── q_table.pkl
│
├── dqn/
│ ├── dqn_agent.py
│ ├── replay_buffer.py
│ ├── dqn_train.py
│ ├── run_trained_dqn.py
│ └── run_best_model.py
│
├── scripts/
│ ├── test_env.py
│ ├── run_simulation.py
│ └── check_phases.py
│
├── configs/
├── networks/
├── routes/
│
├── results/
│ ├── models/
│ └── recordings/
│
├── requirements.txt
└── README.md
```

---

##  How to Run

### 1. Install Dependencies

* Install Python dependencies:
  pip install -r requirements.txt

* Install SUMO:
  https://www.eclipse.org/sumo/

* Set environment variable:

```bash
export SUMO_HOME=/path/to/sumo
export PATH=$SUMO_HOME/bin:$PATH
```

---

### 2. Train the Model

### Train Q-Learning

```bash
python q_learning/q_learning.py


```

* Runs multiple episodes
* Saves Q-table as `q_table.pkl`

### Train DQN

```bash
python dqn/dqn_train.py
```

### Run Models

* Run trained Q-Learning
```bash
python q_learning/run_trained.py
```

* Run trained DQN
```bash
python dqn/run_trained_dqn.py
```

* Run best DQN model
```bash
python dqn/run_best_model.py
```


---

### 3. Visualize Trained Agent

```bash
python run_trained.py
```

* Opens SUMO GUI
* Shows learned traffic signal behavior

---

## Results

### Q-Learning
- Initial reward: ~ -1500
- Best reward: ~ **-764**

### DQN
- Improved reward: ~ **-185 (best)**  
- Stable range: ~ -185 to -250

✅ Significant reduction in congestion  
✅ Better traffic balancing  
✅ More stable signal switching  

---

## Future Improvements

* Add **yellow signal transition** for realistic switching
* Improve reward function (waiting time + imbalance)
* Extend to **multi-intersection traffic** systems
* Implement PPO / Actor-Critic methods
* Real-time dashboard for visualization

---

## Key Learnings

* Practical implementation of Reinforcement Learning
* Integration of RL with real-world simulation (SUMO)
* Importance of reward design in RL systems
* Handling environment stability and action design

---
## Key Engineering Contributions

- Designed modular RL architecture separating environment, Q-learning, and DQN components
- Implemented experience replay and target network for stable DQN training
- Optimized reward function for traffic balancing and reduced oscillations
- Improved performance from -764 (Q-learning) to ~ -185 (DQN)

## Conclusion

This project demonstrates how Reinforcement Learning can be applied to real-world systems like traffic control to create **adaptive, efficient, and intelligent infrastructure solutions**.

---

##  Acknowledgements

* Eclipse SUMO
* Reinforcement Learning concepts from OpenAI Gym-style environments

---

##  Contact

Feel free to connect or reach out for collaboration!
