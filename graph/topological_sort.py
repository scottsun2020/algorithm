from collections import deque, defaultdict

def topological_sort(vertices, edges):
    #step 1: build adjacency list and computer in-degree
    #edges: 1-> 2; 1-> 3
    adj_list = defaultdict(list)
    in_degree = {v: 0 for v in vertices}

    #initialize the edges for incoming
    for u, v in edges:
        adj_list[u].append(v)
        #count incoming edges 1 -> 2 ; 1->3 so 2 and 3 has 1 incoming edge 
        in_degree[v] += 1 

    #step 2: start queue with nodes having in-degree 0
    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []

    #step 3: process the queue
    while queue: 
        #get the vertice has degree 0 
        node = queue.popleft()
        topo_order.append(node)

        #reduce the in-dgeree of adjecent neighbor
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return topo_order


# Example Graph
vertices = {'A', 'B', 'C', 'D', 'E', 'F'}
edges = [('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E'), ('E', 'F')]

# Run Topological Sorting
topo_order = topological_sort(vertices, edges)
print("Topological Order (BFS):", topo_order)

