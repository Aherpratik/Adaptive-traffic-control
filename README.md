# 🚦 Adaptive Traffic Signal Control using Reinforcement Learning (SUMO + Q-Learning)

## 📌 Overview

This project implements an **Adaptive Traffic Signal Control System** using **Reinforcement Learning (Q-Learning)** with the **SUMO (Simulation of Urban Mobility)** traffic simulator.

The goal is to dynamically control traffic lights at an intersection to **reduce congestion and improve traffic flow** based on real-time traffic conditions.

---

## 🎯 Problem Statement

Traditional traffic lights operate on fixed timers, which:

* Do not adapt to real-time traffic
* Cause unnecessary waiting
* Lead to congestion and inefficiency

This project solves the problem by using **Reinforcement Learning** to:

* Observe traffic conditions
* Learn optimal signal switching strategies
* Minimize total waiting vehicles

---

## 🧠 Approach

### Environment

* Built using **SUMO (Eclipse SUMO)**
* Intersection with traffic lights (`B1`)
* Vehicles generated via predefined routes

### State Representation

The state is represented as:

```python
(number_of_cars_lane1, lane2, lane3, lane4)
```

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
reward = -total_waiting
```

Where:

* `total_waiting` = total number of halted vehicles

Objective:
👉 Minimize total waiting → maximize traffic flow

---

### Algorithm

* Q-Learning (Tabular RL)
* ε-greedy policy for exploration
* Bellman update rule

---

## ⚙️ Tech Stack

* Python
* SUMO (Simulation of Urban Mobility)
* TraCI (Traffic Control Interface)
* Reinforcement Learning (Q-Learning)

---

## 📁 Project Structure

```
Adaptive-Traffic-Control/
│
├── traffic_env.py       # RL environment using SUMO + TraCI
├── q_learning.py        # Training script
├── run_trained.py       # Run trained model (visualization)
├── configs/             # SUMO config files
├── q_table.pkl          # Saved Q-table (generated after training)
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

* Install SUMO:
  https://www.eclipse.org/sumo/

* Set environment variable:

```bash
export SUMO_HOME=/path/to/sumo
export PATH=$SUMO_HOME/bin:$PATH
```

---

### 2. Train the Model

```bash
python q_learning.py
```

* Runs multiple episodes
* Saves Q-table as `q_table.pkl`

---

### 3. Visualize Trained Agent

```bash
python run_trained.py
```

* Opens SUMO GUI
* Shows learned traffic signal behavior

---

## 📊 Results

* Initial reward: ~ -1200 to -1500
* Best reward achieved: ~ **-764**

✅ Significant reduction in congestion
✅ Improved traffic balancing
✅ Adaptive signal switching behavior

---

## 🚀 Future Improvements

* Add **yellow signal transition** for realistic switching
* Improve reward function (waiting time + imbalance)
* Scale to **multi-intersection networks**
* Upgrade to **Deep Q-Networks (DQN)**
* Real-time dashboard for visualization

---

## 💡 Key Learnings

* Practical implementation of Reinforcement Learning
* Integration of RL with real-world simulation (SUMO)
* Importance of reward design in RL systems
* Handling environment stability and action design

---

## 📌 Conclusion

This project demonstrates how Reinforcement Learning can be applied to real-world systems like traffic control to create **adaptive, efficient, and intelligent infrastructure solutions**.

---

## 🙌 Acknowledgements

* Eclipse SUMO
* Reinforcement Learning concepts from OpenAI Gym-style environments

---

## 📬 Contact

Feel free to connect or reach out for collaboration!
