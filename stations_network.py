import networkx as nx
import matplotlib.pyplot as plt
import random


G = nx.Graph()

for i in range(1, 51):
    G.add_node(f"Station{i}")

    if i > 1:
        G.add_edge(f"Station{i}", f"Station{random.randint(1, i-1)}")

for _ in range(95):
    u = random.choice(list(G.nodes()))
    v = random.choice(list(G.nodes()))
    if u != v:
        G.add_edge(u, v)

nx.draw(G, with_labels=True, node_size=700, node_color="lightblue", font_size=8)
plt.show()

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Ступені вершин:", dict(G.degree()))
print(f"Щільність графа: {nx.density(G)}")
print(f"Кількість компонентів зв'язності: {nx.number_connected_components(G)}")
if nx.is_connected(G):
    print(f"Діаметр графа: {nx.diameter(G)}")
if nx.is_connected(G):
    print(f"Середній найкоротший шлях: {nx.average_shortest_path_length(G)}")
print(f"Середній кластерний коефіцієнт: {nx.average_clustering(G)}")

# DFS
dfs_tree = nx.dfs_tree(G, source="Station5")
print("DFS Tree:", dfs_tree.edges())

# BFS
bfs_tree = nx.bfs_tree(G, source="Station5")
print("BFS Tree:", bfs_tree.edges())

for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)

if nx.has_path(G, "Station1", "Station50"):
    path = nx.dijkstra_path(G, source="Station1", target="Station50")
    path_length = nx.dijkstra_path_length(G, source="Station1", target="Station50")
    print("Найкоротший шлях від Станції 1 до Станції 50:", path)
    print("Довжина шляху:", path_length)
else:
    print("Такий шлях відсутній.")
