# Number of vertices in the graph
V = 4
answer = []


# Function to find the minimum weight Hamiltonian Cycle
def tsp(graph, v, currPos, n, count, cost):
    # If last node is reached and it has a link to the starting node
    # i.e., the source, then keep the minimum value out of the total cost
    # of traversal and "answer"
    if count == n and graph[currPos][0]:
        answer.append(cost + graph[currPos][0])
        return

    # BACKTRACKING STEP
    # Loop to traverse the adjacency list of currPos node and increasing the count
    # by 1 and cost by graph[currPos][i] value
    for i in range(n):
        if not v[i] and graph[currPos][i]:
            v[i] = True
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i])
            v[i] = False


if __name__ == "__main__":
    n = 4
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

    v = [False for i in range(n)]

    v[0] = True

    tsp(graph, v, 0, n, 1, 0)

    print("The minimum cost is:", min(answer))
