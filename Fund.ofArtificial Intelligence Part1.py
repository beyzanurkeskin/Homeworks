import copy
import random
from agent.agent import Agent


class Node():
    def __init__(self, parent, val, pos, map, bunnyMoves, hunterMoves):
        self.parent = parent  # Parent Node
        self.val = val  # Terminal Value (1, -1, 0)
        self.pos = pos  # Position of the bunny
        self.map = map  # Map of the game
        self.bunnyMoves = bunnyMoves  # List of bunny moves
        self.hunterMoves = hunterMoves  # List of hunter moves


class ReflexAgent(Agent):

    def __init__(self, game):

        super().__init__(game)
        self.node = Node(None, 0, [self.bunny[0] + 1, self.bunny[1] + 1], copy.deepcopy(self.map), [],
                         [])  # Initial Node
        self.reflex = self.reflexPlayer(self.map, self.node)  # Starts the reflex agent
        self.val = self.reflex[0]  # Terminal Value (1, -1, 0)
        self.bunnyMoves = self.reflex[1]  # List of bunny moves
        self.hunterMoves = self.reflex[2]  # List of hunter moves

    # i changed the if else's places for a cleaner look (didn't affect the code)
    def reflexPlayer(self, map, node):

        while True:
            rnd = random.randint(0, 3)
            new_pos = [node.pos[0] + self.moves[rnd][0], node.pos[1] + self.moves[rnd][1]]
            if map[new_pos[0]][new_pos[1]] == 0:
                new_node = Node(node, 0, new_pos, copy.deepcopy(map), copy.deepcopy(node.bunnyMoves),
                                copy.deepcopy(node.hunterMoves))
                new_node.map[new_pos[0]][new_pos[1]] = 3
                new_node.map[node.pos[0]][node.pos[1]] = 0
                new_node.bunnyMoves.append(rnd)
                self.number_of_nodes_generated += 1

                return self.reflexOpponent(new_node.map, new_node)
            elif self.checkTerminal(map, node.pos):
                node.val = self.returnScore(map, node.pos)
                return node.val, node.bunnyMoves, node.hunterMoves

    def reflexOpponent(self, map, node):
        """
            DO NOT CHANGE THIS FUNCTION
        """
        if self.checkTerminal(map, node.pos):
            node.val = self.returnScore(map, node.pos)
            return node.val, node.bunnyMoves, node.hunterMoves

        empty = self.emptySpace(map)
        rnd = random.randint(0, len(empty) - 1)

        new_node = Node(node, 0, node.pos, copy.deepcopy(map), copy.deepcopy(node.bunnyMoves),
                        copy.deepcopy(node.hunterMoves))
        new_node.map[empty[rnd][0]][empty[rnd][1]] = 2
        new_node.hunterMoves.append([empty[rnd][0], empty[rnd][1]])
        self.number_of_nodes_generated += 1

        return self.reflexPlayer(new_node.map, new_node)


class MinimaxAgent(Agent):
    def __init__(self, game):
        super().__init__(game)
        self.node = Node(None, 0, [self.bunny[0] + 1, self.bunny[1] + 1], copy.deepcopy(self.map), [],
                         [])  # Initial Node
        self.minimax = self.maxVal(self.map, 50, self.node)  # Start the Minimax algorithm
        self.val = self.minimax[0]  # Terminal Value (1, -1, 0)
        self.bunnyMoves = self.minimax[1]  # List of bunny moves
        self.hunterMoves = self.minimax[2]  # List of hunter moves

    def maxVal(self, map, depth, node):

        # Inside the maxVal method, it checks each move from the current position. If the move is valid,
        #                        a new node is created and the move is added to the rabbit's move list.
        #                                            The minVal method is then called on this new node.
        v = float('-inf')

        best_bunnyMoves = []
        best_hunterMoves = []

        if self.checkTerminal(map, node.pos) or depth == 0:
            # If the terminal status check is done or reaches the maximum depth, the value of the node,
            #                the movements of the rabbit and the movements of the hunter are returned.

            node.val = self.returnScore(map, node.pos)
            return node.val, node.bunnyMoves, node.hunterMoves

        for i in range(len(self.moves)):
            new_pos = [node.pos[0] + self.moves[i][0], node.pos[1] + self.moves[i][1]]
            if map[new_pos[0]][new_pos[1]] == 0:
                new_node = Node(node, 0, new_pos, copy.deepcopy(map), copy.deepcopy(node.bunnyMoves),
                                copy.deepcopy(node.hunterMoves))
                new_node.map[new_pos[0]][new_pos[1]] = 3
                new_node.map[node.pos[0]][node.pos[1]] = 0
                new_node.bunnyMoves.append(i)
                self.number_of_nodes_generated += 1

                child_val, child_bunnyMoves, child_hunterMoves = self.minVal(new_node.map, depth - 1, new_node)

                if child_val > v:
                    v = child_val
                    best_bunnyMoves = new_node.bunnyMoves
                    best_hunterMoves = new_node.hunterMoves

        return v, best_bunnyMoves, best_hunterMoves

    def minVal(self, map, depth, node):
        # The minVal method is part of the Minimax algorithm for calculating the minimum value.
        # If a terminal status check is performed or the maximum depth is reached, the value of the node,
        #                       the movements of the rabbit and the movements of the hunter are returned.

        v = float('inf')

        best_bunnyMoves = []
        best_hunterMoves = []

        if self.checkTerminal(map, node.pos) or depth == 0:
            # If the terminal status check is done or reaches the maximum depth, the value of the node,
            #                the movements of the rabbit and the movements of the hunter are returned.

            node.val = self.returnScore(map, node.pos)
            return node.val, node.bunnyMoves, node.hunterMoves

        empty = self.emptySpace(map)

        for i in range(len(empty)):
            new_node = Node(node, 0, node.pos, copy.deepcopy(map), copy.deepcopy(node.bunnyMoves),
                            copy.deepcopy(node.hunterMoves))
            new_node.map[empty[i][0]][empty[i][1]] = 2
            new_node.hunterMoves.append([empty[i][0], empty[i][1]])
            self.number_of_nodes_generated += 1

            child_val, child_bunnyMoves, child_hunterMoves = self.maxVal(new_node.map, depth - 1, new_node)

            if child_val < v:
                v = child_val
                best_bunnyMoves = new_node.bunnyMoves
                best_hunterMoves = new_node.hunterMoves

        return v, best_bunnyMoves, best_hunterMoves


# As a result, the best rabbit movements and hunter movements calculated by
# the maxVal and minVal methods are returned. These moves can be used later in the game.


class AlphaBetaAgent(Agent):

    def __init__(self, game):

        super().__init__(game)
        self.node = Node(None, 0, [self.bunny[0] + 1, self.bunny[1] + 1], copy.deepcopy(self.map), [],
                         [])  # Initial Node
        self.alphabeta = self.maxVal(self.map, 50, self.node, float('-inf'),
                                     float('inf'))  # Starts the alpha-beta agent
        self.val = self.alphabeta[0]  # Terminal Value (1, -1, 0)
        self.bunnyMoves = self.alphabeta[1]  # List of bunny moves
        self.hunterMoves = self.alphabeta[2]  # List of hunter moves

    def maxVal(self, map, depth, node, alpha, beta):

        # Variables v, best_bunnyMoves, and best_hunterMoves are initialized to
        # keep track of the best value and corresponding moves found so far.
        v = float('-inf')

        best_bunnyMoves = []
        best_hunterMoves = []

        # If the current node is a terminal node or the maximum depth is reached,
        # the function calculates and returns the terminal value, bunny moves, and hunter moves.
        if self.checkTerminal(map, node.pos) or depth == 0:
            node.val = self.returnScore(map, node.pos)
            return node.val, node.bunnyMoves, node.hunterMoves

        # The function iterates over possible moves for the bunny.
        for i in range(len(self.moves)):

            new_pos = [node.pos[0] + self.moves[i][0], node.pos[1] + self.moves[i][1]]

            if map[new_pos[0]][new_pos[1]] == 0:
                new_node = Node(node, 0, new_pos, copy.deepcopy(map), copy.deepcopy(node.bunnyMoves),
                                copy.deepcopy(node.hunterMoves))
                new_node.map[new_pos[0]][new_pos[1]] = 3
                new_node.map[node.pos[0]][node.pos[1]] = 0
                new_node.bunnyMoves.append(i)
                self.number_of_nodes_generated += 1

                child_val, child_bunnyMoves, child_hunterMoves = self.minVal(new_node.map, depth - 1, new_node, alpha,
                                                                             beta)

                if child_val > v:
                    v = child_val
                    best_bunnyMoves = new_node.bunnyMoves
                    best_hunterMoves = new_node.hunterMoves

                alpha = max(alpha, v)
                if alpha >= beta:
                    break

        return v, best_bunnyMoves, best_hunterMoves

    def minVal(self, map, depth, node, alpha, beta):

        v = float('inf')

        best_bunnyMoves = []
        best_hunterMoves = []

        if self.checkTerminal(map, node.pos) or depth == 0:
            node.val = self.returnScore(map, node.pos)
            return node.val, node.bunnyMoves, node.hunterMoves

        empty = self.emptySpace(map)

        for i in range(len(empty)):
            new_node = Node(node, 0, node.pos, copy.deepcopy(map), copy.deepcopy(node.bunnyMoves),
                            copy.deepcopy(node.hunterMoves))
            new_node.map[empty[i][0]][empty[i][1]] = 2
            new_node.hunterMoves.append([empty[i][0], empty[i][1]])
            self.number_of_nodes_generated += 1

            child_val, child_bunnyMoves, child_hunterMoves = self.maxVal(new_node.map, depth - 1, new_node, alpha, beta)

            if child_val < v:
                v = child_val
                best_bunnyMoves = new_node.bunnyMoves
                best_hunterMoves = new_node.hunterMoves

            beta = min(beta, v)
            if beta <= alpha:
                break

        return v, best_bunnyMoves, best_hunterMoves








