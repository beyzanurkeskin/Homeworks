

from collections import namedtuple
import time
import numpy as np
from game_q_learning import CarGameQL
from macros import *


# Are we rendering or not
RENDER_TRAIN = False


"""
    Parameters related to training process and Q-Learning
"""

# Number of episodes to train
NUM_EPISODES = 1000

# epsilon parameter of e-greedy policy
EPSILON = 0.1

# learning rate parameter of q learning
LEARNING_RATE = 0.3

# discount rate parameter of q learning
DISCOUNT_RATE = 0.9

# The step limit per episode, since we do not want infinite loops inside episodes
MAX_STEPS_PER_EPISODE = 200

"""
    Parameters end
"""

# Here, we are creating the environment with our predefined observation space
env = CarGameQL(render=RENDER_TRAIN)

# Observation and action space
obs_space = env.observation_space
number_of_states = env.observation_space.shape[0]

action_space = env.action_space
number_of_actions = env.action_space.n
print("The observation space: {}".format(obs_space))
# Output: The observation space: Box(n,)
print("The action space: {}".format(action_space))
# Output: The action space: Discrete(m)



# I did not understand what to do in the gamecarql class, and when I made a change in it, 
# it constantly gave me an error. (For example, it said there is no seed function, 
# it said there is no init function. I tried to fix it, but I didn't, so I didn't make any changes.) In addition, I got the following error;


#   File "c:\Users\Beyza\Desktop\game_env\game.py", line 156, in step
#     raise ValueError("Action must be an integer from [0, 1, 2] or a string from [R, L, P]!")
# ValueError: Action must be an integer from [0, 1, 2] or a string from [R, L, P]!


# but there was an output that looked nice before. Since there is no sample output, 
# I don't understand where is my mistake. I tried changing the outputs of the choose_action_greedy 
# and choose_action_e_greedy functions, but I guess they weren't the problem because it wasn't solved.
# Maybe If I could change something in test_agent, it would be fixed but I didn't try it because it is forbidden.





q_table = {}

def choose_action_greedy(state, q_table):                                   # choose the action with the highest Q value for the given state
   
    action = np.argmax(q_table[state])
    return action


def choose_action_e_greedy(state, q_table, epsilon):

    if np.random.random() < epsilon:                                        # choose a random action
        return np.random.choice(number_of_actions)
    
    else:                                                                   # choose the greedy action based on Q values
        return choose_action_greedy(state, q_table)                         # comment line explaining the function call




def main():
    
    q_table = np.zeros((number_of_states, number_of_actions))

    # Loop for each episode
    for e in range(NUM_EPISODES):
        # Initialize S
        s0 = env.reset()

        # Loop for each step of the episode
        episode_steps = 0
        while episode_steps < MAX_STEPS_PER_EPISODE:
            # Choose A from S using policy derived from Q (e.g., epsilon-greedy)
            action = choose_action_e_greedy(s0, q_table, EPSILON)

            # Take action A, observe R, S'
            s1, reward, done, info = env.step(action)

            # Q(S, A) <- Q(S, A) + alpha * [R + gamma * max(Q(S', a)) - Q(S, A)]
            q_table[s0][action] += LEARNING_RATE * (
                    reward + DISCOUNT_RATE * np.max(q_table[s1]) - q_table[s0][action])

            # S <- S'
            s0 = s1

            # Until S is terminal
            if done:
                break

            episode_steps += 1

        # print the number of episodes completed
        if e % 100 == 0:
            print("episode {} completed".format(e))

    # test our trained agent
    test_agent(q_table)


def test_agent(q_table):
    print("Initializing test environment:")
    test_env = CarGameQL(render=True, human_player=False)
    state = env.reset()
    steps = 0
    #while (steps < 200):
    while (True):
        action = choose_action_greedy(state, q_table)
        print("chosen action:", action)
        next_state, reward, done, info = test_env.step(convert_direction_to_action(action))
        print("state:", state, " , next_state:", next_state)
        test_env.render()
        if done:
            break
        else:
            state = next_state
        steps += 1
        print("test current step:",steps)
        
        time.sleep(0.1)


if __name__ == '__main__':
    main()


