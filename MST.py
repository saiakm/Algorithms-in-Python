#Minimum spanning tree using Kruskal's algorithm
def root(v):
    if par[v] == -1:
        return v
    else:
        par[v] = root(par[v])
        return par[v]

def MST_Kruskal(edges):
    tree_weight = 0
    F = set()
    for edge_weight in edges:
        u,v = edge_weight[0]
        w = edge_weight[1]
        u_prime = root(u)
        v_prime = root(v)
        if u_prime != v_prime:
            F.add((u,v))
            tree_weight+=w
            par[u_prime] = v_prime
    return (F,tree_weight)


input_array=[]

try:
    while 1:
        input_line = input()
        if input_line.strip() == "":
            break
        input_array.append(input_line.split())
except EOFError as E:
    pass


n = int(input_array[0][0])
m = int(input_array[0][1])
V = [i+1 for i in range(n)]
par = {}
for v in V:
    par[v] = -1
edges = []
for i in range(1,m+1):

    u = int(input_array[i][0])
    v = int(input_array[i][1])
    w = int(input_array[i][2])
    edges.append([(u,v),w])
    edges.append([(v,u),w])

edges.sort(key = lambda x: x[1])

F,tree_weight = MST_Kruskal(edges)
print(tree_weight)
for edge in F:
    print(edge[0],edge[1])
