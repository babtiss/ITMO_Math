import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Input
V = 42
E = 87
fin_country = open("europe.txt")
fin_edges = open("distances.txt")
country = []  # список стран
edges = []  # список рёбер (num, num)
edges_name = []  # список рёбер (name, name)
G = nx.Graph()  # граф
matrix = [[] for i in range(V)]  
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
# считаем ответ
answer = nx.maximal_matching(G)

# Раскрасим паросочетание
colors = ['b'] * E
c = -1
visited = dict()  # Словарь вершин вошедших в паросочетание
for i in G.edges():
    c += 1
    a, b = i
    if ((a, b) in answer) or ((b, a) in answer):
        colors[c] = 'r'
        visited[a] = 1
        visited[b] = 1

# Найдём те вершины, которые не вошли в паросочетание
for i in country:
    if not i in visited:
        print(i, end=', ')

# Скопировал вершины в список
edges_not_in_matching = [('Denmark', 'Germany'),
                         ('Estonia', 'Latvia'),
                         ('Finland', 'Sweden'),
                         ('Kosovo', 'Serbia'),
                         ('Luxembiurg', 'France'),
                         ('Monaco', 'France'),
                         ('Netherlands', 'Belgium'),
                         ('SanMarino', 'Italy'),
                         ('Turkey', 'Greece'),
                         ('Vatican', 'Italy')]

# Покрасим в красный все рёбра из паросочетания
c = -1
for i in G.edges():
    c += 1
    a, b = i
    if ((a, b) in edges_not_in_matching) or ((b, a) in edges_not_in_matching):
        colors[c] = 'r'

# Посмотрим на полученный граф
plt.figure(figsize=(18, 14))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color=colors)

plt.show()
