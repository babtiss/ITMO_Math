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
matrix = [[] for i in range(V)]  
#
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

# Найдём все клики (4-ёх вершинные и больше) с помощью функции либы networkx
cliques = [clique for clique in nx.find_cliques(G) if len(clique) > 3]
с = 0
# Выводим то что получилось
for clique in cliques:
    с += 1
    print("Clique ", с, clique)
