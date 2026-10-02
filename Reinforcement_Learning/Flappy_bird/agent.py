import argparse
import flappy_bird_gymnasium
import gymnasium as gym
import torch
import random as rd
import torch.nn as nn
import torch.optim as optim
from dqn import DQN
from Experience_replay import ReplyMemory
import itertools
import yaml
import os



# DEVICE


if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(f"Using device: {device}")

if device == "cuda":
    print(f"GPU: {torch.cuda.get_device_name(0)}")



# DIRECTORIES


RUNS_DIR = "runs"
os.makedirs(RUNS_DIR, exist_ok=True)



# AGENT


class Agent:

    def __init__(self, parameter_set):

        self.param_set = parameter_set

        with open(
            "X:\\VScode\\Artificial_intelligence_n_Machine_learning\\Reinforcement_Learning\\Flappy_bird\\parameter.yaml","r") as file:

            all_para = yaml.safe_load(file)
            paras = all_para[parameter_set]

        self.alpha = paras["alpha"]
        self.gamma = paras["gamma"]

        self.epsilon_init = paras["epsilon_init"]
        self.epsilon_min = paras["epsilon_min"]
        self.epsslon_dec = paras["epsslon_dec"]

        self.replay_memory_size = paras["replay_memory_size"]
        self.mini_batch_size = paras["mini_batch_size"]

        self.network_sync_rate = paras["network_sync_rate"]

        self.reward_threshold = paras["reward_threshold"]

        self.loss_fn = nn.MSELoss()
        self.optimizer = None

        self.LOG_FILE = os.path.join(RUNS_DIR,f"{self.param_set}.log"        )

        self.MODEL_FILE = os.path.join(RUNS_DIR,f"{self.param_set}.pt")

    
    # RUN
    

    def run(self, is_training=True, render=False):

        env = gym.make(
            "FlappyBird-v0",
            render_mode="human" if render else None
        )

        num_state = env.observation_space.shape[0]
        num_action = env.action_space.n

        print(f"State size: {num_state}")
        print(f"Action size: {num_action}")

        
        # POLICY NETWORK
        

        policy_dqn = DQN(
            num_state,
            num_action
        ).to(device)

        
        # TRAINING SETUP
        

        if is_training:

            memory = ReplyMemory(
                self.replay_memory_size
            )

            epsilon = self.epsilon_init

            target_dqn = DQN(
                num_state,
                num_action
            ).to(device)

            target_dqn.load_state_dict(
                policy_dqn.state_dict()
            )

            target_dqn.eval()

            steps = 0

            self.optimizer = optim.Adam(
                policy_dqn.parameters(),
                lr=self.alpha
            )

            best_reward = float("-inf")

        
        # LOAD TRAINED MODEL
        

        else:

            policy_dqn.load_state_dict(
                torch.load(
                    self.MODEL_FILE,
                    map_location=device
                )
            )

            policy_dqn.eval()

        
        # EPISODES
        

        for episode in itertools.count():

            state, _ = env.reset()

            state = torch.tensor(
                state,
                dtype=torch.float32,
                device=device
            )

            episode_reward = 0.0

            terminated = False

            
            # EPISODE
            

            while not terminated:

                
                # EPSILON GREEDY ACTION
                

                if is_training and rd.random() < epsilon:

                    action = env.action_space.sample()

                    action = torch.tensor(
                        action,
                        dtype=torch.long,
                        device=device
                    )

                else:

                    with torch.no_grad():

                        action = policy_dqn(
                            state.unsqueeze(0)
                        ).squeeze(0).argmax()

                
                # ENVIRONMENT STEP
                

                next_state, reward, terminated, truncated, _ = env.step(
                    action.item()
                )

                # Gymnasium can signal termination using either flag.
                done = terminated or truncated

                reward = torch.tensor(
                    reward,
                    dtype=torch.float32,
                    device=device
                )

                next_state = torch.tensor(
                    next_state,
                    dtype=torch.float32,
                    device=device
                )

                
                # REPLAY MEMORY
                

                if is_training:

                    memory.append(
                        (
                            state,
                            action,
                            next_state,
                            reward,
                            done
                        )
                    )

                    steps += 1

                
                # UPDATE STATE
                

                state = next_state

                episode_reward += reward.item()

                
                # TRAIN FROM REPLAY MEMORY
                

                if (
                    is_training
                    and len(memory) >= self.mini_batch_size
                ):

                    mini_batch = memory.sample(
                        self.mini_batch_size
                    )

                    self.optimize(
                        mini_batch,
                        policy_dqn,
                        target_dqn
                    )

                    
                    # TARGET NETWORK UPDATE
                    

                    if steps >= self.network_sync_rate:

                        target_dqn.load_state_dict(
                            policy_dqn.state_dict()
                        )

                        steps = 0

                terminated = done

            
            # EPSILON DECAY
            

            if is_training:

                epsilon = max(
                    epsilon * self.epsslon_dec,
                    self.epsilon_min
                )

            
            # PRINT
            

            print(
                f"Episode: {episode + 1} | "
                f"Reward: {episode_reward:.2f} | "
                f"Epsilon: {epsilon:.4f}"
                if is_training
                else
                f"Episode: {episode + 1} | "
                f"Reward: {episode_reward:.2f}"
            )

            
            # SAVE BEST MODEL
            

            if is_training and episode_reward > best_reward:

                best_reward = episode_reward

                log_msg = (
                    f"Best Reward: {episode_reward:.2f} "
                    f"for episode = {episode + 1}"
                )

                with open(
                    self.LOG_FILE,
                    "a"
                ) as file:

                    file.write(
                        log_msg + "\n"
                    )

                torch.save(
                    policy_dqn.state_dict(),
                    self.MODEL_FILE
                )

                print(
                    f"New best model saved! "
                    f"Reward: {best_reward:.2f}"
                )

        env.close()

    
    # OPTIMIZATION
    

    def optimize(
        self,
        mini_batch,
        policy_dqn,
        target_dqn
    ):

        states, actions, next_states, rewards, terminations = zip(
            *mini_batch
        )

        states = torch.stack(states)

        actions = torch.stack(actions)

        next_states = torch.stack(next_states)

        rewards = torch.stack(rewards)

        terminations = torch.tensor(
            terminations,
            dtype=torch.float32,
            device=device
        )

        
        # TARGET Q VALUE
        

        with torch.no_grad():

            next_q_values = target_dqn(
                next_states
            ).max(
                dim=1
            ).values

            target_q = rewards + (
                1 - terminations
            ) * self.gamma * next_q_values

        
        # CURRENT Q VALUE
        

        current_q = policy_dqn(
            states
        ).gather(
            dim=1,
            index=actions.unsqueeze(1)
        ).squeeze(1)

        
        # LOSS
        

        loss = self.loss_fn(
            current_q,
            target_q
        )

        
        # BACKPROPAGATION
        

        self.optimizer.zero_grad()

        loss.backward()

        # Prevent excessively large gradients
        torch.nn.utils.clip_grad_norm_(
            policy_dqn.parameters(),
            max_norm=10.0
        )

        self.optimizer.step()



# MAIN


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Train or test model."
    )

    parser.add_argument(
        "hyperparameters",
        help="Hyperparameter set name from parameter.yaml"
    )

    parser.add_argument(
        "--train",
        help="Training mode",
        action="store_true"
    )

    args = parser.parse_args()

    dql = Agent(
        parameter_set=args.hyperparameters
    )

    if args.train:

        dql.run(
            is_training=True,
            render=False
        )

    else:

        dql.run(
            is_training=False,
            render=True
        )