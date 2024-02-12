import numpy as np

from game import *


class CarGameQL(CarGame):

    def __init__(self, render=True, human_player=False):
        super(CarGameQL, self).__init__(render, human_player)
        
        """
        DEFINE YOUR OBSERVATION SPACE DIMENSIONS HERE FOR EACH MODE.
        JUST CHANGING THE "obs_space_dim" VARIABLE SHOULD BE ENOUGH
        
            Try making your returned state from get_state function
        a 1-D array if its not, it will make things simpler for you
        
            For the first Q-Learning part, you must use a more compact
        game state than raw game array
        """
        obs_space_dim = 30
        self.observation_space = spaces.Box(0, obs_space_dim, shape=(obs_space_dim,))
        
       

    def get_state(self):
                                                           
        game_state = self.game_state                                # access the 6x5 grid array
        car_position = None                                         # define the state representation variables
        obstacles = []

        
        for row in range(len(game_state)):                          # iterate over the game state and extract relevant information
            for col in range(len(game_state[row])):

                cell = game_state[row][col]

                if cell == 'C':                                     # c represents the car position
                    car_position = (row, col)

                elif cell == 'O':                                   # o represents obstacles
                    obstacles.append((row, col))

        
        state = [0] * 30                                            # create a simplified state representation as a 1D array

        if car_position is not None:
            state[car_position[0] * 5 + car_position[1]] = 1        # set the car position index to 1

        for obstacle in obstacles:
            state[obstacle[0] * 5 + obstacle[1]] = 2                # set the obstacle position index to 2

        return state


    def get_reward(self):

        if self.IsCrashed():                                        # check if the agent has crashed
            reward = -1                                             # negative reward for crashing

        else:
            reward = 1                                              # positive reward for surviving

        return reward
    





