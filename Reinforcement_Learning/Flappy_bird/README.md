# Flappy Bird DQN

A Deep Q-Network (DQN) reinforcement learning project that trains an agent to play Flappy Bird using PyTorch, Gymnasium, experience replay, and a target network.

The project automatically uses NVIDIA CUDA when a CUDA-enabled PyTorch installation is available.

## Features

- Deep Q-Network (DQN)
- Experience replay
- Target DQN network
- Epsilon-greedy exploration
- Configurable hyperparameters via `parameter.yaml`
- Automatic CUDA/CPU device selection
- Best-model checkpoint saving
- Training and rendering/testing modes
- Gradient clipping
- Episode reward logging

## Project Structure

```text
Flappy_bird/
├── agent.py
├── dqn.py
├── Experience_replay.py
├── parameter.yaml
├── requirements.txt
└── runs/
    ├── <hyperparameter_set>.pt
    └── <hyperparameter_set>.log
```

## Requirements

- Python 3.12 recommended
- PyTorch
- Gymnasium
- Flappy Bird Gymnasium
- PyYAML
- NumPy
- NVIDIA GPU + compatible NVIDIA driver for CUDA training

## Installation

Clone the repository:

```bash
git clone <https://github.com/RajatBhardwaj2006/Artificial-Intelligence-and-Machine-Learning/tree/96165ea0f596ee5c41d75e8a8f79d5da4ca91378/Reinforcement_Learning/Flappy_bird>
cd Flappy_bird
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

If installing the basic packages manually:

```bash
python -m pip install gymnasium flappy-bird-gymnasium pyyaml numpy
```

### NVIDIA CUDA / RTX Training

Install a CUDA-enabled PyTorch build appropriate for your system. The official PyTorch installer is:

https://pytorch.org/get-started/locally/

For CUDA 12.8, for example:

```bash
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

Verify:

```bash
python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA available:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Not detected')"
```

Expected on a working NVIDIA setup:

```text
CUDA available: True
GPU: NVIDIA GeForce RTX 5050 Laptop GPU
```

The GPU name will depend on your hardware.

## Hyperparameters

Open:

```text
parameter.yaml
```

The configuration contains parameters such as:

```yaml
alpha:
gamma:
epsilon_init:
epsilon_min:
epsslon_dec:
replay_memory_size:
mini_batch_size:
network_sync_rate:
reward_threshold:
```

The command-line argument must match the hyperparameter-set name defined in `parameter.yaml`.

For example, if the YAML contains `flappybirfv0`, run:

```bash
python agent.py flappybirfv0 --train
```

## Train

Run:

```bash
python agent.py flappybirfv0 --train
```

Training runs without rendering to avoid the additional rendering overhead.

The program automatically selects:

```text
CUDA → MPS → CPU
```

When CUDA is available, the terminal will show something similar to:

```text
Using device: cuda
GPU: NVIDIA GeForce RTX 5050 Laptop GPU
```

## Model Checkpoints

The best-performing model is saved to:

```text
runs/flappybirfv0.pt
```

Training information is logged to:

```text
runs/flappybirfv0.log
```

The checkpoint is updated when a new best episode reward is achieved.

## Render the Trained Agent

After a model has been trained:

```bash
python agent.py flappybirfv0
```

Without `--train`, the program loads the saved model and runs the environment with human rendering enabled.

## Training vs Testing

### Training

```bash
python agent.py flappybirfv0 --train
```

- Training enabled
- Rendering disabled
- Replay memory enabled
- Target network enabled
- Best model saved

### Testing / Rendering

```bash
python agent.py flappybirfv0
```

- Training disabled
- Saved model loaded
- Rendering enabled
- Agent plays Flappy Bird

## DQN Training Flow

```text
Environment State
       ↓
   Policy DQN
       ↓
 Q(action 0/1)
       ↓
     Action
       ↓
  Flappy Bird
       ↓
Next State + Reward
       ↓
 Replay Memory
       ↓
Random Mini-batch
       ↓
 DQN Optimization
       ↓
Target Network Sync
```

The project uses a policy network for learning and a target network for producing more stable Q-value targets.

## Experience Replay

Transitions are stored as:

```text
(state, action, next_state, reward, termination)
```

Random mini-batches are sampled from replay memory during training.

This reduces the correlation between consecutive experiences and allows the agent to learn repeatedly from previous experiences.

## Exploration

The agent uses epsilon-greedy exploration.

High epsilon:

```text
More random actions
```

Low epsilon:

```text
More actions chosen by the DQN
```

Epsilon gradually decreases toward `epsilon_min`.

## GPU Notes

The code automatically detects CUDA:

```python
if torch.cuda.is_available():
    device = "cuda"
```

The DQN and tensors are moved to the selected device.

For example:

```python
policy_dqn = DQN(num_state, num_action).to(device)
```

and:

```python
state = torch.tensor(
    state,
    dtype=torch.float32,
    device=device
)
```

The Flappy Bird environment itself performs CPU-side simulation, so GPU utilization may not stay at 100% even when the DQN is using the RTX GPU.

For long training runs, keep the laptop connected to AC power.

## Troubleshooting

### CUDA shows False

Run:

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

If it returns `False`, check that you installed a CUDA-enabled PyTorch build rather than a CPU-only build.

A CPU-only build commonly contains:

```text
+cpu
```

A CUDA build contains a CUDA suffix such as:

```text
+cu128
```

### GPU is not detected

Run:

```bash
nvidia-smi
```

Then:

```bash
python -c "import torch; print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Not detected')"
```

### Model file not found

If:

```bash
python agent.py flappybirfv0
```

cannot find the model, train it first:

```bash
python agent.py flappybirfv0 --train
```

The expected checkpoint is:

```text
runs/flappybirfv0.pt
```

### Gymnasium observation warning

Some versions/configurations of the Flappy Bird environment may report warnings that returned observations are outside the declared observation space. If this occurs, check the installed `flappy_bird_gymnasium` version and inspect the environment observation space before changing the DQN.

## Git Commit

Recommended commit message:

```text
feat: improve Flappy Bird DQN training and CUDA support
```

Or:

```text
Improve DQN training loop and GPU support
```

Git commands:

```bash
git status
git add .
git commit -m "feat: improve Flappy Bird DQN training and CUDA support"
git push
```

## Future Improvements

- Double DQN
- Dueling DQN
- Prioritized experience replay
- Better reward/score tracking
- TensorBoard or Weights & Biases tracking
- Evaluation over multiple episodes
- Automated hyperparameter experiments
- Training-performance graphs
- Separate training and evaluation scripts
