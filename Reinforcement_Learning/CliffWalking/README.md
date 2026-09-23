# Cliff Walking — SARSA Reinforcement Learning

This folder contains a visual example of the **Cliff Walking problem** using the **SARSA (State-Action-Reward-State-Action)** Reinforcement Learning algorithm.

The agent learns to navigate from the starting position to the goal while avoiding the cliff.

---

## What is Cliff Walking?

Cliff Walking is a classic Reinforcement Learning environment where an agent must learn a safe path through a grid.

The environment contains:

- 🧍 **Agent** — the learner
- 🟩 **Safe states** — normal positions
- 🕳️ **Cliff** — dangerous states with a large negative reward
- 🎯 **Goal** — the destination
- 🏆 **Reward** — feedback received after taking an action

The agent is not given the correct path. It learns through repeated interaction with the environment.

---

## SARSA

**SARSA** is an **on-policy Temporal Difference Reinforcement Learning algorithm**.

The name comes from:

```text
State → Action → Reward → Next State → Next Action

   S       A         R          S'           A'
```

The agent follows this process repeatedly:

```text
Current State
      ↓
 Select Action
      ↓
 Take Action
      ↓
 Receive Reward
      ↓
 Observe Next State
      ↓
 Select Next Action
      ↓
 Update Q-Value
      ↓
    Repeat
```

---

## Learning Progress

The following images show how the agent progresses while learning the environment.

### 1. Start

The agent begins with little knowledge about the environment and starts exploring different actions.

![Cliff Walking - Start](https://raw.githubusercontent.com/RajatBhardwaj2006/Artificial-Intelligence-and-Machine-Learning/main/Reinforcement_Learning/CliffWalking/Start.png)

---

### 2. Midway

After interacting with the environment, the agent begins learning which actions lead to better outcomes.

![Cliff Walking - Midway](https://raw.githubusercontent.com/RajatBhardwaj2006/Artificial-Intelligence-and-Machine-Learning/main/Reinforcement_Learning/CliffWalking/Mid_way.png)

---

### 3. End

After training, the agent has learned a policy for navigating toward the goal while avoiding the cliff.

![Cliff Walking - End](https://raw.githubusercontent.com/RajatBhardwaj2006/Artificial-Intelligence-and-Machine-Learning/main/Reinforcement_Learning/CliffWalking/End.png)

---

## SARSA Update

The SARSA Q-value is updated using:

$$
Q(S,A) \leftarrow Q(S,A) +
\alpha [R + \gamma Q(S',A') - Q(S,A)]
$$

Where:

| Symbol | Meaning |
|---|---|
| `S` | Current state |
| `A` | Current action |
| `R` | Reward received |
| `S'` | Next state |
| `A'` | Next action |
| `α` | Learning rate |
| `γ` | Discount factor |

The important characteristic of SARSA is that it uses the **actual next action selected by the agent** when updating the Q-value.

---

## SARSA vs Q-Learning

| Feature | SARSA | Q-Learning |
|---|---|---|
| Learning type | On-policy | Off-policy |
| Uses next selected action | Yes | No |
| Update target | `R + γQ(S',A')` | `R + γ max Q(S',a)` |
| Policy used for update | Current policy | Greedy target policy |

---

## Key Reinforcement Learning Concepts

This example demonstrates:

- Agent
- Environment
- State
- Action
- Reward
- Policy
- Q-Table
- Temporal Difference Learning
- SARSA
- Exploration
- Exploitation
- Learning Rate
- Discount Factor

---

## Files

```text
CliffWalking/
│
├── README.md
├── Start.png
├── Mid_way.png
└── End.png
```

The images are stored in the same directory as this README and are loaded using GitHub's raw file URLs.

---

## Purpose

This example is part of a collection of Reinforcement Learning examples designed to make machine learning concepts easier to understand through **visual demonstrations and practical implementations**.
