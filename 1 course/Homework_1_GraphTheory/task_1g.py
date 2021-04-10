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
edges_name = []
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
    edges_name.append((country[a], country[b]))

# создадим граф
for i in range(E):
    a, b = edges[i]
    G.add_edge(country[a], country[b])

# считаем ответ с помощью функции либы networkx
answer = nx.maximal_matching(G)

# выводим ответ
for i in answer:
    print(i)
print(len(answer))

# Раскрасим паросочетание
colors = ['b'] * E
c = -1
for i in G.edges():
    c += 1
    a, b = i
    if ((a, b) in answer) or ((b, a) in answer):
        colors[c] = 'r'


# Посмотрим на полученный граф
plt.figure(figsize=(20, 20))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=1000)
nx.draw_networkx_labels(G, pos, font_size=21)
nx.draw_networkx_edges(G, pos, edge_color=colors)

plt.show()
