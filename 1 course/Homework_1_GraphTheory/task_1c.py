import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Input
V = 42
E = 87
fin_country = open("europe.txt")
fin_edges = open("distances.txt")
country = []  # список стран
edges = []  # список рёбер
G = nx.Graph()  # граф
matrix = [[] for i in range(V)]  # матрица смежности
for i in range(V):
    pars_one = fin_country.readline().split('.')
    if i != V - 1:
        num, name = pars_one[0], pars_one[1][:-1]
    else:
        num, name = pars_one[0], pars_one[1]
    country.append(name)

for i in range(E):
    pars_two = fin_edges.readline().split()
    a, b = int(pars_two[0]), int(pars_two[1])
    matrix[a].append(b)
    matrix[b].append(a)
    edges.append([a, b])

# создадим граф
for i in range(E):
    a, b = edges[i]
    G.add_edge(country[a], country[b])


colors_map = {}  # цвет каждой вершины
colors_dict = [1, 0.5, 0.3, 0.1]  # палитра цветов
colors_friend = [[] for i in range(V)]  # список соседей у вершины


# Пробуем покрасить в 4 цвета bfs-ом
def bfs(colors_dict, colors_map, matrix, colors_friend, visited):
    start = 0
    q = [start]
    q2 = []
    name = country[start]
    colors_map[name] = 1
    while q:
        x = q.pop()
        name = country[x]
        c = None
        visited[x] = 1
        for i in colors_dict:
            if i not in colors_friend[x]:
                c = i
                break
        colors_map[name] = c

        for i in matrix[x]:
            if visited[i] == 0:
                q2.append(i)
                colors_friend[i].append(c)
        if not q:
            q = q2[::]
            q2 = []


visited = [0] * V   # посещена вершина или нет
bfs(colors_dict, colors_map, matrix, colors_friend, visited)
values = [colors_map.get(node, 0.25) for node in G.nodes()]

# Можно проверить что все вершины получили свой цвет
print(values)

# Посмотрим на полученный граф
plt.figure(figsize=(20, 20))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, font_size =25)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500, node_color=values)
nx.draw_networkx_edges(G, pos)
plt.show()
