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

friends = [0 for i in range(V)]  # соседние цвета
colors = [-1 for i in range(V)]  # цвета


# BFS по вершинам (реализация жадного алгоритма, т.е. красит, если может)
# Выбираем откуда стартовать
def check(start):
    global matrix, friends, colors
    q = [start]
    q2 = []
    while q:
        x = q.pop()
        if friends[x] == 0:
            colors[x] = 1
        else:
            colors[x] = 0

        for v in matrix[x]:
            if colors[v] == -1:
                friends[v] = max(friends[v], colors[x])
                q2.append(v)

        if not q:
            q = q2[:]
            q2 = []

# Выбираем откуда стартовать (до этого был запущен цикл и было выяснено, что
# для вершины 0 будет наилучший результат.
start = 0
check(start)

# Выводим нужные данные
colors_map = dict()
c = 0
for i in colors:
    colors_map[country[c]] = i
    if i == 1:
        print(country[c], end=', ')
    c += 1

values = [colors_map.get(node, 0.5) for node in G.nodes()]

# Можем посмотреть как были покрашены вершины
print()
print(sum(colors))
print(colors)

# Посмотрим на полученный граф
plt.figure(figsize=(20, 20))
pos = nx.planar_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=1000, node_color=values)
nx.draw_networkx_labels(G, pos, font_size=20)
nx.draw_networkx_edges(G, pos)

plt.show()
