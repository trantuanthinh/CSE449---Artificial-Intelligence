from time import sleep


class Solution:
    def solve(self, board):
        # Dictionary to store the states and their respective distances from the start state
        state_distances = {}

        # Flatten the 2D board to a tuple
        flatten = []
        for row in board:
            flatten += row
        flatten = tuple(flatten)

        # Initialize the dictionary with the start state
        state_distances[flatten] = 0

        # Check if the start state is the goal state
        if flatten == (0, 1, 2, 3, 4, 5, 6, 7, 8):
            return 0

        # Perform BFS to find the shortest path to the goal state
        return self.get_paths(state_distances)

    def get_paths(self, state_distances):
        cnt = 0
        while True:
            # Get all nodes at the current distance
            current_nodes = [
                node for node in state_distances if state_distances[node] == cnt
            ]

            # If there are no more nodes to explore, return -1 (no solution)
            if not current_nodes:
                return -1

            for node in current_nodes:
                # Get all possible next moves from the current node
                next_moves = self.find_next(node)
                sleep(2)
                print(next_moves)

                for move in next_moves:
                    if move not in state_distances:
                        # Assign the distance to the next move
                        state_distances[move] = cnt + 1

                        # Check if the next move is the goal state
                        if move == (0, 1, 2, 3, 4, 5, 6, 7, 8):
                            return cnt + 1
            cnt += 1

    def find_next(self, node):
        # Possible moves for each position on the board
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7],
        }

        # Find the position of the empty tile (represented by 0)
        pos_0 = node.index(0)
        results = []

        # Generate new states by swapping the empty tile with its adjacent tiles
        for move in moves[pos_0]:
            new_node = list(node)
            new_node[move], new_node[pos_0] = new_node[pos_0], new_node[move]
            results.append(tuple(new_node))
        return results


# Initialize the puzzle and solve it
ob = Solution()
matrix = [[3, 1, 2], [4, 7, 5], [6, 8, 0]]
print(ob.solve(matrix))
