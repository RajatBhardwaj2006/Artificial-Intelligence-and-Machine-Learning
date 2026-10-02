# 🚀 Reinforcement Learning Journey: From Tabular Methods to Deep Q-Networks (DQN)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📝 Repository Overview
Welcome to my comprehensive Reinforcement Learning (RL) repository! This codebase documents my implementation and hands-on exploration of core RL concepts—starting from foundational Markov Decision Processes (MDPs) and classical tabular algorithms, all the way to deep neural network-based agents solving complex environments using Deep Q-Networks (DQN).

---

## 📚 Syllabus & Topics Covered

This repository is structured into progressive modules reflecting core theoretical and practical milestones:

### **Module 1: Foundations & Tabular RL**
* **Introduction to RL:** Core components of an RL system, agent-environment interaction, and reward structures.
* **Markov Decision Processes (MDPs):** Mathematical formulation of sequential decision-making and grid-world state transitions.
* **Policy Optimization & Q-Functions:** Understanding value functions, policy evaluation, and the exploration-exploitation trade-off ($\epsilon$-greedy strategies).
* **Classical Learning Methods:** 
  * Dynamic Programming
  * Monte Carlo Methods
  * Temporal Difference (TD) Learning

### **Module 2: Tabular Algorithms & Cliff-Walking**
* **SARSA (State-Action-Reward-State-Action):** On-policy TD control implementation.
* **Q-Learning:** Off-policy TD control algorithm.
* **Cliff-Walking Environment:** Training and comparing agent behaviors, path efficiencies, and safety policies learned via SARSA vs. Q-Learning.

### **Module 3: Deep Reinforcement Learning (DQN)**
* **Introduction to Deep RL & DQNs:** Scaling Q-learning to continuous state spaces using neural networks.
* **Experience Replay:** Breaking sample correlations by storing and randomly sampling past transitions.
* **Policy & Target Networks:** Stabilizing training using separate target networks to minimize moving-target instability.
* **Hyperparameter Tuning:** Implementing $\epsilon$-decay schedules, learning rate adjustments, and loss optimization.

### **Module 4: Practical Projects & Environments**
* **Environment Setup:** Interacting with OpenAI Gymnasium / custom game engines.
* **Agent Training & Evaluation:** Training agents to solve physics or arcade tasks (e.g., CartPole balancing / Flappy Bird navigation).

---

## 📂 Repository Structure

```text
├── tabular_methods/
│   ├── mdp_grid/           # Grid world MDP simulations
│   ├── sarsa/              # SARSA implementation and Cliff-Walking script
│   └── q_learning/         # Q-learning implementation and Cliff-Walking script
├── deep_rl/
│   ├── dqn_cartpole/       # DQN agent for CartPole / Gymnasium environments
│   ├── dqn_flappybird/     # DQN agent for Flappy Bird game environment
│   └── utils/              # Experience replay buffer, network architectures
├── models/                 # Saved model weights (.pth)
├── logs/                   # Training metrics and TensorBoard logs
└── requirements.txt        # Project dependencies