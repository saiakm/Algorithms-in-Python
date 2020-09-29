"""
Breadth-First Search is an algorithm to traverse or search in data structures like a tree or a graph. 
The algorithm starts with a root node and visit the node itself first. 
Then traverse its neighbors, traverse its second level neighbors, traverse its third level neighbors, so on and so forth.
"""

#defining an undirected graph with 8 vertices
#the graph is represented in adjacency list format
graph = {1:[2,3],2:[1,3,4,5],3:[1,5,7,8],4:[2,5],5:{2,3,4,6},6:[5],7:[3,8],8:[3,7]}
root = 1

import collections

def bfs(root):
    bfs_result = []
    queue = collections.deque([root])
    visited = set() #set holds the elements already visited, it helps us from revisiting a node 
    #add root to visited set
    visited.add(root)
    while queue:
        node = queue.popleft()
        bfs_result.append(node)
        for adj_node in graph[node]:
            if adj_node not in visited:
                queue.append(adj_node)
                visited.add(adj_node)

    return bfs_result

bfs_result = bfs(root)
print("Order of visiting nodes:",bfs_result)


#result looks as follows:
#Order of visiting nodes: [1, 2, 3, 4, 5, 7, 8, 6]


