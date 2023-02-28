from operator import itemgetter

# Preparing the inputs
file = open('cvicenie2data.txt', 'r')
number_of_stuff = file.readline()
number_of_stuff = number_of_stuff.split()
number_of_stuff = [int(x) for x in number_of_stuff]
number_of_vertices = number_of_stuff[0]
number_of_edges = number_of_stuff[1]
lines = [0] * number_of_edges
skeleton = [0] * (number_of_vertices - 1)
skeleton_edges = [0]

# Reading the lines from the input file
for i in range(number_of_edges):
    x = file.readline()
    x = x.split()
    line = [int(j) for j in x]
    lines[i] = line


# ChatGPT helped with the perfection of this function
# Function to check if edge already exits in skeleton
def creates_cycle(edges, new_edge):
    # Create a dictionary to store the graph
    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        if v not in graph:
            graph[v] = []
        graph[v].append(u)

    # Perform DFS to check if the new edge creates a cycle
    visited = set()
    stack = [new_edge[0]]
    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor == new_edge[1]:
                return True
            elif neighbor not in visited:
                stack.append(neighbor)

    return False


# Kruskal algorithm
lines = sorted(lines, key=itemgetter(2))
current = 1
skeleton[0] = lines[0]
skeleton_edges[0] = [lines[0][0], lines[0][1]]
visited = set()
for i in range(1, number_of_edges):
    if creates_cycle(skeleton_edges, [lines[i][0], lines[i][1]]):
        continue
    else:
        skeleton[current] = lines[i]
        skeleton_edges.append([lines[i][0], lines[i][1]])
        current += 1

print(skeleton)
