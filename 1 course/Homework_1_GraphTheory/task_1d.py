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
    num, name = pars_one[0], pars_one[1][:-1]
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

# Колдую над цветом
colors_map = []
colors_dict = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.3, 0.2, 0]  # список всех цветов
colors_friend = [[] for i in range(V)]  # список соседей у вершины

# Красим рёбра на рандом в 9 цветов
# Для каждого ребра a-b находим такой цвет, который ещё не встречался ранее
# в других рёбрах у вершин a и b.
for i in edges:
    c = 0
    a = i[0]
    b = i[1]
    for j in colors_dict:
        if not (j in colors_friend[a] or j in colors_friend[b]):
            c = j
            break

    colors_map.append(c)
    colors_friend[a].append(c)
    colors_friend[b].append(c)

edge_colors = []

# Можем проверить что все рёбра покрашены
print(colors_map)

# Посмотрим на полученный граф
plt.figure(figsize=(20, 20))
pos = nx.planar_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color=colors_map)

plt.show()
