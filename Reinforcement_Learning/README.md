# Reinforcement Learning: From Tabular Foundations to Deep Q-Networks (DQN)

A comprehensive reinforcement learning laboratory implementing Markov Decision Processes (MDPs), classical tabular methods (SARSA, Q-Learning), grid-world simulations (CliffWalking), and deep neural network agents (Deep Q-Networks for Flappy Bird) with PyTorch and CUDA acceleration.

---

## 📌 Overview

Reinforcement Learning (RL) focuses on agents learning optimal behaviors through trial-and-error interactions with dynamic environments:
- **Foundations & MDPs:** States ($S$), Actions ($A$), Transition Probabilities ($P$), Rewards ($R$), and Discount Factors ($\gamma$).
- **Tabular Methods:**
  - **SARSA (On-Policy TD Control):** Updates Q-values using the action actually selected by the current $\epsilon$-greedy policy.
  - **Q-Learning (Off-Policy TD Control):** Updates Q-values using the greedy optimal next action ($\max_{a'} Q(s', a')$).
- **Environment Case Studies:**
  - **Cliff Walking:** Navigating treacherous grid-world states, comparing the conservative path found by SARSA vs. the high-risk optimal path found by Q-Learning.
  - **Flappy Bird DQN:** High-dimensional arcade control using Deep Q-Networks, Experience Replay, Target Networks, and CUDA support.

---

## 📁 Repository Structure & Modules

```
Reinforcement_Learning/
├── CliffWalking/             # Grid-world Cliff Walking environment & visualizations
│   ├── Start.png             # Initial state visualization
│   ├── Mid_way.png           # Mid-training policy convergence
│   ├── End.png               # Optimal path execution
│   └── README.md             # Detailed CliffWalking guide
├── Flappy_bird/              # Deep Q-Network implementation for Flappy Bird
│   ├── agent.py              # Training loop, evaluation, and PyTorch CUDA pipeline
│   ├── dqn.py                # Deep Q-Network multi-layer perceptron architecture
│   ├── Experience_replay.py  # Deque-based transition buffer
│   ├── parameter.yaml        # Hyperparameters (lr, gamma, batch_size, epsilon)
│   └── README.md             # Complete DQN engineering guide
├── Q_Learning.ipynb          # Off-policy Q-Learning tabular implementation
├── SARSA.ipynb               # On-policy SARSA tabular implementation
└── README.md                 # Module documentation
```

---

## 🧠 Algorithmic Breakdown & Comparison

### 1. Tabular Q-Learning vs. SARSA

| Property | SARSA ([`SARSA.ipynb`](SARSA.ipynb)) | Q-Learning ([`Q_Learning.ipynb`](Q_Learning.ipynb)) |
|---|---|---|
| **Paradigm** | On-Policy Temporal Difference | Off-Policy Temporal Difference |
| **Update Rule** | $Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma Q(s', a') - Q(s, a)]$ | $Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$ |
| **Behavior in Cliff Walking** | Learns safe, conservative path far from the cliff edge. | Learns optimal, shortest path along the dangerous edge. |
| **Exploration Sensitivity** | Penalized heavily during training if exploration steps fall into cliff. | Evaluates optimal path independent of exploratory steps taken. |

---

### 2. Deep Q-Networks (DQN)

To overcome tabular scaling limits in large or continuous state spaces, Deep Q-Networks approximate value functions using deep neural networks ($Q(s, a; \theta)$):
- **Experience Replay Buffer:** Stores past transitions $(s, a, r, s', done)$ in a cyclic buffer, sampling random mini-batches to break temporal autocorrelation.
- **Target Network Synchronization:** Uses a slowly updated frozen target network ($Q(s', a'; \theta^-)$) to prevent moving-target oscillations during gradient descent.
- **$\epsilon$-Greedy Decay:** Transitions smoothly from high initial exploration ($\epsilon = 1.0$) down to exploitation ($\epsilon = 0.05$).

---

## 🛠️ Prerequisites & Installation

Install dependencies for tabular and deep reinforcement learning:

```bash
pip install numpy matplotlib jupyter torch gymnasium pyyaml flappy-bird-gymnasium
```

---

## 🚀 How to Run the Experiments

### 1. Tabular Learning Notebooks
Launch Jupyter to train SARSA and Q-Learning agents:
```bash
jupyter notebook Reinforcement_Learning/
```
- Open [`SARSA.ipynb`](SARSA.ipynb) to inspect on-policy state-action trajectories.
- Open [`Q_Learning.ipynb`](Q_Learning.ipynb) to inspect off-policy convergence.

### 2. Flappy Bird DQN Training
Train the deep neural agent with automated CUDA acceleration:
```bash
cd Reinforcement_Learning/Flappy_bird
python agent.py --train
```

To evaluate and render the trained agent:
```bash
python agent.py --test
```
